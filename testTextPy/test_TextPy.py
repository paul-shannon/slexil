import re
import sys
sys.path.append("..")
from text import *
import importlib
import os
import pdb
from ijalLine import *
from errors import *
#----------------------------------------------------------------------------------------------------
pd.set_option('display.width', 1000)
#----------------------------------------------------------------------------------------------------
def runTests(display=True):
    #test_MonkeyAndThunder(display)
    #test_MonkeyAndThunderTabbing(display)
    #test_MonkeyAndThunderNoPacking(display)
    #test_Fishwoman(display)
    #test_FishwomanNoPacking(display)
    #test_Merchant(display)
    test_Jaguar(display)
    
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
def test_Merchant(display):

    print("--- test_Merchant")

    text = Text("../testTextPyData/JIT0006_ori/JIT0006_ori.eaf",
                "../testTextPyData/JIT0006_ori/Audio",
                "../testTextPyData/JIT0006_ori/abbreviations.txt",
                "../testTextPyData/JIT0006_ori/tierGuide.yaml")
     
    #IjalLine.getTable(1)

    htmlText = text.toHTML()
    if(display):
       filename = "test_Merchant.html"
       f = open(filename, "w")
       f.write(indent(htmlText))
       f.close()
       os.system("open %s" % filename)


#----------------------------------------------------------------------------------------------------
def test_Jaguar(display):

    print("--- test_Jaguar")

    text = Text("../testTextPyData/Ocotepec_TheOpposumAndTheJaguar/OCO2_JaguarAndOpossum.eaf",
                "../testTextPyData/Ocotepec_TheOpposumAndTheJaguar/Audio",
                "../testTextPyData/Ocotepec_TheOpposumAndTheJaguar/abbreviations.txt",
                "../testTextPyData/Ocotepec_TheOpposumAndTheJaguar/tierGuide.yaml")
     
    #IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if(display):
            filename = "test_Jaguar.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print("There are more morphs than glosses in line %s." %e.lineNumber)
    except TooManyGlossesError as e:
        print("There are more glosses than morphs in line %s." %e.lineNumber)



#----------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    runTests()
