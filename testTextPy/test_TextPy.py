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
from audioExtractor import AudioExtractor
from bs4 import BeautifulSoup

# ----------------------------------------------------------------------------------------------------
pd.set_option('display.width', 1000)


# ----------------------------------------------------------------------------------------------------
def runTests(display=False):
    # test_Inferno_numbering(display)--these two tests are no longer relevant as annotations are not numbered
    # test_Aymara_numbering(display) --sequentially in the .eaf file anyway, so line ≠ annotation always
    # test_Riverwoman(display) --.eaf file for this one has gone missing

    test_MonkeyAndThunder(display)
    test_Fishwoman(display)
    test_Merchant(display)
    test_Jaguar(display)
    test_SanMiguel(display)
    test_Caterpillar(display)
    test_Lazy(display)
    test_Imp(display)
    test_Prayer(display)
    test_Inferno(display)
    test_MonkeyAndThunder(display)
    test_Aymara(display)
    test_Aymara_final(display)
    test_Raven(display)
    test_Raven_errors(display)


# ----------------------------------------------------------------------------------------------------
def test_Raven_errors(display):
    '''tests .eaf file with empty and missing line or translation annotations'''

    print("--- test_Raven_with_errors")

    audioFilename = "AM_RavenCopiesSiblingsNRAudition-wav.wav"
    elanXmlFilename = "../testTextPyData/Raven/newraven_all_errors.eaf"
    targetDirectory = "../testTextPyData/Raven/audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../testTextPyData/Raven"
    tierGuideFile = "../testTextPyData/Raven/tierGuide.yaml"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable

    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=None,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)

    htmlText = text.toHTML()
    if (display):
        filename = "../testTextPyData/Raven/badraven.html"
        f = open(filename, "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % filename)


# ----------------------------------------------------------------------------------------------------
def test_Raven(display):
    print("--- test_Raven")

    audioFilename = "AM_RavenCopiesSiblingsNRAudition-wav.wav"
    elanXmlFilename = "../testTextPyData/Raven/newraven.eaf"
    targetDirectory = "../testTextPyData/Raven/audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../testTextPyData/Raven"
    tierGuideFile = "../testTextPyData/Raven/tierGuide.yaml"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=None,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)

    htmlText = text.toHTML()
    if (display):
        filename = "../testTextPyData/Raven/newraven.html"
        f = open(filename, "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % filename)


# ----------------------------------------------------------------------------------------------------
def test_Aymara_final(display):
    print("--- test_Aymara_final")

    audioFilename = "Final-Edwin-historia-del-oso_no_anotado__ch1.wav"
    elanXmlFilename = "../testTextPyData/Aymara_final/Aymara-final.eaf"
    targetDirectory = "../testTextPyData/Aymara_final/Audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../testTextPyData/Aymara_final"
    tierGuideFile = "../testTextPyData/Aymara_final/tierGuide.yaml"
    grammaticalTermsFile = "../testTextPyData/Aymara_final/List of abbreviations.txt"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)  # ,
    # startStopTable=times)

    # IjalLine.getTable(1)

    htmlText = text.toHTML()
    if (display):
        filename = "../testTextPyData/Aymara_final/Aymara_final.html"
        f = open(filename, "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % filename)


# ----------------------------------------------------------------------------------------------------
def test_Aymara(display):
    print("--- test_Aymara")

    audioFilename = "Final-Edwin-historia-del-oso_no_anotado__ch1.wav"
    elanXmlFilename = "../testTextPyData/Aymara/Aymara-final.eaf"
    targetDirectory = "../testTextPyData/Aymara/Audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../testTextPyData/Aymara"
    tierGuideFile = "../testTextPyData/Aymara/tierGuide.yaml"
    grammaticalTermsFile = "../testTextPyData/Aymara/List of abbreviations.txt"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)  # ,
    # startStopTable=times)

    # IjalLine.getTable(1)

    htmlText = text.toHTML()
    if (display):
        filename = "../testTextPyData/Aymara/Aymara.html"
        f = open(filename, "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % filename)


# ----------------------------------------------------------------------------------------------------
def test_Inferno_numbering(display):
    print("--- test_Inferno_numbering")

    audioFilename = "inferno-threeLines.wav"
    elanXmlFilename = "../explorations/playAudioInSequence/Inferno/inferno-threeLines.eaf"
    targetDirectory = "../explorations/playAudioInSequence/Inferno/Audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../explorations/playAudioInSequence/Inferno"
    tierGuideFile = "../explorations/playAudioInSequence/Inferno/tierGuide.yaml"
    grammaticalTermsFile = "../explorations/playAudioInSequence/Inferno/abbreviations.txt"
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)

    # IjalLine.getTable(1)

    htmlText = text.toHTML()

    soup = BeautifulSoup(htmlText, 'html.parser')
    lines = soup.find_all("div", {"class": "line-wrapper"})
    for line in lines:
        id = line.get('id')
        textLineNumber = line.find("div", {"class": "line-sidebar"}).text[:-2]
        audioTag = line.find("source")
        audioFile = audioTag.get('src')
        fileID = audioFile[7:-5]
        print(id, textLineNumber, fileID)
        assert (id == textLineNumber == fileID)

    if (display):
        filename = "../explorations/playAudioInSequence/Inferno/inferno-threeLines.html"
        f = open(filename, "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % filename)


# ----------------------------------------------------------------------------------------------------
def test_Aymara_numbering(display):
    print("--- test_Aymara_numbering")

    audioFilename = "Final-Edwin-historia-del-oso_no_anotado__ch1.wav"
    elanXmlFilename = "../testTextPyData/Aymara/Aymara-final.eaf"
    targetDirectory = "../testTextPyData/Aymara/Audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../testTextPyData/Aymara"
    tierGuideFile = "../testTextPyData/Aymara/tierGuide.yaml"
    grammaticalTermsFile = "../testTextPyData/Aymara/List of abbreviations.txt"
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)

    # IjalLine.getTable(1)

    htmlText = text.toHTML()

    soup = BeautifulSoup(htmlText, 'html.parser')
    lines = soup.find_all("div", {"class": "line-wrapper"})
    for line in lines:
        id = line.get('id')
        textLineNumber = line.find("div", {"class": "line-sidebar"}).text[:-2]
        audioTag = line.find("source")
        audioFile = audioTag.get('src')
        fileID = audioFile[7:-4]
        assert (id == textLineNumber == fileID)

    if (display):
        filename = "../testTextPyData/Aymara/Aymara.html"
        f = open(filename, "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % filename)


# ----------------------------------------------------------------------------------------------------
def test_Inferno(display):
    print("--- test_Inferno")

    audioFilename = "inferno-threeLines.wav"
    elanXmlFilename = "../explorations/playAudioInSequence/Inferno/inferno-threeLines.eaf"
    targetDirectory = "../explorations/playAudioInSequence/Inferno/Audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../explorations/playAudioInSequence/Inferno"
    tierGuideFile = "../explorations/playAudioInSequence/Inferno/tierGuide.yaml"
    grammaticalTermsFile = "../explorations/playAudioInSequence/Inferno/abbreviations.txt"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)  # ,
    # 				startStopTable=times)

    # IjalLine.getTable(1)

    htmlText = text.toHTML()
    if (display):
        filename = "../explorations/playAudioInSequence/Inferno/inferno-threeLines.html"
        f = open(filename, "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % filename)


# ----------------------------------------------------------------------------------------------------
def test_MonkeyAndThunder(display):
    print("--- test_MonkeyAndThunder")
    audioFilename = "AYA1_MonkeyandThunder-1.wav"
    elanXmlFilename = "../explorations/playAudioInSequence/Monkey/AYA1_MonkeyandThunder.eaf"
    targetDirectory = "../explorations/playAudioInSequence/Monkey/Audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../explorations/playAudioInSequence/Monkey"
    tierGuideFile = "../explorations/playAudioInSequence/Monkey/tierGuide.yaml"
    grammaticalTermsFile = "../explorations/playAudioInSequence/Monkey/abbreviations.txt"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)  # ,
    # 				startStopTable=times)

    # IjalLine.getTable(1)

    htmlText = text.toHTML()
    if (display):
        filename = "../explorations/playAudioInSequence/Monkey/monkeyAndThunderTest.html"
        f = open(filename, "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % filename)


# ----------------------------------------------------------------------------------------------------
def test_Fishwoman(display):
    print("--- test_Fishwoman")
    audioFilename = "2_AYA2_FishWoman.wav"
    elanXmlFilename = "../testTextPyData/2_AYA2_FishWoman/2_AYA2_FishWoman.eaf"
    targetDirectory = "../testTextPyData/2_AYA2_FishWoman/Audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../testTextPyData/2_AYA2_FishWoman"
    tierGuideFile = "../testTextPyData/2_AYA2_FishWoman/tierGuide.yaml"
    grammaticalTermsFile = "../testTextPyData/2_AYA2_FishWoman/abbreviations.txt"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)  # ,
    # 				startStopTable=times)

    # IjalLine.getTable(1)

    htmlText = text.toHTML()
    if (display):
        filename = "../testTextPyData/2_AYA2_FishWoman/test_Fishwoman.html"
        f = open(filename, "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % filename)


# ----------------------------------------------------------------------------------------------------
def test_Merchant(display):
    print("--- test_Merchant")
    audioFilename = "JIT0006.WAV"
    elanXmlFilename = "../testTextPyData/JIT0006_ori/JIT0006_ori.eaf"
    targetDirectory = "../testTextPyData/JIT0006_ori/audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../testTextPyData/JIT0006_ori"
    tierGuideFile = "../testTextPyData/JIT0006_ori/tierGuide.yaml"
    grammaticalTermsFile = "../testTextPyData/JIT0006_ori/grammaticalTerms.txt"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)  # ,
    # 				startStopTable=times)

    # IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if (display):
            filename = "test_Merchant.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print(
            "EAF error: There are more morphs (%d) than glosses (%d) in line %s." % (e.morphs, e.glosses, e.lineNumber))
    except TooManyGlossesError as e:
        print(
            "EAF error: There are more glosses (%d) than morphs (%d) in line %s." % (e.glosses, e.morphs, e.lineNumber))
    except EmptyTiersError as e:
        print("EAF error: There are empty tiers or incomplete glosses after line %s" % e.lineNumber)


