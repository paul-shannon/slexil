default:
	@echo targets: extractAudio, eaf, html

all: eaf extractAudio html

extractAudio:
	~/anaconda/bin/python3 extractAudioPhrases.py

eaf:
	~/anaconda/bin/python3 toEAF.py


html:
	~/anaconda/bin/python3 eafToWebpage.py




