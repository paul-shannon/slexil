import yaml
import csv
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, dump
from xml.dom import minidom
import datetime
import xml.etree as etree
import xmlschema
# https://www.mpi.nl/tools/elan/EAF_Annotation_Format_3.0_and_ELAN.pdf
schemaXSD = "http://www.mpi.nl/tools/elan/EAFv3.0.xsd"
schema = xmlschema.XMLSchema(schemaXSD)


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
for i in range(len(startTimes)):
    timeSlot  = SubElement(timeOrder, "TIME_SLOT")
    timeSlot.set("TIME_SLOT_ID", "ts%d" % i)
    timeSlot.set("TIME_VALUE", "%d" % startTimes[i])

lineFieldNames = list(x["lines"][0].keys())
tierNames = lineFieldNames[1:]
for tierName in tierNames:
   tier = SubElement(root, "TIER")
   tier.set("DEFAULT_LOCALE", "tr")   # not sure what "tr" means
   if(tierName.lower().find("speech") >= 0):
       tier.set("LINGUISTIC_TYPE_REF", "speech")
       tier.set("TIER_ID", tierName)
       speechLines = [line[tierName] for line in x["lines"]]
       lineNumber = 1
       for speechLine in speechLines:
           annotation = SubElement(tier, "ANNOTATION")
           alignableAnnotation = SubElement(annotation, "ALIGNABLE_ANNOTATION")
           alignableAnnotation.set("ANNOTATION_ID", "a%d" % lineNumber)
           alignableAnnotation.set("TIME_SLOT_REF1", "ts%d" % lineNumber)
           alignableAnnotation.set("TIME_SLOT_REF2", "ts%d" % (lineNumber+1))
           annotationValue = SubElement(alignableAnnotation, "ANNOTATION_VALUE")
           annotation.text = speechLine


xmlstr = minidom.parseString(etree.ElementTree.tostring(root)).toprettyxml(indent = "   ")
#print(xmlstr)

xmlFilename = "interim.xml"
xmlFile = open(xmlFilename, "w")
xmlFile.write(xmlstr)
xmlFile.close()
validXML = schema.is_valid(xmlFilename)
schema.validate(xmlFilename)
print("valid against schema? %s" % schema.is_valid(xmlFilename))