# ----------------------------------------------------------------------------------------------------
def test_Jaguar(display):
    print("--- test_Jaguar")
    audioFilename = "5_OCO2_TheOpposumAndTheJaguar.wav"
    elanXmlFilename = "../testTextPyData/Ocotepec_TheOpposumAndTheJaguar/OCO2_JaguarAndOpossum.eaf"
    targetDirectory = "../testTextPyData/Ocotepec_TheOpposumAndTheJaguar/audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../testTextPyData/Ocotepec_TheOpposumAndTheJaguar"
    tierGuideFile = "../testTextPyData/Ocotepec_TheOpposumAndTheJaguar/tierGuide.yaml"
    grammaticalTermsFile = "../testTextPyData/Ocotepec_TheOpposumAndTheJaguar/abbreviations.txt"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)

    # IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if (display):
            filename = "test_Jaguar.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print(
            "EAF error: There are more morphs (%d) than glosses (%d) in line %s." % (e.morphs, e.glosses, e.lineNumber))
    except TooManyGlossesError as e:
        print(
            "EAF error: There are more glosses (%d) than morphs (%d) in line %s." % (e.glosses, e.morphs, e.lineNumber))
    except EmptyTiersError as e:
        print("EAF error: There are empty tiers or incomplete glosses after line %s" % e.lineNumber)


