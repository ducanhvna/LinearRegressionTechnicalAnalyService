import numpy as np
# Normalize data
def Normalize(standard, value):
    result = (float(value) - float(standard))*1000/float(standard)
    return result

# LinearRegressionCalculate
def LinearRegressionCalculate(x_train, y_train):
    a,b = np.polyfit(x_train,y_train,1)
    forcast = a*len(x_train)+b

    return a,b,forcast

# Time series data 
def TimeSeriesLinearRegression(rawdata, windowsize, index):
    x_train= []
    y_train = []
    result = []
    if index > windowsize-2:
        #Create x train from 0 to windowsize
        for i in range(0, windowsize):
            x_train.append(i)
            value = float(rawdata[index - windowsize + i + 1][4])
            y_train.append(value)
        lrvalue = LinearRegressionCalculate(x_train, y_train)
        return lrvalue
    else:
        return '','',''

# Find location in rawdata by time
def FindLocationbyTime(rawdata, datetime):
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