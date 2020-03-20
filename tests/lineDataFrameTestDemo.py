import re
import sys
sys.path.append("..")
from ijalLine import *
import importlib
import os
import pdb
import yaml
import pandas as pd


filename = "../testData/lokono/LOKONO_IJAL_2.eaf"
doc = etree.parse(filename)
tierGuideFile = "../testData/lokono/tierGuide.yaml"
with open(tierGuideFile, 'r') as f:
   tierGuide = yaml.safe_load(f)

x3 = IjalLine(doc, 3, tierGuide)
x3.parse()
tbl = x3.getTable()
