# -*- coding: utf-8 -*-
#
# TranslationLine: a class to standardize and enforce the IJAL conventions for translation lines:
#    - begins with a left curly single quote
#    - ends with a right curly single quote
#    - has no leading or trailing whitespace
#  are embedded straight single quotes (') permitted?
#  are embedded double quotes permitted?
#----------------------------------------------------------------------------------------------------
import re

class TranslationLine:

   rawText = ""
   cleanText = ""

   def __init__(self, rawText):
      self.rawText = rawText.strip()
      self.cleanText = self.standardize()

   def standardize(self):
      string = self.rawText
      if string[0] == "‘":
         string = string[1:]
      if string[-1] == "’":
         string = string[:-1]
      # check for apostrophes instead of squo
      if string[0] == "'":
         string = string[1:]
      if string[-1] == "'":
         string = string[:-1]
      # check for punctuation following rsquo
      regex = re.compile("’[\.,!?\)]$")
      if regex.search(string):
         punctuation = string[-1]
         string = string[:-2].strip() + punctuation
      # replace straight double quotes with smart quotes
      if '"' in string:
         string = re.sub('^"','“',string)
         string = re.sub('\s"',' “',string)
         string = string.replace('"','”')
      string = "‘" + string.strip() + "’"
      return string

   def getRaw(self):
      return self.rawText

   def getStandardized(self):
      return self.cleanText

  

