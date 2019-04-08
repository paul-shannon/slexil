# -*- coding: utf-8 -*-
#
# GrammaticalTerms: a class to handle formatting of abbreviations used
# in interlinearizations, specifically to standardize all abbreviations as
# lowercase, to be rendered as small caps by the CSS style .grammatical-term
# 
#----------------------------------------------------------------------------------------------------
import re
from pprint import pprint
from yattag import *
import pdb


#------------------------------------------------------------------------------------------------------------------------
class GrammaticalTerms:

    def __init__(self, part, grammaticalTerms):
        if part.lower() in grammaticalTerms:
            self.text = part.lower()
        else:
            self.text = part

    def getTerm(self):          
        return(self.text)
