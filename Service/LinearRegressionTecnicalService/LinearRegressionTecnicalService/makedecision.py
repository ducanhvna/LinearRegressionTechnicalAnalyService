from datetime import datetime
import csv

# assign label
def makedecisionbyEvaluate(data, lrvalues, evaluatevalues):

    return

def SplitCandidateData(data, candidatevalues, candidatedecision):
    result = []
    decistion = []
    for i in range(0, len(candidatevalues)):
        candidateValue = candidatevalues[i]
        if candidateValue == True:
            outdata = [i,data[i]]
            result.append(outdata)
            decistion.append(candidatedecision[i])
    return result, decistion

def CalculateProfit(dataarray, decisions, outputFile):
    investorLog=[['DataTime', 'Price', 'Action', 'Profit']]
    investor = []
    seller = []
    totalProfit = 0
    profitarray = [0]
    for i in range(0, len(decisions)):
        datatime = datetime.strptime(dataarray[i][1][0], '%d/%m/%Y %H:%M:%S')
        timetuple = datatime.timetuple()
        profit = 0
        if decisions[i] == True:
            seller.append(dataarray[i][1][4])
            if len(investor) > 0:
                buyprice = investor.pop()
                profit = float(dataarray[i][1][4]) - float(buyprice)
                profitarray.append(profit)
            totalProfit += profit
            investorLog.append([dataarray[i][1][0], dataarray[i][1][4], 'SELL', profit])

        elif decisions[i] == False:
            if len(seller) > 0:
                sellprice = seller.pop()
                profit = float(sellprice) - float(dataarray[i][1][4])
                profitarray.append(profit)

            totalProfit += profit
            investor.append(dataarray[i][1][4])
            investorLog.append([dataarray[i][1][0], dataarray[i][1][4], 'BUY', profit])
    
    investorLog.append(['Total Profit:', totalProfit])
    with open(outputFile + ".csv","w+") as my_csv:   
        csvWriter = csv.writer(my_csv, delimiter=',')  # using the csv module to write the file
        csvWriter.writerows(investorLog)
    return investorLog, profitarray

# Assign labble True false
def AssignLabel(profitarray):
    result = []
    for i in range(0, len(profitarray) -1):
        nextprofit = profitarray[i + 1]
        if nextprofit < 0:
            result.append(False)
        else:
            result.append(True)
    result.append('')
    return result


def CalculateProfitByLabel(dataarray, labels, decisions, outputFile):
    newdecisions = []

    ignoreNextAction = False;
    for i in range (0, len(labels)):
        # check ignorflag
        if ignoreNextAction == True:
            ignoreNextAction = False
            newdecisions .append('')
        # check labels
        elif labels[i] == False:
            ignoreNextAction = True
            newdecisions.append('')
        else:
            newdecisions.append(decisions[i])

    investorLog=[['DataTime', 'Price', 'Action', 'Profit']]
    investor = []
    seller = []
    totalProfit = 0
    profitarray = []
    for i in range(0, len(newdecisions)):
        datatime = datetime.strptime(dataarray[i][1][0], '%d/%m/%Y %H:%M:%S')
        timetuple = datatime.timetuple()
        profit = 0
        if newdecisions[i] == True:
            seller.append(dataarray[i][1][4])
            if len(investor) > 0:
                buyprice = investor.pop()
                profit = float(dataarray[i][1][4]) - float(buyprice)
                profitarray.append(profit)
            totalProfit += profit
            investorLog.append([dataarray[i][1][0], dataarray[i][1][4], 'SELL', profit])

        elif newdecisions[i] == False:
            if len(seller) > 0:
                sellprice = seller.pop()
                profit = float(sellprice) - float(dataarray[i][1][4])
                profitarray.append(profit)

            totalProfit += profit
            investor.append(dataarray[i][1][4])
            investorLog.append([dataarray[i][1][0], dataarray[i][1][4], 'BUY', profit])
    
    investorLog.append(['Total Profit:', totalProfit])
    with open(outputFile + ".csv","w+") as my_csv:   
        csvWriter = csv.writer(my_csv, delimiter=',')  # using the csv module to write the file
        csvWriter.writerows(investorLog)
    return newdecisions,investorLog