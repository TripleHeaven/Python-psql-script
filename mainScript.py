from jsonschema import validate
import modulesForWorking as mfw
import json
import sys




# Get information from user
#writtenFile = sys.argv[1]
#schemaJson = sys.argv[2]
#strictMode = sys.argv[3]
#commentLines = sys.argv[4]
# writing a file into json to validate check
#writeToJson("test.txt","test2.json", 2)
#dictar = readingJsonFile('test2.json')


#forDebug
writtenFile = './files/test.txt'
schemaJson = './schemes/schema1.json'
commentLines = 2

# getting data from a text file
forValidate = mfw.writeFileToAList(writtenFile, commentLines , 1)
# validation Cycle

with open(schemaJson) as f:
  schema = json.load(f)
for key in forValidate:  
    validate(instance=forValidate[key], schema=schema)
print (forValidate)

#checking = mfw.readingJsonFile("./schemes/schemaReal1.json")
#properties = checking['properties']

#print (properties)
# print (mfw.readingJsonFile("./schemes/schemaReal1.json")["properties"]["1"]["type"])