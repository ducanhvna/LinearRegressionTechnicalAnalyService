# import lib
import numpy as np
import math
from MachineLeaningService.datacollect import GetStockDataVec
from MachineLeaningService.datacollect import PrepareData, PrepareDataWithReport, FindLocationinData, GetInputState
import csv
from datetime import datetime

# Assign lable to data
def AssignLableToData(investorLog):
    for i in range(1,len(investorLog)-2):
        data = investorLog[i]
        if investorLog[i+1][3] <= 0:
            investorLog[i].append('NG')
        else:
            investorLog[i].append('OK')

# data = PrepareData("fromJSON_1minute","fromJSON_3minute","fromJSON_5minute","Data09062018")
# result after prepare = [rawdata, rawdata1, rawdata3, investorLog]
def CreateTrainingSet(labels):
    element1 = []
    element2 = []
    element3 = []
    element4 = []
    element5 = []
    element0 = []
    data = PrepareDataWithReport("5","15","3","Data09072018")
    
    investorLog = data[3]
    AssignLableToData(investorLog)
    
    # Test Get Test data
    for i in range(8, len(investorLog)-1):
        line = investorLog[i]
        # find index
        datetimeObject = datetime.strptime(line[0], '%d/%m/%Y %H:%M:%S')
        index = FindLocationinData(data[0], datetimeObject)
    
        # Get State
        State = GetInputState(index, data[0], data[1], data[2], 15, 15, 15)
        if len(State[0]) >0 and len(State[0]) >0 and len(State[2]) >0 and len(line) == 5:
            element0.append(State[0][0])
            element1.append(State[0][1])
            element2.append(State[1][0])
            element3.append(State[1][1])
            element4.append(State[2][0])
            element5.append(State[2][1])
            
            if line[4]== 'NG' :
                labels.append(0)
            else:
                labels.append(1)

    with open("Data09112018/label.csv","w+") as my_csv:   
        csvWriter = csv.writer(my_csv, delimiter=',')  # using the csv module to write the file
        csvWriter.writerows(investorLog)
    
    return [element0, element1, element2, element3, element4, element5]

def CreateTestSet(indexs, fromIndex):
    element1 = []
    element2 = []
    element3 = []
    element4 = []
    element5 = []
    element0 = []
    
    data = PrepareDataWithReport("5","15","3","Data09112018")
    
    investorLog = data[3]
    
    # Test Get Test data
    for i in range(fromIndex, len(investorLog)-1):
        line = investorLog[i]
        # find index
        datetimeObject = datetime.strptime(line[0], '%d/%m/%Y %H:%M:%S')
        index = FindLocationinData(data[0], datetimeObject)
    
        # Get State
        State = GetInputState(index, data[0], data[1], data[2], 15, 15, 15)
        if len(State[0]) >0 and len(State[0]) >0 and len(State[2]) >0:
            element0.append(State[0][0])
            element1.append(State[0][1])
            element2.append(State[1][0])
            element3.append(State[1][1])
            element4.append(State[2][0])
            element5.append(State[2][1])
            investorLog[i].append(data[0][index][0])
            indexs.append(index)

    with open("Data09112018/label.csv","w+") as my_csv:   
        csvWriter = csv.writer(my_csv, delimiter=',')  # using the csv module to write the file
        csvWriter.writerows(investorLog)
    
    return [element0, element1, element2, element3, element4, element5, investorLog]

# np.savetxt('text.txt',data,fmt='%.5f',delimiter=',')
#with open("filename2.csv","w+") as my_csv:   
#    csvWriter = csv.writer(my_csv, delimiter=',')  # using the csv module to write the file
#    csvWriter.writerows(data)

def CreateTestSet(indexs, fromIndex):
    element1 = []
    element2 = []
    element3 = []
    element4 = []
    element5 = []
    element0 = []
    
    data = PrepareDataWithReport("5","15","3","Data09072018")
    
    investorLog = data[3]
    
    # Test Get Test data
    for i in range(fromIndex, len(investorLog)-1):
        line = investorLog[i]
        # find index
        datetimeObject = datetime.strptime(line[0], '%d/%m/%Y %H:%M:%S')
        index = FindLocationinData(data[0], datetimeObject)
    
        # Get State
        State = GetInputState(index, data[0], data[1], data[2], 15, 15, 15)
        if len(State[0]) >0 and len(State[0]) >0 and len(State[2]) >0:
            element0.append(State[0][0])
            element1.append(State[0][1])
            element2.append(State[1][0])
            element3.append(State[1][1])
            element4.append(State[2][0])
            element5.append(State[2][1])
            investorLog[i].append(data[0][index][0])
            indexs.append(index)

    with open("Data09112018/label.csv","w+") as my_csv:   
        csvWriter = csv.writer(my_csv, delimiter=',')  # using the csv module to write the file
        csvWriter.writerows(investorLog)
    
    return [element0, element1, element2, element3, element4, element5, investorLog]

# np.savetxt('text.txt',data,fmt='%.5f',delimiter=',')
#with open("filename2.csv","w+") as my_csv:   
#    csvWriter = csv.writer(my_csv, delimiter=',')  # using the csv module to write the file
#    csvWriter.writerows(data)
