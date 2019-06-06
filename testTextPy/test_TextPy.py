import re
import sys
sys.path.append("..")
from text import *
import importlib
import os
import pdb
from ijalLine import *
from errors import *
import logging
#----------------------------------------------------------------------------------------------------
pd.set_option('display.width', 1000)
#----------------------------------------------------------------------------------------------------
def runTests(display=False):
#     test_MonkeyAndThunder(display)
#     test_MonkeyAndThunderTabbing(display)
#     test_MonkeyAndThunderNoPacking(display)
#     test_Fishwoman(display)
#     test_FishwomanNoPacking(display)
    test_Merchant(display)
#     test_Jaguar(display)
#     test_Riverwoman(display)
#     test_SanMiguel(display)
#     test_Caterpillar(display)
#     test_Lazy(display)
#     test_Imp(display)
#     test_Prayer(True)
#     test_Inferno(True)
#     test_MonkeyAndThunder(True)
#     test_Aymara(True)

    
#----------------------------------------------------------------------------------------------------
def test_Aymara(display):

    print("--- test_Aymara")
    
#     projectDirectory = "../testTextPyData/Aymara"
#     logging.basicConfig(filename=os.path.join(projectDirectory,"ERRORS.log"), level = logging.WARNING,format="%(levelname)s %(message)s")
    with open("../testTextPyData/Aymara/startStopTimes.txt","r") as tf:
    	times = tf.read()
    text = Text("../testTextPyData/Aymara/Aymara-final.eaf", "../testTextPyData/Aymara/Audio/Final-Edwin-historia-del-oso_no_anotado__ch1.wav","../testTextPyData/Aymara/List of abbreviations.txt", "../testTextPyData/Aymara/tierGuide.yaml", times, "../testTextPyData/Aymara")
     
    #IjalLine.getTable(1)

    htmlText = text.toHTML()
    if(display):
       filename = "../testTextPyData/Aymara/Aymara.html"
       f = open(filename, "w")
       f.write(indent(htmlText))
       f.close()
       os.system("open %s" % filename)

#----------------------------------------------------------------------------------------------------
def test_Inferno(display):

    print("--- test_Inferno")

    with open("../explorations/playAudioInSequence/Inferno/startStopTimes.txt","r") as tf:
    	times = tf.read()
    text = Text("../explorations/playAudioInSequence/Inferno/inferno-threeLines.eaf",
                "../explorations/playAudioInSequence/Inferno/Audio/inferno-threeLines.wav",
                "../explorations/playAudioInSequence/Inferno/abbreviations.txt",
                "../explorations/playAudioInSequence/Inferno/tierGuide.yaml",
                times)
     
    #IjalLine.getTable(1)

    htmlText = text.toHTML()
    if(display):
       filename = "../explorations/playAudioInSequence/Inferno/inferno-threeLines.html"
       f = open(filename, "w")
       f.write(indent(htmlText))
       f.close()
       os.system("open %s" % filename)



