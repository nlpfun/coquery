# -*- coding: utf-8 -*-

"""
__init__.py is part of Coquery.

Copyright (c) 2016 Gero Kunter (gero.kunter@coquery.org)

Coquery is released under the terms of the GNU General Public License (v3).
For details, see the file LICENSE that you should have received along 
with Coquery. If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import os

base_path, _ = os.path.split(os.path.realpath(__file__))
sys.path.append(base_path)
sys.path.append(os.path.join(base_path, "gui"))

__version__ = "0.9"
NAME = "Coquery"
DATE = "2016"

