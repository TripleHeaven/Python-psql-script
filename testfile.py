import json
import random
import jsonschema
from jsonschema import validate

structureSchema ="""{
    "type" = "object",
}
"""

def makingFile(stringsCount : int, fileName : str):
    '''
    1. how much strings generaate
    2. name of file created 
    '''
    file = open(fileName,'w')
    for i in range (stringsCount):
            file.write(str(random.randint(1,100))+' '+str(round(random.uniform(1.1,99.9),2)) + "\n")
    file.close()

def fileToJson (fileName: str):
        # Python program to convert text 
    # file to JSON 
    # the file to be converted 
    filename = fileName
    
    # intermediate and resultant dictionaries 
    # intermediate 
    dict2 = {} 
    
    # resultant 
    dict1 = {} 
    
    # fields in the sample file  
    fields =['firstNum','secondNum'] 
    
    with open(filename) as fh: 
        
        # loop variable 
        i = 0
        
        # count variable for employee id creation 
        l = 1
        
        for line in fh:          
            # reading line by line from the text file 
            description = list( line.strip().split(None, 2)) 
            
            # for output see below 
            print(description)  
            
            # for automatic creation of id for each employee 
            sno ='strNum'+str(l) 
        
            while i<len(fields): 
                
                    # creating dictionary for each string
                    dict2[fields[i]]= description[i] 
                    i = i + 1
                    
            # appending the record of each string to 
            # the main dictionary 
            dict1[sno]= dict2 
            l = l + 1
    # creating json file         
    out_file = open("test2.json", "w") 
    json.dump(dict1, out_file, indent = 2) 
    out_file.close() 

def readingJsonFile (fileName:str):
    print("Started Reading JSON file")
    with open(fileName, "r") as read_file:
        print("Converting JSON encoded data into Python dictionary")
        fileToRead = json.load(read_file)

        print("Decoded JSON Data From File")
        for key, value in fileToRead.items():
            print(key, ":", value)
        print("Done reading json file")
        return fileToRead
#makingFile(5,'test.txt')
fileToJson('test.txt')
dictFromJson  = readingJsonFile('test2.json')
#testing dump
print(dictFromJson['strNum1'])


