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
	targetDirectory = "../testTextPyData/GoldenEagle/audio"
	soundFile = os.path.join(targetDirectory,audioFilename)
	projectDirectory="../testTextPyData/GoldenEagle"
	tierGuideFile="../testTextPyData/GoldenEagle/tierGuide.yaml"
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
	filename = "../testTextPyData/GoldenEagle/GoldenEagle.html"
	f = open(filename, "w")
	f.write(indent(htmlText))
	f.close()

	if(display):
		os.system("open %s" % filename)

def test_AMRaven(display):
	audioFilename = "AM_RavenCopiesSiblingsNRAudition-wav.wav"
	elanXmlFilename="newraven.eaf"
	targetDirectory = "../testTextPyData/Raven/audio"
	soundFile = os.path.join(targetDirectory,audioFilename)
	projectDirectory="../testTextPyData/Raven"
	tierGuideFile="../testTextPyData/Raven/tierGuide.yaml"
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
	filename = "../testTextPyData/Raven/RavenNew.html"
	f = open(filename, "w")
	f.write(indent(htmlText))
	f.close()

	if(display):
		os.system("open %s" % filename)


if __name__ == '__main__':
	runTests()
