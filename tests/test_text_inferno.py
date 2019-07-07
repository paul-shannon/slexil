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

def createText():
	audioFilename = "inferno-threeLines.eaf.wav"
	elanXmlFilename="../testData/inferno-threeLines/inferno-threeLines.eaf"
	targetDirectory = "../testData/inferno-threeLines/audio"
	soundFile = os.path.join(targetDirectory,audioFilename)
	projectDirectory="../testData/inferno-threeLines"
	tierGuideFile="../testData/inferno-threeLines/tierGuide.yaml"
	grammaticalTermsFile="../testData/inferno-threeLines/grammaticalTerms.txt"
	ae = AudioExtractor(audioFilename, elanXmlFilename, targetDirectory)
	ae.determineStartAndEndTimes()
	times = ae.startStopTable

	text = Text(elanXmlFilename,
<<<<<<< HEAD
				soundFile,
				grammaticalTermsFile=grammaticalTermsFile,
				tierGuideFile=tierGuideFile,
				startStopTable=times,
				projectDirectory=projectDirectory,
				quiet=True)
=======
		    soundFile,
		    grammaticalTermsFile=grammaticalTermsFile,
		    tierGuideFile=tierGuideFile,
		    startStopTable=times,
		    projectDirectory=projectDirectory,
		    quiet=True)
>>>>>>> master

	return(text)


def runTests(display=False):
	test_constructor()
	test_toHTML(display)

def test_constructor():

	print("--- test_constructor")

	text = createText()
	assert(text.validInputs())
	tbl = text.getTierSummary()
	assert(tbl.shape == (4,3))
<<<<<<< HEAD
	pdb.set_trace()
	assert(list(tbl['key']) == ['morpheme', 'morphemeGloss', 'morphemePacking', 'speech'])
	assert(list(tbl['value']) == ['italianSpeech', 'english', 'morphemes', 'morphemeGloss'])
	assert(list(tbl['count']) == [4, 4, 4, 4])
=======
	assert(tbl['key'].tolist() == ['morpheme', 'morphemeGloss', 'speech', 'translation'])
	assert(tbl['value'].tolist() == ['morphemes', 'morphemeGloss', 'italianSpeech', 'english'])
	assert(list(tbl['count']) == [3, 3, 3, 3])
>>>>>>> master

def test_toHTML(display=False):

	print("--- test_toHTML")

	text = createText()

	text.getLineAsTable(1)

	htmlText = text.toHTML()
	filename = "daylight.html"
	f = open(filename, "w")
	f.write(indent(htmlText))
	f.close()
	if(display):
	   os.system("open %s" % filename)

if __name__ == '__main__':
	runTests()
