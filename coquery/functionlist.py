# -*- coding: utf-8 -*-
"""
functionlist.py is part of Coquery.

Copyright (c) 2016, 2017 Gero Kunter (gero.kunter@coquery.org)

Coquery is released under the terms of the GNU General Public License (v3).
For details, see the file LICENSE that you should have received along
with Coquery. If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import unicode_literals

import pandas as pd
import datetime
import warnings
import sys
import traceback
import logging

from . import options
from .general import CoqObject
from .defines import msg_runtime_error_function


class FunctionList(CoqObject):
    def __init__(self, l=None, *args, **kwargs):
        super(FunctionList, self).__init__()
        self._exceptions = []
        if l:
            self._list = l
        else:
            self._list = []

    def lapply(self, df=None, session=None, manager=None):
        """
        Apply all functions in the list to the data frame.
        """
        # in order to allow zero frequencies for empty result tables, empty
        # data frames can be retained if a function demands it. This is
        # handled by keeping track of the drop_on_na attribute. As soon as
        # one function in the list wishes to retain a data frame that contains
        # NAs, the data frame will not be dropped.
        # This code only keeps track of the attributes. The actual dropping
        # takes place (or doesn't) in the summarize() method of the manager.
        if manager:
            if manager.drop_on_na is not None:
                drop_on_na = True
            else:
                drop_on_na = manager.drop_on_na
        else:
            drop_on_na = True

        self._exceptions = []
        for fun in list(self._list):
            if any(col not in df.columns for col in fun.columns):
                self._list.remove(fun)
                continue

            if options.cfg.drop_on_na:
                drop_on_na = True
            else:
                drop_on_na = drop_on_na and fun.drop_on_na
            try:
                if options.cfg.benchmark:
                    print(fun.get_name())
                    then = datetime.datetime.now()
                    for x in range(5000):
                        val = fun.evaluate(df, **fun.kwargs)
                    print(datetime.datetime.now() - then)
                else:
                    val = fun.evaluate(df, **fun.kwargs)
            except Exception as e:
                # if an exception occurs, the function is removed, and the
                # error is logged.
                self._list.remove(fun)
                error = "Error during function call {}".format(
                    fun.get_label(session))
                logging.exception(error)
                self._exceptions.append((error, e, sys.exc_info()))
            else:
                # Functions can return either single columns or data frames.
                # Handle the function result accordingly:
                new_column = fun.get_id()
                if fun.single_column:
                    df[new_column] = val
                else:
                    df = pd.concat([df, val], axis="columns")
        # tell the manager whether rows with NA will be dropped:
        if manager:
            manager.drop_on_na = drop_on_na
        return df

    def exceptions(self):
        return self._exceptions

    def get_list(self):
        return self._list

    def set_list(self, l):
        self._list = l

    def find_function(self, fun_id):
        for x in self._list:
            if x.get_id() == fun_id:
                return x
        return None

    def has_function(self, fun):
        for x in self._list:
            if x.get_id() == fun.get_id():
                return True
        return False

    def add_function(self, fun):
        if not self.has_function(fun):
            self._list.append(fun)
        else:
            warnings.warn("Function duplicate not added: {}".format(fun))

    def remove_function(self, fun):
        self._list.remove(fun)

        for x in self._list:
            if x.get_id() == fun.get_id():
                self.remove_function(x)

    def replace_function(self, old, new):
        ix = self._list.index(old)
        self._list[ix] = new

        # update references to the replaced function:
        for i, func in enumerate(self._list[ix:]):
            func.columns = [new.get_id() if col == old.get_id() else col
                            for col in func.columns]

    def __iter__(self):
        return self._list.__iter__()

    def __repr__(self):
        s = super(FunctionList, self).__repr__()
        return "{}({})".format(
            s, self._list.__repr__())
