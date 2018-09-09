from functions import FindLocationbyTime, TimeSeriesLinearRegression
from datetime import datetime

# Get data from file
def GetStockDataVec(filepath):
    vec = []
    lines = open("Data/"+ filepath+".csv").read().splitlines()
    for line in lines[1:]:
        lineInfo = line.split(",")
        vec.append(lineInfo)
    return vec

# Input are all file with time period 1,3,5,10
# output is array of data
def CollectAllRawData(rawdata_1, rawdata_5, rawdata_10, rawdata_20):
    data_1 = GetStockDataVec(rawdata_1)
    data_5 = GetStockDataVec(rawdata_5)
    data_10= GetStockDataVec(rawdata_10)
    data_20= GetStockDataVec(rawdata_20)

    return data_1,data_5,data_10,data_20

# calculate linear regresstion at this postion rawdata_5 and coressponding in rawdata_10
def CollectTrainData(rawdata_5, rawdata_10, windowsize):
    # linear regression array period 5 minitue
    lrarray_5 = []

    # Coressponding linear regression arry period 10 minute
    lrarray_10 = []
    for i in range(0, len(rawdata_5)):
        a,b,forcast = TimeSeriesLinearRegression(rawdata_5, windowsize, i)
        lrarray_5.append([a,b,forcast])

        # find coresponding index
        datetimestring = rawdata_5[i][0]
        datetimeObject = datetime.strptime(datetimestring, '%d/%m/%Y %H:%M:%S')
        co_index_10 = FindLocationbyTime(rawdata_10, datetimeObject)
        a,b,forcast  = TimeSeriesLinearRegression(rawdata_10, windowsize, co_index_10)
        lrarray_10.append([a,b,forcast])
    return lrarray_5, lrarray_10

# List all cadidate point
def ListCandidatePoint(rawdata_5, lrarray_5):
    candidatevalues = []
    candidatedecision = []
    for i in range(0, len(rawdata_5)):
        if i>1 :
            a, b, forcast = lrarray_5[i]
            prea, preb, prefocast = lrarray_5[i-1]
            if  prea=='':
                candidatevalues.append(False)
                candidatedecision.append('')
            elif float(prea) == 0 and float(a)!=0:
                candidatevalues .append(True)
                if float(a)<0:
                    # Sell
                    candidatedecision.append(True)
                else:
                    #buy
                    candidatedecision.append(False)

            else:
                if float(prea)*float(a)<0:
                    candidatevalues.append(True)
                    if float(a)<0:
                        # Sell
                        candidatedecision.append(True)
                    else:
                        #buy
                        candidatedecision.append(False)
                else:
                    candidatevalues.append(False)
                    candidatedecision.append('')
        else:
            candidatevalues.append(False)
            candidatedecision.append('')

    return  candidatevalues, candidatedecision


