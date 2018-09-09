import keras
from keras.models import Model
from keras.layers import Dense, Input, Add
from collectdata import CollectAllRawData, CollectTrainData
from preparedata import NormalizeData

# Collect data
data_1,data_5,data_10,data_20= CollectAllRawData('1','5','10','20')

slopeDataset, intercept_dataset = CollectTrainData(data_5=data_5,data_10= data_10, windowsize = 15)


# Prepare data

traingset = NormalizeData(dataset)
# Create model

# input for slope 
input_slopes = Input(15, )

x1 = Dense(units = 128, activation='relu')(input_slopes)
x1 = Dense(units = 64, activation='relu')(x1)
x1 = Dense(units = 32, activation ='relu')(x1)
x1 = Dense(units = 8, activation ='relu')(x1)

# input for intercepts
input_intercept = Input(15, )
x2 = Dense(units = 128, activation='relu')(input_slopes)
x2 = Dense(units = 64, activation='relu')(x2)
x2 = Dense(units = 32, activation ='relu')(x2)
x2 = Dense(units = 8, activation ='relu')(x2) 

# Addition model
model_add = Add()([x1,x2])

# Stack after addition
stack_out = Dense(units = 128, activation ='relu')(model_add)
stack_out = Dense(units = 64, activation='relu')(stack_out)
stack_out = Dense(units = 32, activation = 'relu')(stack_out)
stack_out = Dense(units = 8, activation = 'relu')(stack_out)
out = Dense(1, activation='sigmoid')(stack_out)

model = Model(inputs = [input_slopes, input_intercept], outputs = out)