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

def createText():

    text = Text("../testData/Chatino_5Line/20150717_Prayer_community_one.eaf",
                None, #"../testData/Chatino_2Line/audioPhrases",
                grammaticalTermsFile="../testData/Chatino_5Line/grammaticalTerms.txt",
                tierGuideFile="../testData/Chatino_5Line/tierGuide.yaml",
                quiet=True)
    return(text)

def runTests(display=False):

    test_constructor()
    test_toHTML(display)

def test_constructor():

    print("--- test_constructor")

    text = createText()
    assert(text.validInputs())
    tbl = text.getTierSummary()
    assert(tbl.shape == (5,3))
    assert(list(tbl['key']) == ['speech', 'translation', 'morpheme', 'morphemeGloss','translation2'])
    assert(list(tbl['value']) == ['SZC-Chatino', 'English Translation-cp-cp', 'Tokenization-cp', 'POS-cp','SZC-presandhi'])
    assert(list(tbl['count']) == [9, 9, 111, 111, 9])

def test_toHTML(display):

    print("--- test_toHTML")

    text = createText()
    tbl = text.getLineAsTable(0)

    htmlText = text.toHTML()
    filename = "prayer5.html"
    f = open(filename, "w")
    f.write(indent(htmlText))
    f.close()

    if(display):
        os.system("open %s" % filename)

if __name__ == '__main__':
    runTests()
