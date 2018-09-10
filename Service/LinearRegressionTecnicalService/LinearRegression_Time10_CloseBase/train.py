from collectdata import CollectAllRawData, CollectTrainData, ListCandidatePoint
from preparedata import NormalizeData
from makedecision import SplitCandidateData, CalculateProfit, AssignLabel, CalculateProfitByLabel
# Collect data
data_1,data_5,data_10,data_20= CollectAllRawData('1','5','15','3')

lrarray_5, lrarray_10 = CollectTrainData(data_5, data_10, windowsize = 15)

# List Candidate point
candidatevalues, candidatedecision = ListCandidatePoint(data_5, lrarray_5)

# Split candidate data
outdata, splitedcandidatedecision = SplitCandidateData(data_5, candidatevalues, candidatedecision)

investorLog, profitarray = CalculateProfit(outdata, splitedcandidatedecision, 'Data/tempReport' )

# Assign label
trainlables = AssignLabel(profitarray)

# CalculateProfitByLabel
CalculateProfitByLabel(outdata, trainlables, splitedcandidatedecision, 'Data/tempReport2')

# Prepare data

dataset_slopes, dataset_intercept, labels = NormalizeData(lrarray_5, lrarray_10, outdata, trainlables, 30)

# Create model
import keras
from keras.models import Model
from keras.layers import Dense, Input, Add
from keras.optimizers import Adam
import numpy as np

# input for slope 
input_slopes = Input(shape = (30,))

x1 = Dense(units = 128, activation='relu')(input_slopes)
x1 = Dense(units = 64, activation='relu')(x1)
x1 = Dense(units = 32, activation ='relu')(x1)
x1 = Dense(units = 8, activation ='relu')(x1)

# input for intercepts
input_intercept = Input(shape = (30,))
x2 = Dense(units = 128, activation='relu')(input_intercept)
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
model.compile(loss="mse", optimizer=Adam(lr=0.001))
model.fit([dataset_slopes, dataset_intercept] ,
          np.array(labels), epochs = 10000, batch_size = 32)

# Save Model
model.save("Model/model_ep0")