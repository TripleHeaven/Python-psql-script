from jsonschema import validate
import modulesForWorking as mfw
import json
import sys

# Get information from user
writtenFile = sys.argv[1]
schemaJson = sys.argv[2]
# writing a file into json to validate check
#writeToJson("test.txt","test2.json", 2)
#dictar = readingJsonFile('test2.json')
# getting data from a text file
forValidate = mfw.writeFileToAList(writtenFile)
# validation Cycle
with open(schemaJson) as f:
  schema = json.load(f)
for key in forValidate:   
    validate(instance=forValidate[key], schema=schema)
print (forValidate)