# ----------------------------------------------------------------------------------------------------
def test_Riverwoman(display):
    print("--- test_Riverwoman")
    audioFilename = "2015-01-23_NÑwayomo.wav"
    elanXmlFilename = "../testTextPyData/Ocotepec_Riverwoman/2015-01-23_NÑwayomo.eaf"
    targetDirectory = "../testTextPyData/Ocotepec_Riverwoman/audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../testTextPyData/Ocotepec_Riverwoman"
    tierGuideFile = "../testTextPyData/Ocotepec_Riverwoman/tierGuide.yaml"
    grammaticalTermsFile = "../testTextPyData/Ocotepec_Riverwoman/abbreviations.txt"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)  # ,
    # 				startStopTable=times)

    # IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if (display):
            filename = "test_Riverwoman.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print(
            "EAF error: There are more morphs (%d) than glosses (%d) in line %s." % (e.morphs, e.glosses, e.lineNumber))
    except TooManyGlossesError as e:
        print(
            "EAF error: There are more glosses (%d) than morphs (%d) in line %s." % (e.glosses, e.morphs, e.lineNumber))
    except EmptyTiersError as e:
        print("EAF error: There are empty tiers or incomplete glosses after line %s" % e.lineNumber)


# ----------------------------------------------------------------------------------------------------
def test_SanMiguel(display):
    print("--- test_SanMiguel")
    audioFilename = "SanMiguelChimalapaZoque.wav"
    elanXmlFilename = "../testTextPyData/SanMiguelChimalapaZoque/SanMiguelChimalapaZoque.eaf"
    targetDirectory = "../testTextPyData/SanMiguelChimalapaZoque/audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../testTextPyData/SanMiguelChimalapaZoque"
    tierGuideFile = "../testTextPyData/SanMiguelChimalapaZoque/tierGuide.yaml"
    grammaticalTermsFile = "../testTextPyData/SanMiguelChimalapaZoque/abbreviations.txt"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)  # ,
    # 				startStopTable=times)

    # IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if (display):
            filename = "test_SanMiguel.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print(
            "EAF error: There are more morphs (%d) than glosses (%d) in line %s." % (e.morphs, e.glosses, e.lineNumber))
    except TooManyGlossesError as e:
        print(
            "EAF error: There are more glosses (%d) than morphs (%d) in line %s." % (e.glosses, e.morphs, e.lineNumber))
    except EmptyTiersError as e:
        print("EAF error: There are empty tiers or incomplete glosses after line %s" % e.lineNumber)