#----------------------------------------------------------------------------------------------------
def test_MonkeyAndThunder(display):

    print("--- test_MonkeyAndThunder")
    with open("../explorations/playAudioInSequence/Monkey/startStopTimes.txt","r") as tf:
    	times = tf.read()
    text = Text("../explorations/playAudioInSequence/Monkey/AYA1_MonkeyandThunder.eaf",
                "../explorations/playAudioInSequence/Monkey/Audio/AYA1_MonkeyandThunder-1.wav",
                "../explorations/playAudioInSequence/Monkey/abbreviations.txt",
                "../explorations/playAudioInSequence/Monkey/tierGuide.yaml",
                times)
     
    #IjalLine.getTable(1)

    htmlText = text.toHTML()
    if(display):
       filename = "../explorations/playAudioInSequence/Monkey/monkeyAndThunderTest.html"
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
    with open("../testTextPyData/Aymara/startStopTimes.txt","r") as tf:
    	times = tf.read()
    text = Text("../testTextPyData/2_AYA2_FishWoman/2_AYA2_FishWoman.eaf",
                "../testTextPyData/2_AYA2_FishWoman/2_AYA2_FishWoman",
                "../testTextPyData/2_AYA2_FishWoman/abbreviations.txt",
                "../testTextPyData/2_AYA2_FishWoman/tierGuide.yaml",
                times,
                "../testTextPyData/2_AYA2_FishWoman")
     
    #IjalLine.getTable(1)

    htmlText = text.toHTML()
    if(display):
       filename = "../testTextPyData/2_AYA2_FishWoman/test_Fishwoman.html"
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
    with open("../testTextPyData/JIT0006_ori/startStopTimes.txt","r") as tf:
    	times = tf.read()
    text = Text("../testTextPyData/JIT0006_ori/JIT0006_ori.eaf",
                "../testTextPyData/JIT0006_ori/JIT0006.WAV",
                "../testTextPyData/JIT0006_ori/abbreviations.txt",
                "../testTextPyData/JIT0006_ori/tierGuide.yaml",
                times,
                "../testTextPyData/JIT0006_ori")
     
    #IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if(display):
            filename = "test_Merchant.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print("EAF error: There are more morphs (%d) than glosses (%d) in line %s." %(e.morphs,e.glosses,e.lineNumber))
    except TooManyGlossesError as e:
        print("EAF error: There are more glosses (%d) than morphs (%d) in line %s." %(e.glosses,e.morphs,e.lineNumber))
    except EmptyTiersError as e:
        print("EAF error: There are empty tiers or incomplete glosses after line %s" %e.lineNumber)



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
        print("EAF error: There are more morphs (%d) than glosses (%d) in line %s." %(e.morphs,e.glosses,e.lineNumber))
    except TooManyGlossesError as e:
        print("EAF error: There are more glosses (%d) than morphs (%d) in line %s." %(e.glosses,e.morphs,e.lineNumber))
    except EmptyTiersError as e:
        print("EAF error: There are empty tiers or incomplete glosses after line %s" %e.lineNumber)



#----------------------------------------------------------------------------------------------------
def test_Riverwoman(display):

    print("--- test_Riverwoman")

    text = Text("../testTextPyData/Ocotepec_Riverwoman/2015-01-23_NÑwayomo.eaf",
                "../testTextPyData/Ocotepec_Riverwoman/Audio",
                "../testTextPyData/Ocotepec_Riverwoman/abbreviations.txt",
                "../testTextPyData/Ocotepec_Riverwoman/tierGuide.yaml")
     
    #IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if(display):
            filename = "test_Riverwoman.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print("EAF error: There are more morphs (%d) than glosses (%d) in line %s." %(e.morphs,e.glosses,e.lineNumber))
    except TooManyGlossesError as e:
        print("EAF error: There are more glosses (%d) than morphs (%d) in line %s." %(e.glosses,e.morphs,e.lineNumber))
    except EmptyTiersError as e:
        print("EAF error: There are empty tiers or incomplete glosses after line %s" %e.lineNumber)


#----------------------------------------------------------------------------------------------------
def test_SanMiguel(display):

    print("--- test_SanMiguel")

    text = Text("../testTextPyData/SanMiguelChimalapaZoque/SanMiguelChimalapaZoque.eaf",
                "../testTextPyData/SanMiguelChimalapaZoque/Audio",
                "../testTextPyData/SanMiguelChimalapaZoque/abbreviations.txt",
                "../testTextPyData/SanMiguelChimalapaZoque/tierGuide.yaml")
     
    #IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if(display):
            filename = "test_SanMiguel.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print("EAF error: There are more morphs (%d) than glosses (%d) in line %s." %(e.morphs,e.glosses,e.lineNumber))
    except TooManyGlossesError as e:
        print("EAF error: There are more glosses (%d) than morphs (%d) in line %s." %(e.glosses,e.morphs,e.lineNumber))
    except EmptyTiersError as e:
    	print("EAF error: There are empty tiers or incomplete glosses after line %s" %e.lineNumber)

