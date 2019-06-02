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
from decimal import Decimal
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

   def __init__(self, xmlFilename, soundFileName, grammaticalTermsFile, tierGuideFile, startStopTable, quiet=True):
     self.xmlFilename = xmlFilename
     self.soundFileName = soundFileName
     self.audioPath = "audio"
     self.grammaticalTermsFile = grammaticalTermsFile
     self.tierGuideFile = tierGuideFile
     self.startStopTable = self.makeStartStopTable(startStopTable)
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

   def makeStartStopTable(self, startStopTable):
     annotations = startStopTable.split('\n')
     self.audioTable = []
     startStopTimes = "window.annotations=["
     for i,annotation in enumerate(annotations):
          if i == 0:
               continue
          elif len(annotation) == 0:
               continue
          values = annotation.split(',')
          id = values[0]
          #start = int(values[1])/1000
          start = values[1]
          end = values[2]
          entry = "{ 'id' : '%s', 'start' : '%s', 'end' : '%s'}," %(id,start,end)
          startStopTimes += entry
          self.audioTable.append(annotation)
     startStopTimes =startStopTimes[:-1] + "]"
     return(startStopTimes)

   def validInputs(self):
     try:
          assert(os.path.isfile(self.xmlFilename))
     except AssertionError as e:
          raise Exception(self.xmlFilename) from e
     try:
          assert(os.path.isfile(self.tierGuideFile))
     except AssertionError as e:
          raise Exception(tierGuideFile)from e
        # the audioPath points to a relative directory "./audio" in which wav files are found
        # but without a handle on the project directory, we cannot easily test this
        # skip it for now
     if(not self.grammaticalTermsFile == None):
          print("The file coming from webapp is: %s" % self.grammaticalTermsFile)
          #grammaticalTermsFile = os.path.join(self.projectDirectory,grammaticalTermsFile)
          try:
               assert(os.path.isfile(self.grammaticalTermsFile))
          except AssertionError as e:
               raise Exception(self.grammaticalTermsFile) from e
          grammaticalTerms = open(self.grammaticalTermsFile).read()#.split("\n")
          assert(len(grammaticalTerms) > 0)
          self.grammaticalTerms = _makeAbbreviationListLowerCase(grammaticalTerms)
     return(True)

   def getLineAsTable(self, lineNumber):
     audioData = self.audioTable.split('\n')[int(lineNumber)]
     print("audio data: %s" %audioData)
     x = IjalLine(self.xmlDoc, lineNumber, self.tierGuide, audioData)
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
      cssFilename = "ijal.css"
      #assert(os.path.exists(cssFilename))
      #print(cssFilename)
      css = '<link rel = "stylesheet" type = "text/css" href = "%s" />' % cssFilename
#       css = "<style>\n%s</style>" % open(cssFilename).read()
      return(css)

   def getJQuery(self):
      scriptTag = '<script src="jquery-3.3.1.min.js"></script>\n'
      return(scriptTag)

   def getJavascript(self):
      jsSource = '<script src="ijalUtils.js"></script>\n'
      jsSource += '<script type="text/javascript">%s</script>\n' %self.startStopTable
      return(jsSource)

   def getPlayer(self):
      soundFile = os.path.join(self.audioPath,os.path.basename(self.soundFileName))
      playerDiv = '<audio class="player" id="audioplayer" src="%s" controls></audio></audio>' %soundFile
      return playerDiv

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
            htmlDoc.asis(self.getJQuery())
            htmlDoc.asis(self.getCSS())
            with htmlDoc.tag('body'):
                for i in lineNumbers:
                    if(not self.quiet):
                       print("line %d/%d" % (i, self.lineCount))
                    line = IjalLine(self.xmlDoc, i, self.tierGuide,self.audioTable[i], self.grammaticalTerms)
                    line.parse()
                    with htmlDoc.tag("div",  klass="line-wrapper", id=i+1):
                        tbl = line.getTable()
                        lineID = tbl.ix[0]['ANNOTATION_ID']
                        with htmlDoc.tag("div", klass="line-sidebar"):
                            line.htmlLeadIn(htmlDoc, self.audioPath, )
                        line.toHTML(htmlDoc)
                htmlDoc.asis(self.getPlayer())
                htmlDoc.asis(self.getJavascript())
     self.htmlDoc = htmlDoc
     self.htmlText = htmlDoc.getvalue()
     return(self.htmlText)

#---------------------------------------------------------
def _makeAbbreviationListLowerCase(grammaticalTerms):
   ''' ensures grammatical terms in user list are lower case '''
   exceptions  = ["A","S","O","P"]
   newTerms = []
   grammaticalTerms = grammaticalTerms.replace(".","\n")
   grammaticalTerms = grammaticalTerms.replace("<sub>","\n")
   grammaticalTerms = grammaticalTerms.replace("</sub>","\n")
   grammaticalTerms = grammaticalTerms.replace("<sup>","\n")
   grammaticalTerms = grammaticalTerms.replace("</sup>","\n")
   grammaticalTerms = grammaticalTerms.replace("<sub>","\n")
   grammaticalTerms = grammaticalTerms.replace("\n\n","\n")
   terms = grammaticalTerms.split("\n")
   #print()terms
   '''first run through needs to deal with super/subscripts'''
   for term in terms:
      term = term.strip()    
      if term in exceptions:
         newTerms.append(term)
      elif term.isupper():
         newTerm = term.lower()
         newTerms.append(newTerm)
      else:
         newTerms.append(term)
   #print(newTerms)
   uniqueTerms = list(set(newTerms))
   #print(uniqueTerms)
   return(uniqueTerms)

