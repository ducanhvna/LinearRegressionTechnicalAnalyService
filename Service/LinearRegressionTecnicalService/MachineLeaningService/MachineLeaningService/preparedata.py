import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# from functions import GetStockDataVec
from datetime import datetime
import csv

def CalLinearRegresstion(x_train, y_train):
    # explore our dataset a bit, to do so
    #dataset.shape
    #x = dataset.iloc[:, :-1].value
    #y = dataset.iloc[:, 1].value
    
    # x_train, x_test, y_train, y_test = train_test_split(x_train, y_train ,test_size = 0, random_state = 0)
    regressor = LinearRegression()
    # regressor.fit([ x_train], [y_train])
    a,b= np.polyfit(x_train, y_train, 1)
    
    return [a * x_train[len(x_train)-1] + b ,b]

def CalLinearRegression(rawdata, windowsize, index):
    if index >= windowsize -2:
        xtrain = []
        for j in range(0, windowsize-1):
            xtrain.append(j)
        ytrain = getSubState(rawdata, index, windowsize, 4)
        # print (xtrain)
        # print (ytrain)
        result = CalLinearRegresstion(xtrain, ytrain)
        return result
    else:
        return [-1,-1]


def getSubState(data, t, n, index):
    d= t-n+1
    block = data[d: t+1] if d>= 0 else -d * [data[0]] + data[0 : t+1] #path with t0
    res = []
    for i in range(n-1):
        curdata = float(block[i+1][index])
        res.append(curdata)

    return res

# define a method to load data from input and write output to output File
# output data : linear regression in window 5, 15, 50
def PrepareData(inputPath, inputPath2, inputPath3, outputPath):
    # Load Data from input file
    rawdata = GetStockDataVec(inputPath)
   

    # Load Input 2 time = 3
    rawdata2 = GetStockDataVec(inputPath2)


    # Load input 3 time = 5
    rawdata3 = GetStockDataVec(inputPath3)


   # print(rawdata)
    # Calculate linear regresstion value in window 15, write to column 7,8
    for i in range(0,len(rawdata)):
        vec = rawdata[i]

        linearforcast1minute_frame = CalLinearRegression(rawdata, 15, i)
        vec.append(linearforcast1minute_frame[0])
        vec.append(linearforcast1minute_frame[1])

        datetimeObject = datetime.strptime(vec[0], '%d/%m/%Y %H:%M:%S')
        # Calculate value in frame 3 minute
        timeframe3miniteIndex = FindLocationinData(rawdata2, datetimeObject)
        linearforcast3minute_frame = CalLinearRegression(rawdata2,15, timeframe3miniteIndex)
        vec.append(rawdata2[timeframe3miniteIndex][4])
        vec.append(linearforcast3minute_frame[0])
        vec.append(linearforcast3minute_frame[1])

        # Calculate value in frame 5 minute
        timeframe5minuteIndex = FindLocationinData(rawdata3, datetimeObject)
        linearforcast5minute_frame = CalLinearRegression(rawdata3,15, timeframe5minuteIndex)
        vec.append(rawdata3[timeframe5minuteIndex][4])
        vec.append(linearforcast5minute_frame[0])
        vec.append(linearforcast5minute_frame[1])

    with open(outputPath + "/rawdata.csv","w+") as my_csv:   
        csvWriter = csv.writer(my_csv, delimiter=',')  # using the csv module to write the file
        csvWriter.writerows(rawdata)

    # print(rawdata)
    return rawdata

