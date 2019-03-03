# text.py: a class to represent a complete IJAL interlinear text, and to transform its
# represention in ELAN xml (eaf) format, accompanied by audio, into html
#----------------------------------------------------------------------------------------------------
import re
import sys
import os
from yattag import *
import yaml
import unittest
from ijalLine import *
import importlib
pd.set_option('display.width', 1000)
import pdb
#----------------------------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------------------------------
class Text:

   xmlFilename = ''
   audioPath = ''
   grammaticalTermsFile = None
   grammaticalTerms = []
   xmlDoc = None
   htmlDoc = None
   lineCount = 0
   quiet = True

   def __init__(self, xmlFilename, audioPath, grammaticalTermsFile, tierGuideFile, quiet=True):
     self.xmlFilename = xmlFilename
     self.audioPath = audioPath
     self.grammaticalTermsFile = grammaticalTermsFile
     self.tierGuideFile = tierGuideFile
     self.validInputs()
     self.quiet = quiet
     self.xmlDoc = etree.parse(self.xmlFilename)
     self.lineCount = len(self.xmlDoc.findall("TIER/ANNOTATION/ALIGNABLE_ANNOTATION"))
     with open(tierGuideFile, 'r') as f:
        self.tierGuide = yaml.load(f)
     self

   #def discoverTiers(self):
   #  tmpDoc = etree.parse(self.xmlFilename)
   #  tierIDs = [tier.attrib["TIER_ID"] for tier in tmpDoc.findall("TIER")]
   #  return(tierIDs)

   def getTierSummary(self):
     tmpDoc = etree.parse(self.xmlFilename)
     tierIDs = [tier.attrib["TIER_ID"] for tier in tmpDoc.findall("TIER")]
     tiers = tmpDoc.findall("TIER")
     #print(self.tierGuide)
     itemList = pd.DataFrame(list(self.tierGuide.items()), columns=['key', 'value'])
     tbl = itemList[:-1].copy()
     #print(tbl)
     #tbl = pd.DataFrame(list(self.tierGuide.items()), columns=['key', 'value']).ix[0:3]
     tierValues = tbl["value"].tolist()
     tblSize = len(tierValues)
     countList = []
     for i in range(0,tblSize):
        countList.append(0)
     tbl['count'] = countList
     #tbl['count'] = [0, 0, 0, 0]
     for i in range(tblSize):
        try:
           #exception raised by None tiers
           tier = tiers[i]
           tierValue = tierValues[i]
           tierID = tier.attrib["TIER_ID"]
           count = len(tier.findall("ANNOTATION"))
           rowNumber = tbl[tbl['value']==tierValue].index.item()
           tbl.ix[rowNumber, 'count'] = count
           #print(" %30s: %4d" % (tierID, count))
        except IndexError:
           break
     self.tierTable = tbl
     return(tbl)


     return(tierIDs)

   def validInputs(self):
     assert(os.path.isfile(self.xmlFilename))
     assert(os.path.isfile(self.tierGuideFile))
        # the audioPath points to a relative directory "./audio" in which wav files are foudn
        # but without a handle on the project directory, we cannot easily test this
        # skip it for now
     if(not self.grammaticalTermsFile == None):
        assert(os.path.isfile(self.grammaticalTermsFile))
        self.grammaticalTerms = open(self.grammaticalTermsFile).read().split("\n")
        assert(len(self.grammaticalTerms) > 0)
     return(True)

   def getLineAsTable(self, lineNumber):
     x = IjalLine(self.xmlDoc, lineNumber, self.tierGuide)
     x.parse()
     return(x.getTable())

   def traverseStructure(self):
      lineNumbers = range(self.lineCount)
      for i in lineNumbers:
         x = IjalLine(self.xmlDoc, i, self.tierGuide)
         x.parse()
         tbl = x.getTable()
         print("%d: %d tiers" % (i, tbl.shape[0]))

   def getCSS(self):
      cssFilename = os.path.join(os.path.split(os.path.abspath(__file__))[0], "ijal.css")
      assert(os.path.exists(cssFilename))
      css = "<style>\n%s</style>" % open(cssFilename).read()
      return(css)

   def getJavascript(self):
      jsFilename = os.path.join(os.path.split(os.path.abspath(__file__))[0], "ijalUtils.js")
      assert(os.path.exists(jsFilename))
      jsSource = "<script>\n%s</script>" % open(jsFilename).read()
      return(jsSource)

   def toHTML(self, lineNumber=None):

     htmlDoc = Doc()

     if(lineNumber == None):
        lineNumbers = range(self.lineCount)
     else:
        lineNumbers = [lineNumber]

     htmlDoc.asis('<!DOCTYPE html>')
     with htmlDoc.tag('html', lang="en"):
        with htmlDoc.tag('head'):
            htmlDoc.asis('<meta charset="UTF-8">')
            htmlDoc.asis(self.getCSS())
            htmlDoc.asis(self.getJavascript())
            with htmlDoc.tag('body'):
                for i in lineNumbers:
                    if(not self.quiet):
                       print("line %d/%d" % (i, self.lineCount))
                    line = IjalLine(self.xmlDoc, i, self.tierGuide, self.grammaticalTerms)
                    line.parse()
                    with htmlDoc.tag("div",  klass="line-wrapper"):
                        tbl = line.getTable()
                        lineID = tbl.ix[0]['ANNOTATION_ID']
                        with htmlDoc.tag("div", klass="line-sidebar"):
                            line.htmlLeadIn(htmlDoc, self.audioPath, )
                        line.toHTML(htmlDoc)

     self.htmlDoc = htmlDoc
     self.htmlText = htmlDoc.getvalue()
     return(self.htmlText)

