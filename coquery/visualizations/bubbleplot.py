# -*- coding: utf-8 -*-
""" 
bubbleplot.py is part of Coquery.

Copyright (c) 2016 Gero Kunter (gero.kunter@coquery.org)

Coquery is released under the terms of the GNU General Public License (v3).
For details, see the file LICENSE that you should have received along 
with Coquery. If not, see <http://www.gnu.org/licenses/>.
"""
from __future__ import unicode_literals
from __future__ import division
import math

import visualizer as vis
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

class Visualizer(vis.BaseVisualizer):
    dimensionality=2

    sqrt_dict = {}
    circles = []

    def set_defaults(self):
        self.options["color_palette"] = "RdPu"
        self.options["color_number"] = len(self._levels[-1])
        super(Visualizer, self).set_defaults()
        self.options["label_y_axis"] = ""
        self.options["label_x_axis"] = ""

    def setup_figure(self):
        with sns.axes_style("white"):
            super(Visualizer, self).setup_figure()

    def draw(self):
        """ 
        Draw a bubble chart. 
        """
        
        def get_radius(freq):
            """
            Calculate the radius of the bubble based on the frequency.
            
            The radius is chosen so that the area of the bubble is 
            proportional to the frequency.
            """
            return math.sqrt(freq / math.pi)
        
        def my_format_coord(x, y, title):
            """
            
            """
            for (cx, cy), r, label in self.circles:
                if math.sqrt((cx - x) ** 2 + (cy - y) ** 2) <= r:
                    if title:
                        return "{} – {}".format(title, label)
                    else:
                        return label
            return ""
        
        def plot_facet(data, color):
            def r(freq):
                return math.sqrt(freq / math.pi)

            def rotate_vector((x, y), angle):
                """
                Rotate the vector (x, y) by the given angle.
                
                Returns
                -------
                (nx, ny) : tuple
                    The rotated vector.
                """
                cos_theta = math.cos(angle)
                sin_theta = math.sin(angle)
                return x*cos_theta - y*sin_theta, x*sin_theta + y*cos_theta

            def get_angle(a, b, c):
                """
                Return the angle A by using the Law of Cosines.
                
                Parameters
                ----------
                a, b, c : float
                    The length of sides a, b, c in a triangle.
                
                """
                x = (b**2 + c**2 - a**2) / (2 * b * c)
                if x > 2:
                    raise ValueError("Illegal angle")
                # Allow angles > 180 degrees:
                if x > 1:
                    return(math.acos(x-1))
                else:
                    return math.acos(x)
            
            def angle_vect((x1, y1), (x2, y2)):
                return math.atan2(x1*y2 - y1*x2, x1*x2 + y1*y2)  # atan2(y, x) or atan2(sin, cos)
            
            def get_position(i, a, n):
                """
                Return the position of the next bubble I.

                a specifies the 'anchor' bubble A (i.e. the bubble with the 
                circumference around which the algorithm attempts to place 
                the next bubble) and n gives the 'neighbor' bubble N (i.e. 
                the last bubble that has been drawn, and which should be 
                tangent to the next bubble).
                
                The position of I is chosen so that I and A are tangent, as 
                well as I and N. A and N themselves do not have to be tangent 
                (they can be, though). 

                Parameters
                ----------
                i, a, n : int 
                    The index of the next bubble (i), the anchor bubble (a),
                    and the neighboring bubble (n).
                
                """
                # get radii:
                r_a = df_freq.iloc[a]["r"]
                r_n = df_freq.iloc[n]["r"]
                r_i = df_freq.iloc[i]["r"]
                
                A = self.pos[a]
                N = self.pos[n]

                #       I
                #      / \
                #   b /   \ a
                #    /     \
                #  A ------- N
                #       c

                # get side lengths:
                l_a = r_n + r_i
                l_b = r_a + r_i
                # l_c is actually the distance between the centers of the 
                # anchor and the neighbor circles:
                l_c = math.sqrt((A[0] - N[0]) ** 2 + (A[1] - N[1]) ** 2)
                
                # the starting angle is the angle between a union vector
                # and the vector between the anchor and the neighbor:
                #start_angle = angle_vect(
                    #(1,  0),
                    #(N[0] - A[0], N[1] - A[1]))
                
                # in this special case, the call to angle_vect() can be 
                # replaced by this expression:
                start_angle = math.atan2(N[1] - A[1], N[0] - A[0])

                angle = get_angle(l_a, l_b, l_c) + start_angle
                nx, ny = rotate_vector((l_b, 0), angle)
                nx = nx + A[0]
                ny = ny + A[1]

                return (nx, ny)

            def intersecting(p, q):
                r_p = df_freq.iloc[p]["r"]
                r_q = df_freq.iloc[q]["r"]
                x_p, y_p = self.pos[p]
                x_q, y_q = self.pos[q]

                lower = (r_p - r_q)**2
                upper = (r_p + r_q)**2
                
                return lower <= (x_p - x_q) ** 2 + (y_p - y_q) ** 2 < upper - 0.01

            def draw_circle(k):
                row = df_freq.iloc[k]
                freq = row["Freq"]
                rad = row["r"]
                label = " | ".join(list(row[self._groupby]))
                c = self.options["color_palette_values"][k % self.options["color_number"]]
                
                x, y = self.pos[k]
                
                circ = plt.Circle((x, y), max(0, rad - 0.05), color=c)
                ax.add_artist(circ)
                circ.set_edgecolor("black")
                
                ax.text(x, y, "{}: {}".format(label, freq), ha="center")
                
                self.max_x = max(self.max_x, x + rad)
                self.max_y = max(self.max_y, y + rad)
                self.min_x = min(self.min_x, x - rad)
                self.min_y = min(self.min_y, y - rad)
                self.circles.append((self.pos[k], rad,  "{}: {}".format(label, freq)))

            def get_intersections(i, lower, upper):
                for x in range(lower, upper):
                    if intersecting(i, x):
                        return True
                return False

            group_columns = [x for x in data.columns if not x.startswith("coquery_invisible")]
            gp = data.fillna("").groupby(group_columns)
            df_freq = gp.agg(len).reset_index()
            columns = list(df_freq.columns)
            columns[-1] = "Freq"
            df_freq.columns = columns
            if len(self._groupby) == 2:
                df_freq.sort([self._groupby[0], "Freq"], ascending=[True, False], inplace=True)
            else:
                df_freq.sort("Freq", ascending=False, inplace=True)
            df_freq["r"] = df_freq["Freq"].map(r)
            ax = plt.gca()
            
            self.set_palette_values(len(set(df_freq[self._groupby[-1]])))
            

            self.max_x = 0
            self.max_y = 0
            self.min_x = 0
            self.min_y = 0
            ax.set_aspect(1)
            
            a = 0
            n = 1
    
            self.pos = [(None, None)] * len(df_freq.index)
            self.pos[0] = 0, 0
            
            anchor = df_freq.iloc[a]
            draw_circle(a)

            if len(df_freq) > 0:
                self.pos[1] = self.pos[0][0] + df_freq.iloc[0]["r"] + df_freq.iloc[1]["r"], self.pos[0][1]
                draw_circle(n)

            completed = 0
            for i in range(n + 1, len(df_freq.index)):
                self.pos[i] = get_position(i, a, n)
                while get_intersections(i, completed, n) and a < i:
                    a = a + 1
                    completed = a
                    try:
                        self.pos[i] = get_position(i, a, n)
                    except ValueError:
                        continue
                draw_circle(i)
                n = i
                    
            ax.set_ylim(self.min_y * 1.05, self.max_y * 1.05)
            ax.set_xlim(self.min_x * 1.05, self.max_x * 1.05)
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            
            ax.format_coord = lambda x, y: my_format_coord(x, y, ax.get_title())

        sns.despine(self.g.fig, 
                    left=True, right=True, top=True, bottom=True)
        self.g.fig.tight_layout()

        self.map_data(plot_facet)

        self.adjust_fonts(16)

        try:
            self.g.fig.tight_layout()
        except ValueError:
            # A ValueError sometimes occurs with long labels. We ignore it:
            pass