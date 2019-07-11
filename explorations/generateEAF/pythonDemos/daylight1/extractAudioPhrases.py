import re
import sys
sys.path.append("/Users/paul/github/slexil")

from audioExtractor import *

ea = AudioExtractor("audio/harryMosesHowDaylightWasStolen.wav", "daylight.eaf", "audio")
ea.extract(quiet=False)