#----------------------------------------------------------------------------------------------------
def test_Caterpillar(display):

    print("--- test_Caterpillar")

    text = Text("../testTextPyData/SOT_Caterpillar/SOT_TheCaterpillar_Morph.eaf",
                "../testTextPyData/SOT_Caterpillar/Audio",
                "../testTextPyData/SOT_Caterpillar/abbreviations.txt",
                "../testTextPyData/SOT_Caterpillar/tierGuide.yaml")
     
    #IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if(display):
            filename = "test_Caterpillar.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print("EAF error: There are more morphs (%d) than glosses (%d) in line %s." %(e.morphs,e.glosses,e.lineNumber))
    except TooManyGlossesError as e:
        print("EAF error: There are more glosses (%d) than morphs (%d) in line %s." %(e.glosses,e.morphs,e.lineNumber))
    except EmptyTiersError as e:
    	print("EAF error: There are empty tiers or incomplete glosses after line %s" %e.lineNumber)

#----------------------------------------------------------------------------------------------------
def test_Lazy(display):

    print("--- test_Lazy")

    text = Text("../testTextPyData/TEX_Lazy/TEX_Lazy.eaf",
                "../testTextPyData/TEX_Lazy/Audio",
                "../testTextPyData/TEX_Lazy/abbreviations.txt",
                "../testTextPyData/TEX_Lazy/tierGuide.yaml")
     
    #IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if(display):
            filename = "test_Lazy.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print("EAF error: There are more morphs (%d) than glosses (%d) in line %s." %(e.morphs,e.glosses,e.lineNumber))
    except TooManyGlossesError as e:
        print("EAF error: There are more glosses (%d) than morphs (%d) in line %s." %(e.glosses,e.morphs,e.lineNumber))
    except EmptyTiersError as e:
    	print("EAF error: There are empty tiers or incomplete glosses after line %s" %e.lineNumber)

#----------------------------------------------------------------------------------------------------
def test_Imp(display):

    print("--- test_Imp")

    text = Text("../testTextPyData/ZMarRevised/SantaMariaTheImp.eaf",
                "../testTextPyData/ZMarRevised/Audio",
                "../testTextPyData/ZMarRevised/abbreviations.txt",
                "../testTextPyData/ZMarRevised/tierGuide.yaml")
     
    #IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if(display):
            filename = "test_Imp.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print("EAF error: There are more morphs (%d) than glosses (%d) in line %s." %(e.morphs,e.glosses,e.lineNumber))
    except TooManyGlossesError as e:
        print("EAF error: There are more glosses (%d) than morphs (%d) in line %s." %(e.glosses,e.morphs,e.lineNumber))
    except EmptyTiersError as e:
    	print("EAF error: There are empty tiers or incomplete glosses after line %s" %e.lineNumber)

#----------------------------------------------------------------------------------------------------
def test_Prayer(display):

    print("--- test_Prayer")

    text = Text("../testTextPyData/Prayer_superscript/20150717_Prayer_community_one.eaf",
                "../testTextPyData/Prayer_superscript/Audio",
                "../testTextPyData/Prayer_superscript/grammaticalTerms.txt",
                "../testTextPyData/Prayer_superscript/tierGuide.yaml")
     
    #IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if(display):
            filename = "test_Prayer.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print("EAF error: There are more morphs (%d) than glosses (%d) in line %s." %(e.morphs,e.glosses,e.lineNumber))
    except TooManyGlossesError as e:
        print("EAF error: There are more glosses (%d) than morphs (%d) in line %s." %(e.glosses,e.morphs,e.lineNumber))
    except EmptyTiersError as e:
    	print("EAF error: There are empty tiers or incomplete glosses after line %s" %e.lineNumber)

#----------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    runTests()
