import re
import sys
sys.path.append("..")
from text import *
import importlib
import os
import pdb
from ijalLine import *
#----------------------------------------------------------------------------------------------------
pd.set_option('display.width', 1000)
#----------------------------------------------------------------------------------------------------
def runTests(display=True):
    test_MonkeyAndThunder(display)
    #test_MonkeyAndThunderTabbing(display)
    test_MonkeyAndThunderNoPacking(display)
    test_Fishwoman(display)
    test_FishwomanNoPacking(display)
    
#----------------------------------------------------------------------------------------------------
def test_MonkeyAndThunder(display):

    print("--- test_MonkeyAndThunder")

    text = Text("../testTextPyData/AYA1_MonkeyandThunder/AYA1_MonkeyandThunder.eaf",
                "../testTextPyData/AYA1_MonkeyandThunder/Audio",
                "../testTextPyData/AYA1_MonkeyandThunder/abbreviations.txt",
                "../testTextPyData/AYA1_MonkeyandThunder/tierGuide.yaml")
     
    #IjalLine.getTable(1)

    htmlText = text.toHTML()
    if(display):
       filename = "monkeyAndThunderTest.html"
       f = open(filename, "w")
       f.write(indent(htmlText))
       f.close()
       os.system("open %s" % filename)


#----------------------------------------------------------------------------------------------------
def test_MonkeyAndThunderTabbing(display):

    print("--- test_MonkeyAndThunder_tiers")

    text = Text("../testTextPyData/AYA1_MonkeyandThunder/AYA1_MonkeyandThunder.eaf",
                "../testTextPyData/AYA1_MonkeyandThunder/Audio",
                "../testTextPyData/AYA1_MonkeyandThunder/abbreviations.txt",
                "../testTextPyData/AYA1_MonkeyandThunder/tierGuideTier.yaml")
     
    #IjalLine.getTable(1)

    htmlText = text.toHTML()
    if(display):
       filename = "monkeyAndThunderTest2.html"
       f = open(filename, "w")
       f.write(indent(htmlText))
       f.close()
       os.system("open %s" % filename)


#----------------------------------------------------------------------------------------------------
def test_MonkeyAndThunderNoPacking(display):

    print("--- test_MonkeyAndThunder_NoPacking")

    text = Text("../testTextPyData/AYA1_MonkeyandThunder/AYA1_MonkeyandThunder.eaf",
                "../testTextPyData/AYA1_MonkeyandThunder/Audio",
                "../testTextPyData/AYA1_MonkeyandThunder/abbreviations.txt",
                "../testTextPyData/AYA1_MonkeyandThunder/tierGuideNone.yaml")
     
    #IjalLine.getTable(1)

    htmlText = text.toHTML()
    if(display):
       filename = "monkeyAndThunderTest3.html"
       f = open(filename, "w")
       f.write(indent(htmlText))
       f.close()
       os.system("open %s" % filename)


#----------------------------------------------------------------------------------------------------
def test_Fishwoman(display):

    print("--- test_Fishwoman")

    text = Text("../testTextPyData/2_AYA2_FishWoman/2_AYA2_FishWoman.eaf",
                "../testTextPyData/2_AYA2_FishWoman/Audio",
                "../testTextPyData/2_AYA2_FishWoman/abbreviations.txt",
                "../testTextPyData/2_AYA2_FishWoman/tierGuide.yaml")
     
    #IjalLine.getTable(1)

    htmlText = text.toHTML()
    if(display):
       filename = "test_Fishwoman.html"
       f = open(filename, "w")
       f.write(indent(htmlText))
       f.close()
       os.system("open %s" % filename)


#----------------------------------------------------------------------------------------------------
def test_FishwomanNoPacking(display):

    print("--- test_Fishwoman_NoPacking")

    text = Text("../testTextPyData/2_AYA2_FishWoman/2_AYA2_FishWoman.eaf",
                "../testTextPyData/2_AYA2_FishWoman/Audio",
                "../testTextPyData/2_AYA2_FishWoman/abbreviations.txt",
                "../testTextPyData/2_AYA2_FishWoman/tierGuideNone.yaml")
     
    #IjalLine.getTable(1)

    htmlText = text.toHTML()
    if(display):
       filename = "test_FishwomanNoPack.html"
       f = open(filename, "w")
       f.write(indent(htmlText))
       f.close()
       os.system("open %s" % filename)


#----------------------------------------------------------------------------------------------------
def test_prayer(display):

    print("--- test_prayer")

    text = Text("../testData/prayer/20150717_Prayer_community_one.eaf",
                "../testData/prayer/audioPhrases",
                grammaticalTermsFile=None,
                quiet=False)

    text.getTable(0)

    htmlText = text.toHTML(0)

    if(display):
       filename = "prayer.html"
       f = open(filename, "w")
       f.write(indent(htmlText))
       f.close()
       os.system("open %s" % filename)


#----------------------------------------------------------------------------------------------------
def test_aktzini(display):

    print("--- test_aktzini")

    text = Text("../testData/aktzini/18-06-03Aktzini-GA.eaf",
                "../testData/aktzini/audioPhrases",
                grammaticalTermsFile=None,
                quiet=False)

    text.getTable(1)

    htmlText = text.toHTML()
    if(display):
       filename = "aktzini.html"
       f = open(filename, "w")
       f.write(indent(htmlText))
       f.close()
       os.system("open %s" % filename)


#----------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    runTests()
