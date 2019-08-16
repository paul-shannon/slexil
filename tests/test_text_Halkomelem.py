import re
import sys
sys.path.append("..")
from text import *
import importlib
import os
import pdb
from audioExtractor import AudioExtractor
#----------------------------------------------------------------------------------------------------
pd.set_option('display.width', 1000)
#----------------------------------------------------------------------------------------------------

def runTests(display=False):

	test_GoldenEagle(True)
	test_AMRaven(True)

def test_GoldenEagle(display):
	audioFilename = "WS_GoldenEagle4.wav"
	elanXmlFilename="HHgoldenEagle4.eaf"
	targetDirectory = "../testData/GoldenEagle/audio"
	soundFile = os.path.join(targetDirectory,audioFilename)
	projectDirectory="../testData/GoldenEagle"
	tierGuideFile="../testData/GoldenEagle/tierGuide.yaml"
	#grammaticalTermsFile="../testData/lokono/grammaticalTerms.txt"
	elanFile = os.path.join(projectDirectory,elanXmlFilename)
	ae = AudioExtractor(soundFile, elanFile, targetDirectory)
	ae.determineStartAndEndTimes()
	ae.extract()
	times = ae.startStopTable	
	text = Text(elanFile,
				soundFile,
				grammaticalTermsFile=None,
				tierGuideFile=tierGuideFile,
				projectDirectory=projectDirectory)

	print("--- test_toHTML")

	text.getLineAsTable(0)

	htmlText = text.toHTML()
	filename = "../testData/GoldenEagle/GoldenEagle.html"
	f = open(filename, "w")
	f.write(indent(htmlText))
	f.close()

	if(display):
		os.system("open %s" % filename)

def test_AMRaven(display):
	audioFilename = "AM_RavenCopiesSiblingsNRAudition-wav.wav"
	elanXmlFilename="newraven.eaf"
	targetDirectory = "../testData/Raven/audio"
	soundFile = os.path.join(targetDirectory,audioFilename)
	projectDirectory="../testData/Raven"
	tierGuideFile="../testData/Raven/tierGuide.yaml"
	#grammaticalTermsFile="../testData/lokono/grammaticalTerms.txt"
	elanFile = os.path.join(projectDirectory,elanXmlFilename)
	ae = AudioExtractor(soundFile, elanFile, targetDirectory)
	ae.determineStartAndEndTimes()
	ae.extract()
	times = ae.startStopTable
	text = Text(elanFile,
				soundFile,
				grammaticalTermsFile=None,
				tierGuideFile=tierGuideFile,
				projectDirectory=projectDirectory)

	print("--- test_toHTML")

	text.getLineAsTable(0)

	htmlText = text.toHTML()
	filename = "../testData/Raven/RavenNew.html"
	f = open(filename, "w")
	f.write(indent(htmlText))
	f.close()

	if(display):
		os.system("open %s" % filename)


if __name__ == '__main__':
	runTests()
