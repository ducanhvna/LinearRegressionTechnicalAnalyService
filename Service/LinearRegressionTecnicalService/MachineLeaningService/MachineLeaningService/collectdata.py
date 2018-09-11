import numpy as np
import math
from MachineLeaningService.preparedata import PrepareData
from datetime import datetime
from sklearn.linear_model import LinearRegression

# Get all racing value from data
def GetStockDataVec(filepath):
    vec = []
    lines = open("Data/"+ filepath+".csv").read().splitlines()
    for line in lines[1:]:
        lineInfo = line.split(",")
        vec.append(lineInfo)

    return vec

# return an n-minute state representation ending at time t
def getState(data, t, n, step, interceptindex, focastindex,closeindex):
    startindex = t-n*step +1

    state1 =[]
    state2 = []
    for i in range(n):
        idx = startindex + step*i
        closedata = float(data[idx][closeindex])
        intercepdata = float(data[idx][interceptindex])
        forcastdata = float(data[idx][focastindex])

        # res.append((curdata - predata))
        normalizeData1 = (intercepdata - closedata)*1000/(closedata)
        normalizeData2 = (forcastdata -closedata)*1000/(closedata)
        state1.append(normalizeData1)
        state2.append(normalizeData2)

    return [state1, state2]

def CollectTraningData(test_data, labels):
    # Load Data from input file
    rawdata = GetStockDataVec(test_data)

    
    # collection 1 is Linear regresstion forcast window size = 5
    # lollection 2 is linear resgrestion intercept with window size = 5
    collection1 = []
    collection2 = []

    # collection 3 is linear regresstion forcast wtih window size = 15
    # collection 4 is linear regresstion intercep with window size = 15
    collection3 = []
    collection4 = []

    # collection 5 is linear regresstion forcast with window size = 50
    # collection 6 is linear regresstion intercept with window size = 50
    collection5 = []
    collection6 = []
    
    #Index array store index of chosen line
    indexs = []

    for i in range(len(rawdata)):
        line = rawdata[i]
        label = line [14]
        if label != "":
            # Store Index
            indexs.append(i)

            # Collect linear regrestion forcast: window = 5, index = 7(size focast 5)
            state = getState(rawdata, i, 10, 1, 7, 6, 4)
            collection1.append(state[0])
           
            collection2.append(state[1])

            # collect linear regresstion forcaset: window = 5 , index = 9 (size forcast = 7)
            state = getState(rawdata, i, 10, 3,10, 9, 8)
            collection3.append(state[0])
           
            collection4.append(state[1])

            # collection linear regresstio forcast window = 5, index = 11 (size forcast = 9
            state = getState(rawdata, i, 10, 5, 13,12,11 )
            collection5.append(state[0])
            collection6.append(state[1])

            #labels
            if label == "OK":
                labels.append(1)
            else:
                labels.append(0)
    return[collection1, collection2, collection3, collection4, collection5, collection6]


