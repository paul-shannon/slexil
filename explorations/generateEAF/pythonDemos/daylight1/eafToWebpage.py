import re
import sys
sys.path.append("../../../..")
from text import *
from audioExtractor import *
import importlib
import os
import pdb
#----------------------------------------------------------------------------------------------------
pd.set_option('display.width', 1000)
#----------------------------------------------------------------------------------------------------
#audioFilename = "daylight_1_9.wav"
audioFilename = "harryMosesHowDaylightWasStolen.wav"
elanXmlFilename="daylight.eaf"
audioPhrasesTargetDirectory = "audio"
soundFile = os.path.join(audioPhrasesTargetDirectory, audioFilename)
projectDirectory="./"
tierGuideFile="tierGuide.yaml"
grammaticalTermsFile="grammaticalTerms.txt"

#assert(os.path.isfile(audioFilename))
assert(os.path.isfile(elanXmlFilename))
assert(os.path.isdir(audioPhrasesTargetDirectory))
assert(os.path.isfile(soundFile))
assert(os.path.isdir(projectDirectory))
assert(os.path.isfile(tierGuideFile))
assert(os.path.isfile(grammaticalTermsFile))


#ae = AudioExtractor(audioFilename, elanXmlFilename, audioPhrasesTargetDirectory)
#ae.determineStartAndEndTimes()
#times = ae.startStopTable
text = Text(elanXmlFilename,
	    soundFile,
	    grammaticalTermsFile=grammaticalTermsFile,
	    tierGuideFile=tierGuideFile,
	    projectDirectory=projectDirectory)
	    #startStopTable=times)

htmlText = text.toHTML()
filename = "daylight.html"
f = open(filename, "w")
f.write(indent(htmlText))
f.close()
display = True
if(display):
    os.system("open %s" % filename)
