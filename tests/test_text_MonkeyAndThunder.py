import re
import sys
sys.path.append("..")
from text import *
import importlib
import os
import pdb
#----------------------------------------------------------------------------------------------------
pd.set_option('display.width', 1000)
#----------------------------------------------------------------------------------------------------

def runTests(display=False):

    test_constructor()
    test_toHTML(display)

def createText():
    text = Text("../testData/monkeyAndThunder/AYA1_MonkeyandThunder.eaf",
                None, #"../testData/monkeyAndThunder/audioPhrases",
                grammaticalTermsFile="../testData/monkeyAndThunder/grammaticalTerms.txt",
                tierGuideFile="../testData/monkeyAndThunder/tierGuide.yaml")

    return(text)

def test_constructor():

    print("--- test_constructor")
    text = createText()
    assert(text.validInputs())
    tbl = text.getTierSummary()
    assert(tbl.shape == (4,3))
    assert(list(tbl['key']) == ['speech', 'translation', 'morpheme', 'morphemeGloss'])
    assert(list(tbl['value']) == ['AYA', 'ENG', 'AYA2', 'GL'])
    assert(list(tbl['count']) == [41, 41, 41, 41])

def test_toHTML(display):

    print("--- test_toHTML")
    
    text = createText()
    tbl = text.getLineAsTable(0)
    
    htmlText = text.toHTML()
    filename = "monkeyAndThunder.html"
    f = open(filename, "w")
    f.write(indent(htmlText))
    f.close()
    if(display):
        os.system("open %s" % filename)

if __name__ == '__main__':
    runTests()
