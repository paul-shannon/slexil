# -*- coding: utf-8 -*-
#
# GrammaticalTerms: a class to handle formatting of abbreviations used
# in interlinearizations, specifically to standardize all abbreviations as
# lowercase, to be rendered as small caps by the CSS style .grammatical-term
# and to ensure hyphens are replaced by n-dashes
#----------------------------------------------------------------------------------------------------
import re
from pprint import pprint
from yattag import *
import pdb


#------------------------------------------------------------------------------------------------------------------------
class GrammaticalTerms:

    rawText = ""
    grammaticalTerms = []
    delimiters = "(<sub>|</sub>|<sup>|</sup>|[=•\-\.–~\^+<>])"

    def __init__(self, rawText, grammaticalTerms):
        self.rawText = self.replaceHyphensWithNDashes(rawText)
        self.grammaticalTerms = self.makeAbbreviationsLowerCase(grammaticalTerms)

    def show(self):
        pprint(vars(self))

    def parse(self):
        """ identify terms, delimiters, plain words """
        parts = _extractParts(self.delimiters, self.rawText)
        self.addNumberedAbbreviations(parts) #extends self.grammaticalTerms 
        self.parts = self.makePartsLowerCase(parts)

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

    def makeAbbreviationsLowerCase(self,terms):
        ''' ensures grammatical terms are lower case '''
        #misses things inside sub and sup tags
        exceptions  = ["A","S","O","P"]
        newTerms = []
        for term in terms:
            if term in exceptions:
                newTerms.append(term)
            elif term.isupper():
                newTerm = term.lower()
                newTerms.append(newTerm)
            else:
                newTerms.append(term)
        return newTerms
            
    def addNumberedAbbreviations(self, parts):
        ''' adds number + abbreviation combinations used
            in the text (e.g., 1sg, 3obj) to self.grammaticalTerms
            and ensures these are in the correct case
        ''' 
        newTerms = [part for part in parts if any(i.isdigit() for i in part)]
        for term in newTerms:
            if term[0].isdigit() and term[1:].lower() in self.grammaticalTerms:
                self.grammaticalTerms.append(term.lower())
            elif term[-1].isdigit() and term[:-1].lower() in self.grammaticalTerms:
                self.grammaticalTerms.append(term.lower())
            elif not term in self.grammaticalTerms:
                self.grammaticalTerms.append(term)

    def makePartsLowerCase(self, parts):
        ''' makes sure the grammatical glosses are in lower case
            but leaves lexical glosses and exceptions alone
        ''' 
        grammaticalTerms = self.grammaticalTerms
        newParts = []
        for part in parts:
            if part.lower() in grammaticalTerms:
                newParts.append(part.lower())
            else:
                newParts.append(part)          
        return(newParts)

    def replaceHyphensWithNDashes(self, text):
        ''' replace hyphens with n-dashes
        ''' 
        text = text.replace('-','–')          
        return(text)

#------------------------------------------------------------------------------------------------------------------------
# non-class functions
#------------------------------------------------------------------------------------------------------------------------
def _extractParts(delimiters, string):
   parts = re.split(delimiters, string)
   parts_noEmptyStrings = [part for part in parts if part != ""]
   return(parts_noEmptyStrings)


