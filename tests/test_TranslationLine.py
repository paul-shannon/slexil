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
    #regex = re.compile("‘\S.+\S’")   # opening curly single quote, no whitespace, any characters, no whitespace, closing curly single quote
    for case in cases:
        translationLine = TranslationLine(case)
        standardizedLine = translationLine.getStandardized()
        print(standardizedLine)
        test_begins_and_ends_with_squo(standardizedLine)
        test_extraneous_whitespace(standardizedLine)
        test_punctuation_outside_quote(standardizedLine)
        test_straight_apostrophes(standardizedLine)
        test_straight_dquo(standardizedLine)
    
#----------------------------------------------------------------------------------------------------
def test_begins_and_ends_with_squo(standardizedLine):
    '''makes sure the first and last character of the translation is a single quote'''
    
    # untested regex!
    regex = re.compile("‘\S.+\S’")   # opening curly single quote, no whitespace, any characters, no whitespace, closing curly single quote
    assert(len(regex.findall(standardizedLine)) == 1)
    
#----------------------------------------------------------------------------------------------------
def test_extraneous_whitespace(standardizedLine):
    '''checks to make sure author did not have whitespaces at either end of the translation line'''
    
    regex = re.compile("‘\s")   # opening curly single quote followed by whitespace
    assert(len(regex.findall(standardizedLine)) == 0)
    regex = re.compile("\s’")   # close curly single quote preceded by whitespace
    assert(len(regex.findall(standardizedLine)) == 0)
    
#----------------------------------------------------------------------------------------------------
def test_punctuation_outside_quote(standardizedLine):
    '''checks to make sure author did not have a punctuation mark outside a close quote'''
    
    regex = re.compile("’[\.,!?\)]’")   # punctuation preceded by rsquo
    assert(len(regex.findall(standardizedLine)) == 0)

#----------------------------------------------------------------------------------------------------
def test_straight_apostrophes(standardizedLine):
    '''checks to make sure author did not use straight apostrophes rather than squo'''
    
    regex = re.compile("‘'")   # initial straight apostrophe
    assert(len(regex.findall(standardizedLine)) == 0)
    regex = re.compile("'’")   # final straight apostrophe
    assert(len(regex.findall(standardizedLine)) == 0)
    
#----------------------------------------------------------------------------------------------------
def test_straight_dquo(standardizedLine):
    '''checks to make sure author did not use straight double quotes'''
    
    regex = re.compile('"')   # check for double quotes
    assert(len(regex.findall(standardizedLine)) == 0)
    
#----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    runTests()
