import sys
import os
from xml.etree import ElementTree as etree

if(len(sys.argv) != 2):
   print("usage:  python learnTierIDs.py <fullPath to eaf xml file>")
   sys.exit()

xmlFilename = sys.argv[1]

fileFound = os.path.isfile(xmlFilename)

if(not fileFound):
    print("error.  could not read eaf xml file'%s'" % xmlFilename)
    sys.exit()

#xmlFilename = "../testData/harryMosesDaylight/daylight_1_4.eaf"
tmpDoc = etree.parse(xmlFilename)
tierIDs = [tier.attrib["TIER_ID"] for tier in tmpDoc.findall("TIER")]
tiers = tmpDoc.findall("TIER")

for tier in tiers:
   tierID = tier.attrib["TIER_ID"]
   count = len(tier.findall("ANNOTATION"))
   print(" %30s: %4d" % (tierID, count))
   
   