def PrepareDataWithReport(inputPath, inputPath1, inputPath3, outputPath):
    # Load Data from input file
    rawdata = GetStockDataVec(inputPath)
    focuslist = rawdata.copy()
    investorLog = ExportDataCollected(focuslist, outputPath, inputPath+"_minutereport")

    # Load Input 2 time = 3
    rawdata1 = GetStockDataVec(inputPath1)
    newlist = rawdata1.copy()
    ExportDataCollected(newlist, outputPath, inputPath1+ "_minutereport")

    # Load input 3 time = 5
    rawdata3 = GetStockDataVec(inputPath3)
    newlist = rawdata3.copy()
    ExportDataCollected(newlist, outputPath, inputPath3+ "_minutereport")

   ## print(rawdata)
   # # Calculate linear regresstion value in window 15, write to column 7,8
   # for i in range(0,len(rawdata)):
   #     vec = rawdata[i]

   #     linearforcast1minute_frame = CalLinearRegression(rawdata, 15, i)
   #     vec.append(linearforcast1minute_frame[0])
   #     vec.append(linearforcast1minute_frame[1])

   #     datetimeObject = datetime.strptime(vec[0], '%d/%m/%Y %H:%M:%S')
   #     # Calculate value in frame 3 minute
   #     timeframe3miniteIndex = FindLocationinData(rawdata2, datetimeObject)
   #     linearforcast3minute_frame = CalLinearRegression(rawdata2,15, timeframe3miniteIndex)
   #     vec.append(rawdata2[timeframe3miniteIndex][4])
   #     vec.append(linearforcast3minute_frame[0])
   #     vec.append(linearforcast3minute_frame[1])

   #     # Calculate value in frame 5 minute
   #     timeframe5minuteIndex = FindLocationinData(rawdata3, datetimeObject)
   #     linearforcast5minute_frame = CalLinearRegression(rawdata3,15, timeframe5minuteIndex)
   #     vec.append(rawdata3[timeframe5minuteIndex][4])
   #     vec.append(linearforcast5minute_frame[0])
   #     vec.append(linearforcast5minute_frame[1])


    # print(rawdata)
    return [rawdata, rawdata1, rawdata3, investorLog]

# Get the data state with state index refer value in rawdata1 and rawdata 3
# Infomation: data in rawdata: window size  = timeperiod
# Infomation: data in rawdata1: window size = timeperiod1
# Infomation: data in rawdata2: window size = timeperiod2
def GetInputState(stateindex, rawdata,rawdata1, rawdata3, timeperiod, timeperiod1, timeperiod3):
    #Initialize result element
    # element 1 is forcast and intercept in rawdata1 with windowsize = timeperiod 1
    element1 = []

    # element 3 is forcast and intercept in rawdata=3 with windowsize = timeperiod 3
    element3 = []

    # element is forcast and intercpet values rawdata with windowsize = timeperiod
    element = []

    # Validate
    if stateindex >= len(rawdata):
        return []
    # Get line from rawdata
    dataline = rawdata[stateindex]

    # Get date time selected
    datetimeSelect = datetime.strptime (dataline[0], '%d/%m/%Y %H:%M:%S')

    # Get state in rawdata
    element = GetStateinRawData(rawdata, stateindex, timeperiod)

    # find location in data 1
    location1 = FindLocationinData(rawdata1, datetimeSelect)

    # Get state in raw data 1
    element1 = GetStateinRawData(rawdata1, location1, timeperiod1)

    # find location in data 3
    location3 = FindLocationinData(rawdata3, datetimeSelect)

    # Get state in data3
    element3 = GetStateinRawData(rawdata3, location3, timeperiod3)

    return [element, element1, element3]

# result is 2 demension array 
# forcast array is all forcast data of from timeperiod
def GetStateinRawData(rawdata, stateindex, timeperiod):
    forcastArray = []
    interceptArray = []
    if(stateindex - timeperiod < - 1): 
        return []
    startIndex = stateindex -timeperiod +1
    for i in range(startIndex, stateindex+1):
        # Calculate LinearRegression
        lrvalue = CalLinearRegression(rawdata, 15, i)
        focastValue = lrvalue[0]
        interceptValue = lrvalue[0]
        closeValue = rawdata[i][4]

        forcastArray.append((float(focastValue)- float(closeValue))*1000/ float(closeValue))
        interceptArray.append((float(interceptValue)- float(closeValue))*1000/float(closeValue))

    return [forcastArray, interceptArray]

