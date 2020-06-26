from jsonschema import validate
import modulesForWorking as mfw
import json
import sys


# for debug 

fileName = sys.argv[1]
fileType = fileName [-3:]
schemaAdress = sys.argv[2]

# typeFile 
'''
fileType = fileName[-3:]
schemaAdress = sys.argv[2]

#Info from user


fileName = sys.argv[1]

# typeFile 

fileType = fileName[-3:]
schemaAdress = sys.argv[2]

'''
with open(schemaAdress) as f:
  schema = json.load(f)
  sepa = schema['separator']['sep']
  commentLines = schema['commentLines']['quant']

if (fileType == "txt"):
  forValidate = mfw.writeFileToAList(fileName,commentLines,1,schemaAdress,sepa)
elif (fileType == "csv"):
  forValidate = mfw.writeFileToAListBeta(fileName,commentLines,sepa,schemaAdress)



# parsing a txt file
#######
with open(schemaAdress) as f:
  schema = json.load(f)
for key in forValidate:  
    validate(instance=forValidate[key], schema=schema)
print (forValidate)
print ("File Succesfully readed!")