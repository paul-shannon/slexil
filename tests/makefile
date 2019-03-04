all: morphemeGloss ijalLine audioExtractor text_daylight text_monkeyAndThunder  text_PlumedSerpent text_prayer test_chatino5 test_chatino6

morphemeGloss:
	python test_MorphemeGloss.py

ijalLine:
	python test_IjalLine.py

audioExtractor:
	python test_audioExtractor.py

text_monkeyAndThunder:
	python test_text_MonkeyAndThunder.py

text_daylight:
	python test_text_HowDaylightWasStolen.py

text_PlumedSerpent:
	python test_text_PlumedSerpent.py

text_prayer:
	python test_text_prayer.py

# takes several minutes to run, but a worthwhile test, now not run out of the "all" target above
text_lokono:
	python test_text_lokono.py

test_chatino5:
	python test_text_Chatino_5Line.py

test_chatino6:
	test_text_Chatino_5Line.py
