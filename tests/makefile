all: morphemeGloss ijalLine audioExtractor text_daylight text_monkeyAndThunder  text_PlumedSerpent text_prayer test_chatino5 test_chatino6

morphemeGloss:
	python3 test_MorphemeGloss.py

ijalLine:
	python3 test_IjalLine.py

audioExtractor:
	python3 test_audioExtractor.py

text_monkeyAndThunder:
	python3 test_text_MonkeyAndThunder.py

text_daylight:
	python3 test_text_HowDaylightWasStolen.py

text_PlumedSerpent:
	python3 test_text_PlumedSerpent.py

text_prayer:
	python3 test_text_prayer.py

# takes several minutes to run, but a worthwhile test, now not run out of the "all" target above
text_lokono:
	python3 test_text_lokono.py

test_chatino5:
	python3 test_text_Chatino_5Line.py

test_chatino6:
	python3 test_text_Chatino_6Line.py
