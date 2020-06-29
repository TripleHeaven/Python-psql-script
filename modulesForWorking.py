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
def writeFileToAList(fileName :str, commentLines : int, strictMode : bool, schema, sepa):
    outputDict = dict()
    # intermediate and resultant dictionaries 
    # dict for middle 
    middleDict = {} 
    # resultant dict
    outputDict  = {}  
    namesList = takingNames(schema)
    forLines = commentLines
    
    # considering comment lines
    with open(fileName) as fh: 
            for line in fh:   
                if (forLines >0):
                    argsQuantity = 0
                    forLines -=1
                else:
                    argsQuantity = len (list( line.split(sepa)))   
                    tttest = list(line.split(sepa))
                    nj = 5      
    fields = list()
    forLines = commentLines
    for i in range (argsQuantity):
        if (len (namesList) > 0):
            el = namesList[0]
            namesList.remove(namesList[0])
        fields.append(el)
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
                        description= list( line.strip().split(sepa, argsQuantity))                
                        # for automatic creation of id for line
                        
                        i = 0 
                        middleDict = dict()
                        sno ='line'+str(l) 
                        
                       

                        icheck = fileSizeChecker(schema)
                        dcheck = doubleChecker(schema)
                        while i<len(fields): 
                                # creating dictionary for each line
                                    # this moment needs to be continued
                                    # so first there is a number , if not then we write it as a str type
                                    # and if something happens json validate will check it
                                description[i] = description[i].strip()
                                if (icheck and icheck == i):
                                    middleDict[fields[i]] = longToBytes(description[i])
                                elif (dcheck and dcheck == i):
                                    middleDict[fields[i]] = doubleValidator(description[i].replace(' ','.'))
                                else:
                                    try:
                                        middleDict[fields[i]]= float(( description[i].replace(' ','.')))
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
    convertingSchema(schema)
    print ("Succesfully readed file!")
    return outputDict
#reading a json file into a dictionary for validation check
def readingJsonFile (fileName:str):
    #print("Started Reading JSON file")
    with open(fileName, "r") as read_file:
        #print("Converting JSON encoded data into Python dictionary")
        fileToRead = json.load(read_file)
        # we decoded a json file into a python dictionary
        #for key, value in fileToRead.items():
            #print(key, ":", value)
        #print("Done reading json file")
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
    fields =['type','secondParam'] 
    
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
def takingNames (schemaAdress ):
    namesList = list ()
    with open(schemaAdress) as f:
        schema = json.load(f)
        schemaThing = schema["properties"]
        for key in schemaThing:
            namesList.append(key)
    return namesList        

def writeFileToAListBeta (inputfile:str, commentLines : int, sepa , schema): 
    fileName = csvToTxt(inputfile)
    outputDict = dict()
    # intermediate and resultant dictionaries 
    # dict for middle 
    middleDict = {} 
    # resultant dict
    outputDict  = {}  
    namesList = takingNames(schema)
    forLines = commentLines
        # considering comment lines

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
        el = namesList[0]
        namesList.remove(namesList[0])
        fields.append(el)
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
                        description= list( line.strip().split(sepa, argsQuantity))                
                        # for automatic creation of id for line
                        sno ='line'+str(l) 
                        i = 0 
                        middleDict = dict()
                        
                        icheck = fileSizeChecker(schema)
                        dcheck = doubleChecker(schema)
                        while i<len(fields): 
                                # creating dictionary for each line
                                    # this moment needs to be continued
                                    # so first there is a number , if not then we write it as a str type
                                    # and if something happens json validate will check it
                                description[i] = description[i].strip()
                                if (icheck and icheck == i):
                                    middleDict[fields[i]] = longToBytes(description[i])
                                elif (dcheck and dcheck == i):
                                    middleDict[fields[i]] = doubleValidator(description[i].replace(' ','.'))
                                else:
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
    convertingSchema(schema)
    
    print ("Succesfully readed file!")
    return outputDict
def longToBytes(baseString : str):
    baseString = baseString.replace(" ","")
    baseString = baseString.replace(',','.')
    # removing all spaces in the number
    workingString = baseString
    numberFlag = False
    stringFlag = False
    dotFlag = False
    # string cycle
    numberString = ""
    sizeString = ""

    # error checking
    if (workingString[0].isalpha() and workingString[0] !='.'):
        return -1
    else:
        if (workingString[0]=='.'):
            dotFlag = True
        else:
            numberFlag = True
    for i in range (len(workingString)):
        elIsDot = workingString[i] == '.'
        elementIsAlpha = not elIsDot and workingString[i].isalpha()
        elementIsNumber = workingString[i].isdigit()
        if (elIsDot and dotFlag):
            return -1
        elif (elementIsAlpha and stringFlag):
            return -1 
        elif (elementIsAlpha and not stringFlag):
            sizeString +=workingString[i]
            stringFlag = True
        elif (elementIsNumber):
            numberString += workingString[i]
        elif (not elIsDot):
            numberString += "."
            dotFlag = True
        
        
    
    '''
    "BKMGTP"
    '''
    returnedNumber = float(0)
    if (len (sizeString) == 0):
        returnedNumber = float(numberString)
        returnedValue = str(returnedNumber) + "B"
        return returnedValue
    elif (sizeString=="K"):
        returnedNumber = float(numberString) * 1024
        returnedValue = str(returnedNumber) + "B"
        return returnedValue
    elif (sizeString=="M"):
        returnedNumber = float(numberString) * 1024 * 1024
        returnedValue = str(returnedNumber)+ "B"
        return returnedValue
    elif (sizeString=="G"):
        returnedNumber = float(numberString) * 1024 * 1024 * 1024
        returnedValue = str(returnedNumber)+ "B"
        return returnedValue
    elif (sizeString=="T"):
        returnedNumber = float(numberString) * 1024 * 1024 * 1024 * 1024
        returnedValue = str(returnedNumber)+ "B"
        return returnedValue
    elif (sizeString=="P"):
        returnedNumber = float(numberString) * 1024 * 1024 * 1024  * 1024 * 1024
        returnedValue = str(returnedNumber)+ "B"
        return returnedValue

def fileSizeChecker(schema):
    a = readingJsonFile(schema)
    a = a["properties"]
    # if there is a long in the schema then it return  postition of type long in the schema else it return fals
    i = 0
    for key in a :
        if (a[key]['type'] == "fileSize"):
            return i
        i += 1
def doubleChecker (schema):
    a = readingJsonFile(schema)
    a = a["properties"]
    # if there is a long in the schema then it return  postition of type long in the schema else it return fals
    i = 0
    for key in a :
        if (a[key]['type'] == "double"):
            return i
        i += 1
def doubleValidator (num ):
    #a = ((float(num) * 100) % 1)
    c = float (num)
    a = str(c).replace(',','.')
    l = a.split('.')
    if (len (l[1])<3):
        return float(num)
    else:
        raise Exception('Validation Error')
def convertingSchema(schemaJson):
    with open(schemaJson) as f:
        schema = json.load(f)
        a = schema['properties']
        for key in a: 
            if (a[key]['type'] == 'fileSize'):
                a[key]['type'] = 'string'
            elif (a[key]['type'] == 'float'):
                a[key]['type'] = 'number'
            elif (a[key]['type'] == 'double'):           
                a[key]['type'] = 'number'
        schema["properties"]=a
        out_file = open(schemaJson, "w") 
        json.dump(schema, out_file, indent = 2) 
        out_file.close() 