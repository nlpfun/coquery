# -*- coding: utf-8 -*-
""" 
beeswarmplot.py is part of Coquery.

Copyright (c) 2015 Gero Kunter (gero.kunter@coquery.org)

Coquery is released under the terms of the GNU General Public License.
For details, see the file LICENSE that you should have received along 
with Coquery. If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import print_function

import options
from defines import *
from pyqt_compat import QtGui

import visualizer as vis
import seaborn as sns
import matplotlib.pyplot as plt

from beeswarm import *

class Visualizer(vis.BaseVisualizer):
    dimensionality = 1

    def format_coord(self, x, y, title):
        return "Corpus position: {}".format(int(y))
    
    def setup_figure(self):
        with sns.axes_style("whitegrid"):
            super(Visualizer, self).setup_figure()
 
    def set_defaults(self):
        self.options["color_palette"] = "Paired"
        self.options["color_number"] = len(self._levels[0])
        super(Visualizer, self).set_defaults()
        self.options["label_y_axis"] = "Corpus position"
        if not self._levels or len(self._levels[0]) < 2:
            self.options["label_x_axis"] = ""
        else:
            self.options["label_x_axis"] = self._groupby[0]

    def onclick(self, event):
         options.cfg.main_window.result_cell_clicked(token_id=int(event.ydata))
 
    def draw(self):
        def plot_facet(data, color):
            values = [data[data[self._groupby[-1]] == x]["coquery_invisible_corpus_id"].values for x in self._levels[-1]]

            col = ["#{:02X}{:02X}{:02X}".format(
                    int(255*r), int(255*g), int(255*b)) for r, g, b in self.options["color_palette_values"]][:len(values)]
            beeswarm(
                values=values,
                method="center",
                s=5,
                positions=range(len(self._levels[-1])),
                col=col, 
                ax=plt.gca())
        
        self.g.map_dataframe(plot_facet)
        self.g.set_axis_labels(self.options["label_x_axis"], self.options["label_y_axis"])
        self.g.set(xticklabels=self._levels[-1])
        self.g.fig.tight_layout()

        #sns.despine(self.g.fig, left=False, right=False, top=False, bottom=False)
