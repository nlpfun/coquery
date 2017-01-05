# -*- coding: utf-8 -*-
"""
managers.py is part of Coquery.

Copyright (c) 2016, 2017 Gero Kunter (gero.kunter@coquery.org)

Coquery is released under the terms of the GNU General Public License (v3).
For details, see the file LICENSE that you should have received along
with Coquery. If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import unicode_literals

import logging
import collections
import math

from .functions import *
from .functionlist import FunctionList
from .general import CoqObject, get_visible_columns
from . import options


class Sorter(CoqObject):
    def __init__(self, column, ascending=True, reverse=False, position=0):
        self.column = column
        self.ascending = ascending
        self.reverse = reverse
        self.position = position


class Manager(CoqObject):
    name = "RESULTS"
    ignore_user_functions = False

    def __init__(self):
        self._functions = []
        self.sorters = []
        self._len_pre_filter = None
        self._len_post_filter = None
        self._len_pre_group_filter = {}
        self._len_post_group_filter = {}
        self.drop_on_na = None
        self.stopwords_failed = False
        self.reset_hidden_columns()

        self.group_functions = FunctionList()
        self.manager_summary_functions = FunctionList()
        self.user_summary_functions = FunctionList()

        self._group_filters = []
        self._filters = []
        self._last_query_id = None
        self.reset_context_cache()

    def reset_context_cache(self):
        self._context_cache = collections.defaultdict(
            lambda: (None, None, None))

    def reset_hidden_columns(self):
        self.hidden_columns = set([])

    def hide_column(self, column):
        self.hidden_columns.add(column)

    def show_column(self, column):
        self.hidden_columns.remove(column)

    def is_hidden_column(self, column):
        return column in self.hidden_columns

    def get_function(self, id):
        for fun in self._functions:
            if type(fun) == type:
                logger.warning("Function {} not found in manager".format(fun))
                return None
            if fun.get_id() == id:
                return fun

    def set_filters(self, filter_list):
        self._filters = filter_list

    def set_group_filters(self, filter_list):
        self._group_filters = filter_list

    def _get_main_functions(self, df, session):
        """
        Returns a list of functions that are provided by this manager.
        They will be executed after user functions.
        """
        l = []

        if options.cfg.context_mode != CONTEXT_NONE:
            # the context columns are only retrieved if there is no cached
            # context for the current context mode and the current query.
            if self._last_query_id != session.query_id:
                self.reset_context_cache()
                self._last_query_id = session.query_id
            (left, right, cached_context) = self._context_cache[options.cfg.context_mode]
            if (left != options.cfg.context_left or
                right != options.cfg.context_right or
                cached_context is None):
                if options.cfg.context_mode == CONTEXT_COLUMNS:
                    l.append(ContextColumns())
                elif options.cfg.context_mode == CONTEXT_KWIC:
                    l.append(ContextKWIC())
                elif options.cfg.context_mode == CONTEXT_STRING:
                    l.append(ContextString())

        return l

    @staticmethod
    def _apply_function(df, fun, session):
        try:
            if fun.single_column:
                df = df.assign(COQ_FUNCTION=lambda d: fun.evaluate(d, session=session))
                return df.rename(columns={"COQ_FUNCTION": fun.get_id()})
            else:
                new_df = df.apply(lambda x: fun.evaluate(x, session=session), axis="columns")
                return pd.concat([df, new_df], axis=1)
        except Exception as e:
            print(e)
            raise e

    def get_group_columns(self, df, session):
        columns = []
        # use group columns as sorters
        for col in options.cfg.group_columns:
            formatted_cols = session.Resource.format_resource_feature(col, session.get_max_token_count())
            for x in formatted_cols:
                if x in df.columns:
                    columns.append(x)
        return columns

    def mutate_groups(self, df, session):
        if (len(df) == 0 or
                len(options.cfg.group_columns) == 0 or
                len(self.group_functions.get_list()) == 0):
            return df
        print("\tmutate_groups({})".format(options.cfg.group_columns))

        grouped = df.groupby(self.get_group_columns(df, session))
        df_new = None
        for dsub in grouped.groups:
            dsub = FunctionList(self.group_functions).apply(
                df.iloc[grouped.groups[dsub]], session=session, manager=self)
            if df_new is None:
                df_new = dsub
            else:
                df_new = pd.concat([df_new, dsub], axis=0)

        print("\tDone mutate_groups")
        return df_new

    def mutate(self, df, session):
        """
        Modify the transformed data frame by applying all needed functions.
        """
        if len(df) == 0:
            return df

        print("\tmutate()")
        # apply manager functions, including context functions:
        manager_functions = FunctionList(self._get_main_functions(df, session))
        df = manager_functions.apply(df, session=session, manager=self)

        if options.cfg.context_mode != CONTEXT_NONE:
            (_, _, cached_context) = self._context_cache[options.cfg.context_mode]
            if cached_context is not None:
                # use the cached context columns if available:
                df = pd.concat([df, cached_context], axis=1)
            else:
                # take the context columns from the data frame if there is no
                # cached context for the current context mode, and store them
                # in the context cache:
                context_columns = [x for x in df.columns
                                   if x.startswith(("coq_context"))]
                self._context_cache[options.cfg.context_mode] = (
                    options.cfg.context_left,
                    options.cfg.context_right,
                    df[context_columns])

        # apply user functions, i.e. functions that were added to
        # individual columns:
        df = FunctionList(session.column_functions).apply(df, session=session, manager=self)
        df = df.reset_index(drop=True)
        print("\tdone")
        return df

    def remove_sorter(self, column):
        self.sorters.remove(self.get_sorter(column))
        for i, x in enumerate(self.sorters):
            x.position = i

    def add_sorter(self, column, ascending=True, reverse=False):
        if self.get_sorter(column):
            self.remove_sorter(column)
        self.sorters.append(Sorter(column, ascending, reverse, len(self.sorters)))

    def get_sorter(self, column):
        for x in self.sorters:
            if x.column == column:
                return x
        return None

    def arrange_groups(self, df, session):
        if len(df) == 0 or len(options.cfg.group_columns) == 0:
            return df

        print("\tarrange_groups({})".format(options.cfg.group_columns))

        columns = self.get_group_columns(df, session)
        columns += ["coquery_invisible_corpus_id"]
        directions = [True] * len(columns)

        # filter columns that should be in the data frame, but which aren't
        # (this may happen for example with the contingency table which
        # takes one column and rearranges it)
        column_check = [x in df.columns for x in columns]
        for i, col in enumerate(column_check):
            if not col:
                directions.pop(i)
                columns.pop(i)

        if COLUMN_NAMES["statistics_column_total"] in df.index:
            # make sure that the row containing the totals is the last row:
            df_data = df[df.index != COLUMN_NAMES["statistics_column_total"]]
            df_totals = df[df.index == COLUMN_NAMES["statistics_column_total"]]
        else:
            df_data = df

        # always sort by coquery_invisible_corpus_id if there is no other
        # sorter -- but not if the session covered multiple queries.

        # sort the data frame (excluding a totals row) with backward
        # compatibility:
        try:
            # pandas <= 0.16.2:
            df_data = df_data.sort(columns=columns,
                            ascending=directions,
                            axis="index")[df.columns]
        except AttributeError:
            # pandas >= 0.17.0
            df_data = df_data.sort_values(by=columns,
                                    ascending=directions,
                                    axis="index")[df.columns]
        if COLUMN_NAMES["statistics_column_total"] in df.index:
            # return sorted data frame plus a potentially totals row:
            df = pd.concat([df_data, df_totals])
        else:
            df = df_data
        df = df.reset_index(drop=True)
        print("\tdone")
        return df

    def arrange(self, df, session):
        if len(df) == 0:
            print("exit arrange")
            return df

        print("\tarrange()")

        original_columns = df.columns
        columns = []
        directions = []

        # list that stores unusuable sorters (e.g. because the sorter
        # refers to a function column and the function has been deleted):
        drop_list = []
        if self.sorters:
            # gather sorting information:
            for sorter in self.sorters:
                # create dummy columns for reverse sorting:
                if sorter.reverse:
                    target = "{}__rev".format(sorter.column)
                    df[target] = (df[sorter.column].apply(lambda x: x[::-1]))
                else:
                    target = sorter.column

                if target not in df.columns:
                    drop_list.append(target)
                else:
                    columns.append(target)
                    directions.append(sorter.ascending)

        # drop illegal sorters:
        self.sorters = [x for x in self.sorters if x not in drop_list]

        # filter columns that should be in the data frame, but which aren't
        # (this may happen for example with the contingency table which
        # takes one column and rearranges it)
        column_check = [x in original_columns for x in columns]
        for i, col in enumerate(column_check):
            if not col and not columns[i].endswith("__rev"):
                directions.pop(i)
                columns.pop(i)

        if COLUMN_NAMES["statistics_column_total"] in df.index:
            # make sure that the row containing the totals is the last row:
            df_data = df[df.index != COLUMN_NAMES["statistics_column_total"]]
            df_totals = df[df.index == COLUMN_NAMES["statistics_column_total"]]
        else:
            df_data = df

        if len(columns) == 0:
            return df

        # sort the data frame (excluding a totals row) with backward
        # compatibility:
        try:
            # pandas <= 0.16.2:
            df_data = df_data.sort(columns=columns,
                            ascending=directions,
                            axis="index")[original_columns]
        except AttributeError:
            # pandas >= 0.17.0
            df_data = df_data.sort_values(by=columns,
                                    ascending=directions,
                                    axis="index")[original_columns]
        except Exception as e:
            print(e)
            print(columns, directions)
            raise e

        df_data = df_data.reset_index(drop=True)

        if COLUMN_NAMES["statistics_column_total"] in df.index:
            # return sorted data frame plus a potentially totals row:
            df = pd.concat([df_data, df_totals])
        else:
            df = df_data
        print("\tdone")

        df = df[[x for x in df.columns if not x.endswith("__rev")]]
        return df

    def summarize(self, df, session):
        print("\tsummarize()")
        vis_cols = get_visible_columns(df, manager=self, session=session)

        df = self.manager_summary_functions.apply(df, session=session, manager=self)
        if not self.ignore_user_functions:
            df = self.user_summary_functions.apply(df,
                                                   session=session,
                                                   manager=self)

        cols = [x for x in vis_cols if x.startswith("coq_")]

        if options.cfg.drop_on_na and cols:
            ix = df[vis_cols].dropna(axis="index",
                                     subset=cols,
                                     how="all").index
            df = df.iloc[ix]

        print("\tdone")
        return df

    def set_summary_functions(self, l):
        if l is None:
            l = []
        self.user_summary_functions.set_list([x(sweep=True) for x in l])

    def set_group_functions(self, l):
        if l is None:
            l = []
        self.group_functions.set_list([x(sweep=True) for x in l])

    def distinct(self, df, session):
        vis_cols = get_visible_columns(df, manager=self, session=session)
        try:
            df = df.drop_duplicates(subset=vis_cols)
        except ValueError:
            # ValueError is raised if df is empty
            pass
        return df.reset_index(drop=True)

    def filter(self, df, session):
        if (len(df) == 0 or not self._filters):
            return df

        self.reset_group_filter_statistics()
        self._len_pre_filter = len(df)
        print("\tfilter()")
        for filt in self._filters:
            print("\t\t", filt)
            df = filt.apply(df)
        print("\tdone")
        df = df.reset_index(drop=True)
        self._len_post_filter = len(df)
        return df

    def get_available_columns(self, session):
        pass

    def reset_filter_statistics(self):
        self._len_pre_filter = None
        self._len_post_filter = None

    def reset_group_filter_statistics(self):
        self._len_pre_group_filter = {}
        self._len_post_group_filter = {}

    def filter_groups(self, df, session):
        if (len(df) == 0 or
                len(options.cfg.group_columns) == 0 or
                len(self._group_filters) == 0):
            return df

        print("\tfilter_groups()")
        self.reset_group_filter_statistics()

        columns = self.get_group_columns(df, session)
        grouped = df.groupby(columns)
        new_df = pd.DataFrame(columns=df.columns)
        for x in grouped.groups:
            _df = df.iloc[grouped.groups[x]]
            _df = _df.reset_index(drop=True)
            self._len_pre_group_filter[x] = len(_df)
            for filt in self._group_filters:
                _df = filt.apply(_df)
            new_df = pd.concat([new_df, _df], axis=0)
            self._len_post_group_filter[x] = len(_df)
        print("\tdone")
        new_df = new_df.reset_index(drop=True)
        return new_df

    def select(self, df, session):
        """
        Select the columns that will appear in the final output. Also, put
        them into the preferred order.
        """
        print("\tselect()")

        # 'coquery_dummy' is used to manage frequency queries with zero
        # matches. It is never displayed:
        vis_cols = [x for x in df.columns if x != "coquery_dummy"]

        resource = session.Resource

        lexical_features = []
        corpus_features = []
        functions = []
        others = []

        for col in list(vis_cols):
            if col.startswith("coq_"):
                this_res = resource
                this_rc_feature = resource.extract_resource_feature(col)
            elif col.startswith("db_"):
                fields = col.split("_")
                last_index = len(fields) - fields[::-1].index("coq") - 1
                db_name = "_".join(fields[1:last_index])
                this_res = options.get_resource_of_database(db_name)
                this_rc_feature = "_".join(fields[last_index + 1:-1])
            elif col.startswith("func_"):
                functions.append(col)
                continue
            else:
                others.append(col)
                continue
            if this_res.is_lexical(this_rc_feature):
                lexical_features.append(col)
            else:
                corpus_features.append(col)

        resource_order = resource.get_preferred_output_order()
        for feature in resource_order[::-1]:
            lex_list = [col for col in lexical_features if feature in col]
            lex_list = sorted(lex_list)[::-1]
            for lex in lex_list:
                lexical_features.remove(lex)
                lexical_features.insert(0, lex)

        vis_cols = lexical_features + corpus_features + others + functions
        print("\tdone")
        return df[vis_cols]

    def filter_stopwords(self, df, session):
        self.stopwords_failed = False

        if not options.cfg.stopword_list:
            return df

        print("\tfilter_stopwords({})".format(options.cfg.stopword_list))
        word_id_column = getattr(session.Resource, QUERY_ITEM_WORD)
        columns = []
        for col in df.columns:
            if col.startswith("coq_{}_".format(word_id_column)):
                columns.append(col)
        if columns == []:
            self.stopwords_failed = True
            return df

        stopwords = [x.lower() for x in options.cfg.stopword_list]
        valid = ~(df[columns].apply(lambda x: x.str.lower())
                             .isin(stopwords)).apply(any, axis="columns")
        print("\tdone")
        return df[valid]

    def process(self, df, session, recalculate=True):
        print("process()")
        df = df.reset_index(drop=True)
        self.drop_on_na = None
        self._group_functions = []

        if options.cfg.stopword_list:
            df = self.filter_stopwords(df, session)

        df = df[[x for x in df.columns if not x.startswith("func_")]]
        df = self.mutate(df, session)

        if options.cfg.group_columns:
            df = self.filter_groups(df, session)
            df = self.arrange_groups(df, session)
            df = self.mutate_groups(df, session)

        df = self.filter(df, session)
        df = self.summarize(df, session)
        df = self.select(df, session)
        self._functions = (self._group_functions +
                        session.column_functions.get_list() +
                        self.group_functions.get_list() +
                        self.manager_summary_functions.get_list() +
                        self.user_summary_functions.get_list())

        print("done")
        return df

class Types(Manager):
    def summarize(self, df, session):
        df = super(Types, self).summarize(df, session)
        return self.distinct(df, session)


class FrequencyList(Manager):
    name = "FREQUENCY"

    def summarize(self, df, session):
        vis_cols = get_visible_columns(df, manager=self, session=session)
        freq_function = Freq(columns=vis_cols)

        if not self.user_summary_functions.has_function(freq_function):
            self.manager_summary_functions = FunctionList([freq_function])
        df = super(FrequencyList, self).summarize(df, session)
        return self.distinct(df, session)


class ContingencyTable(FrequencyList):
    name = "CONTINGENCY"

    def select(self, df, session):
        l = list(super(ContingencyTable, self).select(df, session).columns)
        for col in [x for x in df.columns if x != "coquery_dummy"]:
            if col not in l:
                l.append(col)

        # make sure that the frequency column is shown last:
        freq = self.manager_summary_functions.get_list()[0].get_id()
        l.remove(freq)
        l.append(freq)
        df = df[l]
        l[-1] = "statistics_column_total"
        df.columns = l
        return df

    def summarize(self, df, session):
        def _get_column_label(row):
            if row[1] == "All":
                if agg_fnc[row[0]] == sum:
                    s = "{}(TOTAL)"
                elif agg_fnc[row[0]] == np.mean:
                    s = "{}(MEAN)"
                else:
                    s = "{}({}=ANY)"
                return s.format(row[0], row.index[1])
            elif row[1]:
                return "{}({}='{}')".format(row[0],
                                            session.translate_header(row.index[1]),
                                            row[1].replace("'", "''"))
            else:
                return row[0]

        df = super(ContingencyTable, self).summarize(df, session)

        vis_cols = get_visible_columns(df, manager=self, session=session)

        cat_col = list(df[vis_cols]
                       .select_dtypes(include=[object]).columns.values)
        num_col = (list(df[vis_cols]
                        .select_dtypes(include=[np.number]).columns.values) +
                   ["coquery_invisible_number_of_tokens",
                    "coquery_invisible_corpus_id",
                    "coquery_invisible_origin_id"])

        # determine appropriate aggregation functions:
        # - internal columns that are needed for context look-up take
        #   the first value (so clicking on a cell in the contingency
        #   table returns the first matching context)
        # - frequency functions return the sum
        # - all other numeric columns return the mean
        agg_fnc = {}
        for col in num_col:
            if col.startswith(("coquery_invisible")):
                agg_fnc[col] = lambda x: int(x.values[0])
            elif col.startswith(("func_Freq")):
                agg_fnc[col] = sum
            else:
                agg_fnc[col] = np.mean

        if len(cat_col) > 1:
            # Create pivot table:
            piv = df.pivot_table(index=cat_col[:-1],
                                columns=[cat_col[-1]],
                                values=num_col,
                                aggfunc=agg_fnc,
                                fill_value=0)
            piv = piv.reset_index()

            # handle the multi-index that pivot_table() creates:
            l1 = pd.Series(piv.columns.levels[-2][piv.columns.labels[-2]])
            l2 = pd.Series(piv.columns.levels[-1][piv.columns.labels[-1]])

            piv.columns = pd.concat([l1, l2], axis=1).apply(_get_column_label, axis="columns")
        else:
            piv = df

        # Ensure that the pivot columns have the same dtype as the original
        # column:
        for x in piv.columns:
            match = re.search("(.*)\(.*\)", x)
            if match:
                name = match.group(1)
            else:
                name = x
            if piv.dtypes[x] != df.dtypes[name]:
                piv[x] = piv[x].astype(df.dtypes[name])

        if len(cat_col) > 1:
            # Sort the pivot table
            try:
                # pandas <= 0.16.2:
                piv = piv.sort(columns=cat_col[:-1], axis="index")
            except AttributeError:
                # pandas >= 0.17.0
                piv = piv.sort_values(by=cat_col[:-1], axis="index")

        bundles = collections.defaultdict(list)
        d = {}

        # row-wise apply the aggregate function
        for x in piv.columns[(len(cat_col)-1):]:
            col = x.rpartition("(")[0]
            if col:
                bundles[col].append(x)
        for col in bundles:
            piv[col] = piv[bundles[col]].apply(agg_fnc[col], axis="columns")
        # add summary row:
        for x in piv.columns[(len(cat_col)-1):]:
            rc_feature = x.partition("(")[0]
            if rc_feature in agg_fnc:
                fnc = agg_fnc[rc_feature]
                d[x] = fnc(piv[x])
        row_total = pd.DataFrame([pd.Series(d)],
                                columns=piv.columns,
                                index=[COLUMN_NAMES["statistics_column_total"]]).fillna("")
        piv = piv.append(row_total)
        return piv


class Collocations(Manager):
    """
    Manager class which calculates the collocation measures for the
    current results table.

    The basic algorithm works like this:
    (1) Get a list of all words in the left and right context
    (2) Count how often each word occurs (separately either in the
        left or in the right context)
    """

    ignore_user_functions = True

    def _get_main_functions(self, df, session):
        """
        This manager will always use a ContextColumn function.
        """
        # FIXME:
        # If the context span is zero (i.e. neither a left nor a right
        # context, the program should alert the user somehow.
        return [ContextColumns()]

    def filter(self, df, session):
        return df

    def summarize(self, df, session):
        """
        This returns a completely different data frame than the argument.
        """

        # FIXME: reimplement a function that returns the corpus
        # size taking current filters into account.
        # Alternatively, get rid of this function call if the
        # corpus size can be handled correctly by an appropriate
        # function
        # Probably, the best solution is to take the queried corpus
        # features into account when calculating the collcations.
        # This would make a comparison of collactions in e.g. COCA across
        # genres fairly easy. In order to do this, all corpus features
        # should be included in the aggregation, and the _subcorpus_size()
        # function should be used to get the correct size.
        # If no corpus features are selected, the whole corpus will be
        # used.
        corpus_size = session.Resource.corpus.get_corpus_size()

        left_cols = ["coq_context_lc{}".format(x + 1) for x in range(options.cfg.context_left)]
        right_cols = ["coq_context_rc{}".format(x + 1) for x in range(options.cfg.context_right)]

        left_context_span = df[left_cols]
        right_context_span = df[right_cols]

        # convert all context columns to upper or lower case unless
        # the current setting says otherwise
        if not options.cfg.output_case_sensitive:
            if options.cfg.output_to_lower:
                left_context_span = left_context_span.apply(lambda x: x.apply(str.lower))
                right_context_span = right_context_span.apply(lambda x: x.apply(str.lower))
            else:
                left_context_span = left_context_span.apply(lambda x: x.apply(str.upper))
                right_context_span = right_context_span.apply(lambda x: x.apply(str.upper))

        left = left_context_span.stack().value_counts()
        right = right_context_span.stack().value_counts()

        all_words = [x for x in set(list(left.index) + list(right.index)) if x]

        left = left.reindex(all_words).fillna(0).astype(int)
        right = right.reindex(all_words).fillna(0).astype(int)

        collocates = pd.concat([left, right], axis=1)
        collocates = collocates.reset_index()
        collocates.columns = ["coq_collocate_label", "coq_collocate_frequency_left", "coq_collocate_frequency_right"]

        # calculate collocate frequency (i.e. occurrences of the collocate
        # in the context
        collocates["coq_collocate_frequency"] = collocates[["coq_collocate_frequency_left", "coq_collocate_frequency_right"]].sum(axis=1)
        # calculate total frequency of collocate
        collocates["statistics_frequency"] = collocates["coq_collocate_label"].apply(
            session.Resource.corpus.get_frequency, engine=session.db_engine)
        # calculate conditional probabilities:
        func = ConditionalProbability()
        collocates["coq_conditional_probability"] = func.evaluate(
            collocates,
            freq_cond="coq_collocate_frequency",
            freq_total="statistics_frequency")
        collocates["coq_conditional_probability_left"] = func.evaluate(
            collocates,
            freq_cond="coq_collocate_frequency_left",
            freq_total="statistics_frequency")
        collocates["coq_conditional_probability_right"] = func.evaluate(
            collocates,
            freq_cond="coq_collocate_frequency_right",
            freq_total="statistics_frequency")

        func = MutualInformation()
        collocates["coq_mutual_information"] = func.evaluate(collocates,
                            f_1=len(df),
                            f_2="statistics_frequency",
                            f_coll="coq_collocate_frequency",
                            size=corpus_size,
                            span=len(left_cols) + len(right_cols))

        aggregate = collocates.drop_duplicates(subset="coq_collocate_label")

        # FIXME:
        # now that we have the collocations table, the summarize filters
        # should be applied, and perhaps also summarize functions?

        for filt in self._filters:
            aggregate = filt.apply(aggregate)
        aggregate = aggregate.reset_index(drop=True)

        order = ["coq_collocate_label",
                 "statistics_frequency",
                 "coq_collocate_frequency",
                 "coq_collocate_frequency_left",
                 "coq_collocate_frequency_right",
                 "coq_conditional_probability",
                 "coq_conditional_probability_left",
                 "coq_conditional_probability_right",
                 "coq_mutual_information"]

        return aggregate[order]


class ContrastMatrix(Manager):
    _ll_cache = {}
    ignore_user_functions = True

    def matrix(self, df, session):
        labels = sorted(self.collapse_columns(df, session))
        df["coquery_invisible_row_id"] = labels
        df = df.sort_values(by="coquery_invisible_row_id")

        for x in labels:
            df["statistics_g_test_{}".format(x)] = df.apply(
                self.retrieve_loglikelihood, axis=1, label=x, df=df)

        return df

    def summarize(self, df, session):
        vis_cols = get_visible_columns(df, manager=self, session=session)
        #df = df.drop_duplicates(subset=vis_cols)

        self.p_correction = math.factorial(len(vis_cols))
        self._freq_function = Freq(columns=vis_cols, alias="coquery_invisible_count")
        self._subcorpus_size = SubcorpusSize(columns=vis_cols, alias="coquery_invisible_size")

        self.manager_summary_functions = FunctionList([self._freq_function,
                                                       self._subcorpus_size])
        df = super(ContrastMatrix, self).summarize(df, session)
        df = self.matrix(df, session)

        return df

    def select(self, df, session):
        df = super(ContrastMatrix, self).select(df, session)
        vis_cols = get_visible_columns(df, manager=self, session=session)
        for i, x in enumerate(vis_cols):
            if x.startswith("statistics_g_test"):
                self._start_pos = i
                break
        return df

    def collapse_columns(self, df, session):
        """
        Return a list of strings. Each string contains the concatinated
        content of the feature cells in each row of the data frame.
        """
        # FIXME: columns should be processed in the order that they appear in
        # the None results table view.

        def fnc(x, cols=[]):
            l = [x[col] for col in cols]
            return ":".join(l)

        vis_cols = get_visible_columns(df, manager=self, session=session)
        vis_cols = [x for x in vis_cols
                    if not x in (self._freq_function.get_id(),
                                 self._subcorpus_size.get_id())]
        return df.apply(fnc, cols=vis_cols, axis=1).unique()

    def retrieve_loglikelihood(self, row, df, label):
        def g_test(freq_1, freq_2, total_1, total_2):
            """
            This method calculates the G test statistic as described here:
            http://ucrel.lancs.ac.uk/llwizard.html

            For a formal description of the G² test, see Agresti (2013: 76).
            """
            if (freq_1, freq_2, total_1, total_2) not in ContrastMatrix._ll_cache:
                exp1 = total_1 * (freq_1 + freq_2) / (total_1 + total_2)
                exp2 = total_2 * (freq_1 + freq_2) / (total_1 + total_2)

                G = 2 * (
                    (freq_1 * math.log(freq_1 / exp1)) +
                    (freq_2 * math.log(freq_2 / exp2)))

                ContrastQuery._ll_cache[(freq_1, freq_2, total_1, total_2)] = G
            return ContrastQuery._ll_cache[(freq_1, freq_2, total_1, total_2)]

        if options.use_scipy:
            from scipy import stats

        freq = self._freq_function.get_id()
        size = self._subcorpus_size.get_id()

        freq_1 = row[freq]
        total_1 = row[size]

        freq_2 = df[df["coquery_invisible_row_id"] == label][freq].values[0]
        total_2 = df[df["coquery_invisible_row_id"] == label][size].values[0]

        obs = [[freq_1, freq_2], [total_1 - freq_1, total_2 - freq_2]]
        try:
            if options.use_scipy:
                g2, p_g2, _, _ = stats.chi2_contingency(obs, correction=False, lambda_="log-likelihood")
                return g2
            else:
                return g_test(freq_1, freq_2, total_1, total_2)
        except ValueError:
            print(label)
            print(df)
            print(obs)
            return None

    def get_cell_content(self, index, df, session):
        """
        Return that content for the indexed cell that is needed to handle
        a click on it for the current aggregation.
        """
        row = df.iloc[index.row()]
        column = df.iloc[index.column() - self._start_pos]

        freq_1 = row[self._freq_function.get_id()]
        total_1 = row[self._subcorpus_size.get_id()]
        label_1 = row["coquery_invisible_row_id"]

        freq_2 = column[self._freq_function.get_id()]
        total_2 = column[self._subcorpus_size.get_id()]
        label_2 = column["coquery_invisible_row_id"]

        return {"freq_row": freq_1, "freq_col": freq_2,
                "total_row": total_1, "total_col": total_2,
                "label_row": label_1, "label_col": label_2}


def manager_factory(manager):
    if manager == QUERY_MODE_TYPES:
        return Types()
    elif manager == QUERY_MODE_FREQUENCIES:
        return FrequencyList()
    elif manager == QUERY_MODE_CONTINGENCY:
        return ContingencyTable()
    elif manager == QUERY_MODE_COLLOCATIONS:
        return Collocations()
    elif manager == QUERY_MODE_CONTRASTS:
        return ContrastMatrix()
    else:
        return Manager()


def get_manager(manager, resource):
    """
    Returns a data manager
    """
    try:
        return options.cfg.managers[resource][manager]
    except KeyError:
        if resource not in options.cfg.managers:
            options.cfg.managers[resource] = {}
        new_manager = manager_factory(manager)
        options.cfg.managers[resource][manager] = new_manager
    finally:
        return options.cfg.managers[resource][manager]

logger = logging.getLogger(NAME)
