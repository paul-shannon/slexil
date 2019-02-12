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
    text = Text("../testData/aktzini/18-06-03Aktzini-GA.eaf",
                "../testData/aktzini/audioPhrases",
                grammaticalTermsFile=None,
                tierGuideFile="../testData/aktzini/tierGuide.yaml",
                quiet=False)
    return(text)

def test_constructor():

    print("--- test_constructor")
    text = createText()
    assert(text.validInputs())


def test_toHTML(display):

    print("--- test_toHTML")

    text = createText()
    text.getTable(0)

    htmlText = text.toHTML()
    filename = "aktzini.html"
    f = open(filename, "w")
    f.write(indent(htmlText))
    f.close()

    if(display):
        os.system("open %s" % filename)

if __name__ == '__main__':
    runTests()
