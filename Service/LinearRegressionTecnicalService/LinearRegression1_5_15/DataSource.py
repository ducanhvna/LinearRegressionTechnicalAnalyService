import pandas as pd
from TechnicalAnalys import LinearRegression

class DataSource: 
    def __init__(self, fileName, lnRgwindowSize):
        self.FileName = fileName
        self.LnRgwindowSize = lnRgwindowSize

        # Read data frame from file
        self.DataFrame = pd.read_csv('Data+/' + fileName +'.csv')

        # Calculat linear regression value for close value
        self.LinearRegressionCloseValue = LinearRegression(DataFrame, 4, lnRgwindowSize)

    def ExportLinearRegressionTimeSeriesInfo(self, windowsize):
        self.DataInputSize = windowsize

        self. AvaiableIndexStarted = self.LnRgwindowSize + self.DataInputSize
        self.RegressionArray = []
        
        for i in range(AvaiableIndexStarted, len(LinearRegressionCloseValue)):
            dataitem = []
            for j in range(0, self. DataInputSize):
                index = i -  self. DataInputSize + j + 1
                dataitem.append(LinearRegressionCloseValue[index])
            self.RegressionArray.append(dataitem)


     