# ----------------------------------------------------------------------------------------------------
def test_Caterpillar(display):
    print("--- test_Caterpillar")
    audioFilename = "SOT_TheCaterpillar.wav"
    elanXmlFilename = "../testTextPyData/SOT_Caterpillar/SOT_TheCaterpillar_Morph.eaf"
    targetDirectory = "../testTextPyData/SOT_Caterpillar/audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../testTextPyData/SOT_Caterpillar"
    tierGuideFile = "../testTextPyData/SOT_Caterpillar/tierGuide.yaml"
    grammaticalTermsFile = "../testTextPyData/SOT_Caterpillar/abbreviations.txt"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)  # ,
    # 				startStopTable=times)

    # IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if (display):
            filename = "test_Caterpillar.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print(
            "EAF error: There are more morphs (%d) than glosses (%d) in line %s." % (e.morphs, e.glosses, e.lineNumber))
    except TooManyGlossesError as e:
        print(
            "EAF error: There are more glosses (%d) than morphs (%d) in line %s." % (e.glosses, e.morphs, e.lineNumber))
    except EmptyTiersError as e:
        print("EAF error: There are empty tiers or incomplete glosses after line %s" % e.lineNumber)


# ----------------------------------------------------------------------------------------------------
def test_Lazy(display):
    print("--- test_Lazy")

    audioFilename = "4_TEX_TheLazyWoman.wav"
    elanXmlFilename = "../testTextPyData/TEX_Lazy/TEX_Lazy.eaf"
    targetDirectory = "../testTextPyData/TEX_Lazy/audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../testTextPyData/TEX_Lazy"
    tierGuideFile = "../testTextPyData/TEX_Lazy/tierGuide.yaml"
    grammaticalTermsFile = "../testTextPyData/TEX_Lazy/abbreviations.txt"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)  # ,
    # 				startStopTable=times)

    # IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if (display):
            filename = "test_Lazy.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print(
            "EAF error: There are more morphs (%d) than glosses (%d) in line %s." % (e.morphs, e.glosses, e.lineNumber))
    except TooManyGlossesError as e:
        print(
            "EAF error: There are more glosses (%d) than morphs (%d) in line %s." % (e.glosses, e.morphs, e.lineNumber))
    except EmptyTiersError as e:
        print("EAF error: There are empty tiers or incomplete glosses after line %s" % e.lineNumber)


