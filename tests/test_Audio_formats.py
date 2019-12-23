import re
import sys

sys.path.append("..")
from text import *
import importlib
import os
import pdb
from audioExtractor import AudioExtractor

# ----------------------------------------------------------------------------------------------------
pd.set_option('display.width', 1000)


# ----------------------------------------------------------------------------------------------------
def runTests(display=False):
    test_wav(display)
    test_ogg(display)
    #test_mp3(display)

# ----------------------------------------------------------------------------------------------------
def test_wav(display):

    print("--- test_wav")
    audioFilename = "daylight_1_4.wav"
    elanXmlFilename = "../testData/harryMosesDaylight/daylight_1_4.eaf"
    targetDirectory = "../testData/harryMosesDaylight/audio"
    projectDirectory = "../testData/harryMosesDaylight"
    soundFile = os.path.join(projectDirectory, audioFilename)
    print(soundFile)
    tierGuideFile = "../testData/harryMosesDaylight/tierGuide.yaml"
    grammaticalTermsFile = "../testData/harryMosesDaylight/grammaticalTerms.txt"
    ae = AudioExtractor(soundFile, elanXmlFilename, targetDirectory)
    ae.validInputs()
    ae.extract(False)
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)

    htmlText = text.toHTML()
    if (display):
        filename = "../testData/harryMosesDaylight/daylightwav.html"
        f = open(filename, "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % filename)

# ----------------------------------------------------------------------------------------------------
def test_mp3(display):

    print("--- test_mp3")
    audioFilename = "daylight_1_4.mp3"
    elanXmlFilename = "../testData/harryMosesDaylight/daylight_1_4.eaf"
    targetDirectory = "../testData/harryMosesDaylight/audio"
    projectDirectory = "../testData/harryMosesDaylight"
    soundFile = os.path.join(projectDirectory, audioFilename)
    tierGuideFile = "../testData/harryMosesDaylight/tierGuide.yaml"
    grammaticalTermsFile = "../testData/harryMosesDaylight/grammaticalTerms.txt"
    ae = AudioExtractor(soundFile, elanXmlFilename, targetDirectory)
    ae.validInputs()
    ae.extract(False)
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)

    htmlText = text.toHTML()
    if (display):
        filename = "../testData/harryMosesDaylight/daylightmp3.html"
        f = open(filename, "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % filename)

# ----------------------------------------------------------------------------------------------------
def test_ogg(display):

    print("--- test_ogg")
    audioFilename = "daylight_1_4.ogg"
    elanXmlFilename = "../testData/harryMosesDaylight/daylight_1_4.eaf"
    targetDirectory = "../testData/harryMosesDaylight/audio"
    projectDirectory = "../testData/harryMosesDaylight"
    soundFile = os.path.join(projectDirectory, audioFilename)
    print(soundFile)
    tierGuideFile = "../testData/harryMosesDaylight/tierGuide.yaml"
    grammaticalTermsFile = "../testData/harryMosesDaylight/grammaticalTerms.txt"
    ae = AudioExtractor(soundFile, elanXmlFilename, targetDirectory)
    ae.validInputs()
    ae.extract(False)
    times = ae.startStopTable
    text = Text(elanXmlFilename,
                soundFile,
                grammaticalTermsFile=grammaticalTermsFile,
                tierGuideFile=tierGuideFile,
                projectDirectory=projectDirectory)

    htmlText = text.toHTML()
    if (display):
        filename = "../testData/harryMosesDaylight/daylightogg.html"
        f = open(filename, "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % filename)

# ----------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    runTests()
