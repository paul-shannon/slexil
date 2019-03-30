# -*- coding: utf-8 -*-
#
# MorphemeGloss.py: a class to capture, and render into HTML, the morphemes of the spoken text, using
# standard grammatical terms
#
# see https://en.wikipedia.org/wiki/List_of_glossing_abbreviations
# from https://en.wikipedia.org/wiki/Interlinear_gloss#Structure
#
#  grammatical terms are commonly abbreviated and printed in SMALL CAPITALS to keep them distinct
#  from translations,  especially when they are frequent or important for analysis.
#
#  for IJAL style requirements of interlinear glosses, see http://www.americanlinguistics.org/?page_id=93
#  also see the Leipzig Glossing Rules: https://www.eva.mpg.de/lingua/resources/glossing-rules.php
#
# in interlinear morphological glosses, punctuation separating the glosses:
#
#        .  equivalent to a space (separating words) in the morpheme line
#        _  when a source language word corresponds to a phrase in the glossing language
#        =  separates clitics (a morpheme with syntactic characteristics of a word, but which
#           depends phonologically upon another word or phrase)
#        ~  reduplication
#        -- and more...
#
# david beck (email 12 aug 2018):
#
#    I usually leave the numbers in the abbreviations in normal font size, as well as punctuation
#    marks like the colon and the period (which are reserved characters for interlinear glossing). The
#    morpheme delimiters are also in regular sized type, and in the original GUI there was a field
#    where the user could list the symbols in use. – (n-dash), =, and • are the most common, but there
#    are others people are likely to use such as ~ (for reduplication), ^ (to add a floating tone to a
#    morph), and < > (for infixes). Another thing that we haven’t come up against yet is that there are
#    sometimes subscripts, most commonly used to label something as belonging to a particular class.
#------------------------------------------------------------------------------------------------------------------------
import re
from pprint import pprint
from yattag import *
import pdb


#------------------------------------------------------------------------------------------------------------------------
class MorphemeGloss:

   rawText = ""
   grammaticalTerms = []
   delimiters = "([=•\d\-\.–~])"   # more to come: ^ < >, subscripts recognition?

   def __init__(self, rawText, grammaticalTerms):
     self.rawText = rawText
     self.grammaticalTerms = grammaticalTerms#.extend(['1','2','3'])

   def show(self):
      pprint(vars(self))

   def parse(self):
      """ identify terms, delimiters, plain words """
      self.parts = _extractParts(self.delimiters, self.rawText)

   def getParts(self):
      return(self.parts)

   def toHTML(self, htmlDoc):
      """ iterate over the parts list, identify each grammaticalTerm
          wrap each of those in a <span class='grammaticalTerm'> tag
      """
      with htmlDoc.tag("div", klass="morpheme-gloss"):
         for part in self.parts:
            if(self.grammaticalTerms) and (part in self.grammaticalTerms):
               with htmlDoc.tag("span", klass="grammatical-term"):
                  htmlDoc.asis(part)
            else:
               htmlDoc.text(part)


#------------------------------------------------------------------------------------------------------------------------
# non-class functions
#------------------------------------------------------------------------------------------------------------------------
def _extractParts(delimiters, string):
   parts = re.split(delimiters, string)
   parts_noEmptyStrings = [part for part in parts if part != ""]
   return(parts_noEmptyStrings)
