from DataSource import DataSource
class TrainingSet:
    
    def __init__(self, filename_1m, filename_3m, filename_5m, filename_15m, lrwindowsize):
        self.Filename = filename
        self.Datasource_1minute = DataSource(filename_1m, lrwindowsize)
        self.Datasource_3minute = DataSource(filename_3m, lrwindowsize)
        self.Datasource_5minute = DataSource(filename_5m, lrwindowsize)
        self.Datasource_15minute = DataSource(filename_15m, lrwindowsize)

        LoadDatasetFromfile(filename)
        return

    # 
    def LoadDatasetFromfile(self, LoadDatasetFromfile):
        self.Data = []
