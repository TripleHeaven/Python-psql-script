from jsonschema import validate
import modulesForWorking as mfw
import json
import sys




# Get information from user
#writtenFile = sys.argv[1]
#schemaJson = sys.argv[2]
#commentLines = int(sys.argv[3])
#strictMode = sys.argv[3]
#commentLines = sys.argv[4]
# writing a file into json to validate check
#writeToJson("test.txt","test2.json", 2)
#dictar = readingJsonFile('test2.json')


#forDebug
#writtenFile = './files/test.txt'
schemaJson = './schemes/schemaReal2.json'


# getting data from a text file
#forValidate = mfw.writeFileToAList(writtenFile, 1 , 1)
# validation Cycle



# getting data from a csv file

#forValidate = mfw.writeFileToAListFromCsv('./files/run2_log.csv')



#forValidate = mfw.writeFileToAListBeta('./files/run2_log.csv',0,';','./schemes/schemaReal2.json')
'''
forValidate = mfw.writeFileToAList('./files/run2_log.csvCONVERTED',0,';',"./schemes/schemaReal2.json",';')
# parsing a txt file
#######
with open(schemaJson) as f:
  schema = json.load(f)
  print (schema)
for key in forValidate:  
    validate(instance=forValidate[key], schema=schema)
#print (forValidate)
print ("File Succesfully readed!")
#######
'''

# parsing the csv file
#print (mfw.writeFileToAListFromCsv('./files/run2_log.csv'))


#checking = mfw.readingJsonFile("./schemes/schemaReal1.json")
#properties = checking['properties']

#print (properties)
# print (mfw.readingJsonFile("./schemes/schemaReal1.json")["properties"]["1"]["type"])



forV1 = mfw.writeFileToAListBeta('./files/run2_log.csv',1,';','./schemes/schemaReal2.json')
with open(schemaJson) as f:
  schema = json.load(f)
  print (schema)
for key in forV1:  
    validate(instance=forV1[key], schema=schema)
#print (forValidate)
print ("File Succesfully readed!")
