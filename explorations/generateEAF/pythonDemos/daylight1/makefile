default:
	@echo targets: build [extractAudio, eaf, html], publish

build: eaf extractAudio html

extractAudio:
	~/anaconda/bin/python3 extractAudioPhrases.py

eaf:
	~/anaconda/bin/python3 toEAF.py


html:
	~/anaconda/bin/python3 eafToWebpage.py

publish:
	scp daylight.html paulshannnon@pshannon.net:public_html/pshannon.net/daylight/index.html
	scp ijal.css paulshannnon@pshannon.net:public_html/pshannon.net/daylight/
	scp ijalUtils.js paulshannnon@pshannon.net:public_html/pshannon.net/daylight/
	scp -pr audio/a*.wav paulshannnon@pshannon.net:public_html/pshannon.net/daylight/audio/
	open http://pshannon.net/daylight




