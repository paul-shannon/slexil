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
    text = Text("../testData/lokono/LOKONO_IJAL_2.eaf",
                audioPath=None,
                grammaticalTermsFile=None,
                tierGuideFile="../testData/lokono/tierGuide.yaml")
    return(text)

def test_constructor():

    print("--- test_constructor")
    text = createText()
    assert(text.validInputs())
    tbl = text.getTierSummary()
    assert(tbl.shape == (4,3))
    assert(list(tbl['key']) == ['speech', 'translation', 'morpheme', 'morphemeGloss'])
    assert(list(tbl['value']) == ['Orthographic represntation', 'English translation', 'morpheme', 'gloss'])
    assert(list(tbl['count']) == [344, 344, 1857, 1857])

def test_traverseStructure():

    print("--- test_traverseStructure")
    text = createText()
    text.traverseStructure()

def exploreMapping():

    text = createText()
    tbl = text.getLineAsTable(0)


def test_toHTML(display):

    print("--- test_toHTML")

    text = createText()
    text.getLineAsTable(0)

    htmlText = text.toHTML()
    filename = "lokono.html"
    f = open(filename, "w")
    f.write(indent(htmlText))
    f.close()

    if(display):
        os.system("open %s" % filename)

if __name__ == '__main__':
    runTests()
