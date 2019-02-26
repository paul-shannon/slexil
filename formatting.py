# -*- coding: utf-8 -*-
#
# formatting.py: methods to normalize and standardize the formats of the different
# line components of the interlinear glosses


def cleanUpInterlinears(string):
   string = removeWhitespace(string)
   string = string.replace("-","–")
   return string

def removeWhitespace(string):
    string = string.replace(" ","")
    return string
