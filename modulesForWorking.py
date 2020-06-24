import random
import json 
import pandas as pd
import csv
def csvToTxt(input):
    csv_file = input
    txt_file = input+ 'CONVERTED'
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()
    return txt_file
def makingFile(stringsCount : int, fileName : str):
    '''
    1. how much strings generaate
    2. name of file created 
    '''
    file = open(fileName,'w')
    for i in range (stringsCount):
            file.write(str(random.randint(1,100))+' '+str(round(random.uniform(1.1,99.9),2)) + "\n")
    file.close()
def writeFileToAListFromCsv (fileName:str):
    
    data = pd.read_csv('./files/run2_log.csv', sep = ';').to_dict()
    print (data)
    print (type(data))
    return data
def writeFileToAList(fileName :str, commentLines : int, strictMode : bool):
    outputDict = dict()
    # intermediate and resultant dictionaries 
    # dict for middle 
    middleDict = {} 
    # resultant dict
    outputDict  = {}  

    forLines = commentLines
    
    with open(fileName) as fh: 
            for line in fh:   
                if (forLines >0):
                    argsQuantity = 0
                    forLines -=1
                else:
                    argsQuantity = len (list( line.split()))            
    fields = list()
    forLines = commentLines
    for i in range (argsQuantity):
         fields.append(str(i+1))
    with open(fileName) as fh:
            # line number 
            lineNumber = 1
            # loop variable 
            i = 0 
            # count variable for dict
            l = 1          
            for line in fh:  
                if (forLines > 0 ): 
                    m = 0 
                    forLines -=1
                    lineNumber +=1
                else:             
                        # reading line by line from the text file 
                        description= list( line.strip().split(None, argsQuantity))                
                        # for automatic creation of id for line
                        sno ='line'+str(l) 
                        i = 0 
                        middleDict = dict()
                        while i<len(fields): 
                                # creating dictionary for each line
                                    # this moment needs to be continued
                                    # so first there is a number , if not then we write it as a str type
                                    # and if something happens json validate will check it
                                try:
                                    middleDict[fields[i]]= float(description[i])
                                except ValueError:
                                    middleDict[fields[i]]= str(description[i])
                                except IndexError:
                                    a=50    
                                #    print ('One of the arguments is missing! In Line ',lineNumber)
                                #    if (strictMode==1):
                                #        raise SystemExit
                                i = i + 1
                                
                        # appending the record of each line to 
                        # the main dictionary 
                        outputDict[sno]= middleDict 
                        l = l + 1
                        lineNumber +=1
    print ("Succesfully readed file!")
    return outputDict
#reading a json file into a dictionary for validation check
def readingJsonFile (fileName:str):
    print("Started Reading JSON file")
    with open(fileName, "r") as read_file:
        print("Converting JSON encoded data into Python dictionary")
        fileToRead = json.load(read_file)
        # we decoded a json file into a python dictionary
        for key, value in fileToRead.items():
            print(key, ":", value)
        print("Done reading json file")
        return fileToRead
# Python program to convert text 
# file to JSON 
def writeToJson(fileToWrite: str, fileWhichToWrite: str, elemsInLine: int):


    '''
    create a json file of text file 
    UsesForValidationCheck
    '''
    # the file to be converted 
    filename = fileToWrite
    
    # intermediate and resultant dictionaries 
    # intermediate 
    dict2 = {} 
    
    # resultant 
    dict1 = {} 
    
    # fields in the sample file  
    fields =['firstParam','secondParam'] 
    
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
            sno ='line'+str(l) 
            i = 0 
            dict2 = dict()
            while i<len(fields): 
                
                    # creating dictionary for each employee 
                    dict2[fields[i]]= description[i] 
                    i = i + 1
                    
            # appending the record of each employee to 
            # the main dictionary 
            print (dict2)
            dict1[sno]= dict2 
            
            l = l + 1
    # creating json file         
    out_file = open(fileWhichToWrite, "w") 
    json.dump(dict1, out_file, indent = 2) 
    out_file.close() 
def writeFileToAListBeta (inputfile:str, commentLines : int, sepa): 
    fileName = csvToTxt(inputfile)
    outputDict = dict()
    # intermediate and resultant dictionaries 
    # dict for middle 
    middleDict = {} 
    # resultant dict
    outputDict  = {}  

    forLines = commentLines
    
    with open(fileName) as fh: 
            for line in fh:   
                if (forLines >0):
                    argsQuantity = 0
                    forLines -=1
                else:
                    argsQuantity = len (list( line.split(sepa)))            
    fields = list()
    forLines = commentLines
    for i in range (argsQuantity):
         fields.append(str(i+1))
    with open(fileName) as fh:
            # line number 
            lineNumber = 1
            # loop variable 
            i = 0 
            # count variable for dict
            l = 1          
            for line in fh:  
                if (forLines > 0 ): 
                    m = 0 
                    forLines -=1
                    lineNumber +=1
                else:             
                        # reading line by line from the text file 
                        description= list(line.strip().split(sepa, argsQuantity))                
                        # for automatic creation of id for line
                        sno ='line'+str(l) 
                        i = 0 
                        middleDict = dict()
                        while i<len(fields): 
                                # creating dictionary for each line
                                    # this moment needs to be continued
                                    # so first there is a number , if not then we write it as a str type
                                    # and if something happens json validate will check it
                                try:
                                    middleDict[fields[i]]= float(description[i].replace(' ','.'))
                                except ValueError:
                                    middleDict[fields[i]]= str(description[i])
                                except IndexError:
                                    a=50    
                                #    print ('One of the arguments is missing! In Line ',lineNumber)
                                #    if (strictMode==1):
                                #        raise SystemExit
                                i = i + 1
                                
                        # appending the record of each line to 
                        # the main dictionary 
                        outputDict[sno]= middleDict 
                        l = l + 1
                        lineNumber +=1
    print ("Succesfully readed file!")
    print (outputDict)
    return outputDict