# Export Data to file
def ExportDataCollected(rawdata, outputPath, outputFile):
    # Calculate linear regresstion value in raw data
    
    for i in range(0, len(rawdata)):
        vec = rawdata[i]
        linearregression = CalLinearRegression(rawdata, 15, i)
        forcastValue = linearregression[0]
        interceptValue = linearregression[1]
        vec.append(forcastValue)
        vec.append(interceptValue)
        # Check the trend 

        if i>13:
            # check focast value more than intercept value
            preStatement =  rawdata[i-1][6] > rawdata[i-1][7]
            # Get current state
            currentStatement = forcastValue > interceptValue
            # check if the statement change
            if preStatement != currentStatement:
                vec.append(True)
                if(currentStatement == True):
                    vec.append('BUY')
                else:
                    vec.append('CELL')
            else:
                vec.append(False)
        else:
            vec.append(False)

    resultfile = outputPath + "/" + outputFile + '_investor_2018_9_5_full'
    # ReportOneDay(rawdata,2018, 9, 5,resultfile)
    investorLog =  ReportFull(rawdata, resultfile)

    with open(outputPath+"/"+ outputFile + ".csv","w+") as my_csv:   
        csvWriter = csv.writer(my_csv, delimiter=',')  # using the csv module to write the file
        csvWriter.writerows(rawdata)
    return investorLog

def FindLocationinData(rawdata, datetime):
    for i in range(0, len(rawdata)):
        data = rawdata[i]
        datatime = datetime.strptime(data[0], '%d/%m/%Y %H:%M:%S')
        if i == len(rawdata)-1:
            return i
        elif datetime == datatime:
            return i
        elif datatime> datetime:
            return i-1
        
    return -1




def GetStockDataVec(filepath):
    vec = []
    lines = open("Data/"+ filepath+".csv").read().splitlines()
    for line in lines[1:]:
        lineInfo = line.split(",")
        vec.append(lineInfo)
    return vec

def ReportOneDay(data ,year, moth, day, outputFile):
    investorLog=[['DataTime', 'Price', 'Action', 'Profit']]
    investor = []
    totalProfit = 0

    for i in range(0, len(data)):
        datatime = datetime.strptime(data[i][0], '%d/%m/%Y %H:%M:%S')
        timetuple = datatime.timetuple()
        if timetuple[0] == year and timetuple[1] == moth and timetuple[2] == day and len(data[i])==10:
            if data[i][9] == 'CELL':
                buyprice = investor.pop()
                profit = float(data[i][4]) - float(buyprice)
                data[i].append(profit)
                totalProfit += profit
                investorLog.append([data[i][0], data[i][4], 'CELL', profit])
            elif data[i][9] =='BUY':
                investor.append(data[i][4])
                investorLog.append([data[i][0], data[i][4], 'BUY'])
    
    investorLog.append(['Total Profit:', totalProfit])
    with open(outputFile + ".csv","w+") as my_csv:   
        csvWriter = csv.writer(my_csv, delimiter=',')  # using the csv module to write the file
        csvWriter.writerows(investorLog)
    return investorLog

def ReportFull(data , outputFile):
    investorLog=[['DataTime', 'Price', 'Action', 'Profit']]
    investor = []
    seller = []
    totalProfit = 0

    for i in range(0, len(data)):
        datatime = datetime.strptime(data[i][0], '%d/%m/%Y %H:%M:%S')
        timetuple = datatime.timetuple()
        if len(data[i])==10:
            profit = 0
            if data[i][9] == 'CELL':
                seller.append(data[i][4])
                if len(investor) > 0:
                    buyprice = investor.pop()
                    profit = float(data[i][4]) - float(buyprice)
                    data[i].append(profit)
                totalProfit += profit
                investorLog.append([data[i][0], data[i][4], 'SELL', profit])

            elif data[i][9] =='BUY':
                if len(seller) > 0:
                    sellprice = seller.pop()
                    profit = float(sellprice) - float(data[i][4])
                    data[i].append(profit)

                totalProfit += profit
                investor.append(data[i][4])
                investorLog.append([data[i][0], data[i][4], 'BUY', profit])
    
    investorLog.append(['Total Profit:', totalProfit])
    with open(outputFile + ".csv","w+") as my_csv:   
        csvWriter = csv.writer(my_csv, delimiter=',')  # using the csv module to write the file
        csvWriter.writerows(investorLog)
    return investorLog
