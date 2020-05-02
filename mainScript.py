from jsonschema import validate
import modulesForWorking as mfw

schema = {    
    "properties" : {
        "firstParam" : {"type" : "number"},
        "secondParam" : {"type" : "number"},
   },
}


# writing a file into json to validate check
#writeToJson("test.txt","test2.json", 2)
#dictar = readingJsonFile('test2.json')
# getting data from a text file
forValidate = mfw.writeFileToAList('test.txt')
# validation Cycle
for key in forValidate:
    print (type(forValidate[key]['firstParam']))
    #validate(instance=forValidate[key], schema=schema)