# ----------------------------------------------------------------------------------------------------
def test_Imp(display):
    print("--- test_Imp")
    audioFilename = "SantaMariaTheImp.wav"
    elanXmlFilename = "../testTextPyData/ZMarRevised/SantaMariaTheImp.eaf"
    targetDirectory = "../testTextPyData/ZMarRevised/audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../testTextPyData/ZMarRevised"
    tierGuideFile = "../testTextPyData/ZMarRevised/tierGuide.yaml"
    grammaticalTermsFile = "../testTextPyData/ZMarRevised/abbreviations.txt"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)  # ,
    # 				startStopTable=times)

    # IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if (display):
            filename = "test_Imp.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print(
            "EAF error: There are more morphs (%d) than glosses (%d) in line %s." % (e.morphs, e.glosses, e.lineNumber))
    except TooManyGlossesError as e:
        print(
            "EAF error: There are more glosses (%d) than morphs (%d) in line %s." % (e.glosses, e.morphs, e.lineNumber))
    except EmptyTiersError as e:
        print("EAF error: There are empty tiers or incomplete glosses after line %s" % e.lineNumber)


# ----------------------------------------------------------------------------------------------------
def test_Prayer(display):
    print("--- test_Prayer")
    audioFilename = "SJQ-2009_Cruz.wav"
    elanXmlFilename = "../testTextPyData/Prayer_superscript/20150717_Prayer_community_one.eaf"
    targetDirectory = "../testTextPyData/Prayer_superscript/audio"
    soundFile = os.path.join(targetDirectory, audioFilename)
    projectDirectory = "../testTextPyData/Prayer_superscript"
    tierGuideFile = "../testTextPyData/Prayer_superscript/tierGuide.yaml"
    grammaticalTermsFile = "../testTextPyData/Prayer_superscript/grammaticalTerms.txt"
    ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
    ae.determineStartAndEndTimes()
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)  # ,
    # 				startStopTable=times)

    # IjalLine.getTable(1)

    try:
        htmlText = text.toHTML()
        if (display):
            filename = "test_Prayer.html"
            f = open(filename, "w")
            f.write(indent(htmlText))
            f.close()
            os.system("open %s" % filename)
    except TooManyMorphsError as e:
        print(
            "EAF error: There are more morphs (%d) than glosses (%d) in line %s." % (e.morphs, e.glosses, e.lineNumber))
    except TooManyGlossesError as e:
        print(
            "EAF error: There are more glosses (%d) than morphs (%d) in line %s." % (e.glosses, e.morphs, e.lineNumber))
    except EmptyTiersError as e:
        print("EAF error: There are empty tiers or incomplete glosses after line %s" % e.lineNumber)


# ----------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    runTests()
