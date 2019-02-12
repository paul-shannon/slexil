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

def runTests():

    test_constructor()
    test_toHTML(display=False)

def createText():
    text = Text("../testData/plumedSerpent/TRS_Plumed_Serpent_Legend_05-15-2017.eaf",
                None, #"../testData/plumedSerpent/audioPhrases",
                grammaticalTermsFile=None,
                tierGuideFile="../testData/plumedSerpent/tierGuide.yaml",
                quiet=False)
    return(text)

def test_constructor():

    print("--- test_constructor")
    text = createText()
    assert(text.validInputs())
    tbl = text.getTierSummary()
    assert(tbl.shape == (4,3))
    assert(list(tbl['key']) == ['speech', 'translation', 'morpheme', 'morphemeGloss'])
    assert(list(tbl['value']) == ['TRS-Ortho', 'Free Translation', 'Tokenization-cp', 'Tokenization-Gloss-cp'])
    assert(list(tbl['count']) == [15, 15, 15, 141])

def test_toHTML(display):

    print("--- test_toHTML")
    text = createText()    

    tbl = text.getLineAsTable(0)
    assert(tbl.shape == (10, 14))

    htmlText = text.toHTML()
    filename = "plumedSerpent.html"
    f = open(filename, "w")
    f.write(indent(htmlText))
    f.close()

    if(display):
        os.system("open %s" % filename)

if __name__ == '__main__':
    runTests()
