#!usr/bin/env python
"""c
from oscheck import *
import wx
"""

import os
import sys
import pathlib

# path = "{}{}".format(os.getcwd(), "/AppsSDS")
# print (type(path))
path = pathlib.Path.cwd() / 'AppsSDS'
# print (type(path))

sys.path.append(str(path))
sys.path
print (sys.path)
# os.getcwd()
# cd = "{}{}".format(os.getcwd(), "/AppsSDS")
cd = pathlib.Path.cwd() / "AppsSDS"
os.chdir(str(cd))

import AppsSDS.main 
#import run
