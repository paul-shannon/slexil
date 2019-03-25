# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------------------------
# test_TranslationLine.pyt
#----------------------------------------------------------------------------------------------------
import sys
sys.path.append("..")
from translationLine import *
import re
#----------------------------------------------------------------------------------------------------
def runTests():
    test_standardizeTranslationLine()
    
#----------------------------------------------------------------------------------------------------
def test_standardizeTranslationLine():
    """
      ensure we can handle all proper and improper translation lines
      the eaf xml schema only requires that they be character strings
      we require that each line
        - begins with a left curly single quote
        - ends with a right curly single quote
        - has no leading or trailing whitespace
      we use the intentionally flawed text "Chatino_FaultyAuthorExamples" to collect all
      the improper translation lines we imagine, or encounter over time, to ensure
      that we can render them into our proper form 
    """

    from xml.etree import ElementTree as etree
    filename = "../testData/Chatino_FaultyAuthorExamples/20150717_Prayer_community_one.eaf"
    doc = etree.parse(filename)
    pattern = "TIER[@TIER_ID='English Translation-cp-cp']/ANNOTATION/REF_ANNOTATION/ANNOTATION_VALUE"
    childElements = doc.findall(pattern)
    assert(len(childElements) >= 9)
    cases = [element.text for element in childElements]
       # untested regex!
    regex = re.compile("‘\S.+\S’")   # opening curly single quote, no whitespace, any characters, no whitespace, closing curly single quote
    for case in cases:
       translationLine = TranslationLine(case)
       standardizedLine = translationLine.getStandardized()
       assert(len(regex.findall(standardizedLine)) == 1)
    
#----------------------------------------------------------------------------------------------------
