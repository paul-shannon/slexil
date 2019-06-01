import os.path
import pandas as pd
from xml.etree import ElementTree as etree
from scipy.io.wavfile import *

class AudioExtractor:

    audioFilename = ''
    elanXmlFilename = ''
    targetDirectory = ''

    def __init__(self, audioFilename, elanXmlFilename, targetDirectory):
       self.audioFilename = audioFilename
       self.elanXmlFilename = elanXmlFilename
       self.targetDirectory = targetDirectory

    def validInputs(self):
       assert(os.path.exists(audioFilename))
       assert(os.path.exists(elanXmlFilename))
       assert(os.path.isdir(targetDirectory))
       return(True)

    def determineStartAndEndTimes(self):
       xmlDoc = etree.parse(self.elanXmlFilename)
       timeSlotElements = xmlDoc.findall("TIME_ORDER/TIME_SLOT")
       audioTiers = xmlDoc.findall("TIER/ANNOTATION/ALIGNABLE_ANNOTATION")
       timeIDs = [x.attrib["TIME_SLOT_ID"] for x in timeSlotElements]
       times = [int(x.attrib["TIME_VALUE"]) for x in timeSlotElements]
#        audioIDs = [x.attrib["ANNOTATION_ID"] for x in audioTiers]
       audioIDs = list(range(1, len(audioTiers)+1))
       tsRef1 = [x.attrib["TIME_SLOT_REF1"] for x in audioTiers]
       tsRef2 = [x.attrib["TIME_SLOT_REF2"] for x in audioTiers]
       d = {"id": audioIDs, "t1": tsRef1, "t2": tsRef2}
       tbl_t1 = pd.DataFrame({"id": audioIDs, "t1": tsRef1})
       tbl_t2 = pd.DataFrame({"id": audioIDs, "t2": tsRef2})
       tbl_times = pd.DataFrame({"id": timeIDs, "timeValue": times})
       tbl_t1m = pd.merge(tbl_t1, tbl_times, left_on="t1", right_on="id")
       tbl_t2m = pd.merge(tbl_t2, tbl_times, left_on="t2", right_on="id")
       tbl_raw = pd.merge(tbl_t1m, tbl_t2m, on="id_x")
       tbl = tbl_raw.drop(["id_y_x", "id_y_y"], axis=1)
          # still need to rename, maybe also reorder columns
       tbl.columns = ["lineID", "t1", "start", "t2", "end"]
       list(tbl.columns)
       tbl = tbl[["lineID", "start", "end", "t1", "t2"]]
#        tbl = tbl.sort('start')
       return(tbl)

    def extract(self, quiet=True):
       tbl = self.determineStartAndEndTimes()
       self.startStopTable = tbl.to_csv(index=False)
       print(self.startStopTable)
       rate, mtx = read(self.audioFilename)
       mtx.shape
       mtx.shape[0]/rate   # 5812410, 2
       samples = mtx.shape[0]
       duration = mtx.shape[0] / rate
       phraseCount = tbl.shape[0]
       for i in range(phraseCount):
           phraseID, start, end = tbl.ix[i].tolist()[0:3]
           startSeconds = start/1000
           endSeconds = end/1000
           startIndex = int(round(startSeconds * rate))
           endIndex   = int(round(endSeconds * rate))
           phrase = mtx[startIndex:endIndex,]
           sampleFilename = "%s/a%s.wav" % (self.targetDirectory, phraseID)
           if(not quiet):
              print("--- %d) writing %d samples to %s" % (i, phrase.shape[0], sampleFilename))
           write(sampleFilename, rate, phrase)
      
               
