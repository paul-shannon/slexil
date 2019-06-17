import yaml
import csv
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, dump
from xml.dom import minidom
import datetime
import xml.etree as etree
import xmlschema
import pdb


# https://www.mpi.nl/tools/elan/EAF_Annotation_Format_3.0_and_ELAN.pdf
schemaXSD = "http://www.mpi.nl/tools/elan/EAFv3.0.xsd"
schema = xmlschema.XMLSchema(schemaXSD)

# "elements" are all the nodes in the xml document we create here, for instance speech, phonemes, phonemeGlosses, translation
# in a classic text, there will be an equal number of each element type: maybe 20 speech elements, 20 phoneme elements (each a
# set of tab-delemited phonemes), 20 phonemGlosses (also tab-delmited sets), 20 translations.
# in eaf xml, each kind of element is separated, gathered together in sequence:  there is a tier of speech elements,
# a tier of tab-delimited phoneme set elements; same for phonemeGlosses and translations.
# the relationship between, for example, a speech element and its phoneme set is explicit in our yaml schema: they are
# nested together in a line
# for eaf xml, however, we must provide explicit links tying related elements together.
# the eaf mechanism for doing this is
#   create a unique ANNOTATION_ID for each element, independent of element type.  a0, a1, a2 ... aMax
#   for each dependent element (everything except for time-aligned speech elements), also specify
#   an ANNOTATION_REF - which points back to the parent element:
#        ANNOTATION_ID     ANNOTATION_REF
#      phoneme set          speech
#      phonemicGloss set    phonemic set
#      translation          speech
# the refMap data structure records these ID/elementType/line relationships as they are dynamically
# created, so that we can them look up as child elements are subsequently created

referenceMap = {}

x = yaml.load(open("daylight1.yaml"))
# print(yaml.dump(x))

root = Element('ANNOTATION_DOCUMENT')
root.set('VERSION', '2.8')
root.set('FORMAT', '2.8')
root.set('AUTHOR', x['author'])
root.set('DATE', datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))
root.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
root.set('xsi:noNamespaceSchemaLocation', schemaXSD)

header = SubElement(root, 'HEADER')
header.set("MEDIA_FILE", "")
header.set("TIME_UNITS", "milliseconds")

mediaDescriptor = SubElement(header, 'MEDIA_DESCRIPTOR')
mediaDescriptor.set('MEDIA_URL', "file:///Users/paul/github/howDaylightWasStolen-harryMoses/peelingOffSomeDaylight/daylight77a.wav")
mediaDescriptor.set('MIME_TYPE', "audio/x-wav")
mediaDescriptor.set('RELATIVE_MEDIA_URL', "file://./daylight_1_4.wav")
property = SubElement(header, "PROPERTY")
property.set('NAME', "lastUsedAnnotationId")
property.text = '340'

timeOrder = SubElement(root, "TIME_ORDER")

startTimes = [line["startTime"] for line in x["lines"]]
endTimes = [line["endTime"] for line in x["lines"]]
allTimes = sorted(set(startTimes + endTimes))

for i in range(len(allTimes)):
    timeSlot  = SubElement(timeOrder, "TIME_SLOT")
    timeSlot.set("TIME_SLOT_ID", "ts%d" % i)
    timeSlot.set("TIME_VALUE", "%d" % allTimes[i])

documentElementID = 0   # unique, a0, a1, ... aN

lineFieldNames = list(x["lines"][0].keys())
tierNames = lineFieldNames[2:4]
for tierName in tierNames:
   tier = SubElement(root, "TIER")
   tier.set("DEFAULT_LOCALE", "tr")   # not sure what "tr" means
   #if(tierName.lower().find("speech") >= 0):
   print("tierName: %s" % tierName)
   if(tierName == "lushootseedSpeech"):
       tier.set("LINGUISTIC_TYPE_REF", "speech")
       tier.set("TIER_ID", tierName)
       speechLines = [line[tierName] for line in x["lines"]]
       lineNumber = 0
       for speechLine in speechLines:
           annotation = SubElement(tier, "ANNOTATION")
           alignableAnnotation = SubElement(annotation, "ALIGNABLE_ANNOTATION")
           alignableAnnotation.set("ANNOTATION_ID", "a%d" % documentElementID)
           documentElementID += 1
           alignableAnnotation.set("TIME_SLOT_REF1", "ts%d" % lineNumber)
           alignableAnnotation.set("TIME_SLOT_REF2", "ts%d" % (lineNumber+1))
           annotationValue = SubElement(alignableAnnotation, "ANNOTATION_VALUE")
           annotationValue.text = speechLine
           lineNumber += 1
   if(tierName == "tabDelimitedPhonemes"):
       tier.set("LINGUISTIC_TYPE_REF", "phonemes")
       tier.set("TIER_ID", tierName)
       phonemeLines = [line[tierName] for line in x["lines"]]
       lineNumber = 0
       for phonemeLine in phonemeLines:
           annotation = SubElement(tier, "ANNOTATION")
           refAnnotation = SubElement(annotation, "REF_ANNOTATION")
           refAnnotation.set("ANNOTATION_ID", "a%d" % documentElementID)
           refAnnotation.set("ANNOTATION_REF", "a%d" % (documentElementID - len(speechLines)))
           documentElementID += 1
           annotationValue = SubElement(refAnnotation, "ANNOTATION_VALUE")
           tabDelimitedString = ""
           for i in range(len(phonemeLine) - 1):
               tabDelimitedString += "%s\t" % phonemeLine[i]
           tabDelimitedString += phonemeLine[i]
           #pdb.set_trace()
           annotationValue.text = tabDelimitedString
           lineNumber += 1


linguisticType = SubElement(root, "LINGUISTIC_TYPE")
linguisticType.set("LINGUISTIC_TYPE_ID", "speech")
linguisticType.set("TIME_ALIGNABLE", "true")

linguisticType = SubElement(root, "LINGUISTIC_TYPE")
linguisticType.set("LINGUISTIC_TYPE_ID", "phonemes")
linguisticType.set("TIME_ALIGNABLE", "false")

xmlstr = minidom.parseString(etree.ElementTree.tostring(root)).toprettyxml(indent = "   ")
#print(xmlstr)

xmlFilename = "interim.xml"
xmlFile = open(xmlFilename, "w")
xmlFile.write(xmlstr)
xmlFile.close()
# schema.is_valid(xmlFilename)
# schema.validate(xmlFilename)

