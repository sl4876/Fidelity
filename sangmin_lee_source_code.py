# -*- coding: utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

ls

data = pd.read_csv("export.csv")

data = pd.DataFrame(data)

data

data.head()

uni_data =data['Total Population'][0:10]
uni_data.index = data['label'][0:10]
plt.figure()
plt.xlabel('Years') 
plt.ylabel('Population') 
plt.title("Population Graph for   Cader park")
plt.plot(uni_data)
plt.show()

df = pd.read_csv('Austin_Water_-_Residential_Water_Consumption.csv')

lists=[]
for a in df["Year Month"]:
  print(a)
  text = str(int(a/100))+"-" + str(int(a%100))+ "-01"
  print(text)
  lists.append(text)

check = pd.to_datetime(lists)
df["Year Month"] = check

df.rename(columns = {'Year Month':'datetime'}, inplace = True)

df.head()

df1 = pd.read_excel("Austin Population by Zip Code.xlsx")

df1

df2 = pd.read_csv("Austin,United States 2012-01-01 to 2022-11-28.csv")

df2_1 = df2.groupby(pd.PeriodIndex(df2['datetime'], freq="M"))['temp'].mean().reset_index()
df2_2 = df2.groupby(pd.PeriodIndex(df2['datetime'], freq="M"))['humidity'].mean().reset_index()

df2["Day_time"] = pd.to_datetime(df2["sunset"]) -pd.to_datetime(df2['sunrise'])

df2_3 = df2.groupby(pd.PeriodIndex(df2['datetime'], freq="M"))["Day_time"].mean().reset_index()



final = pd.merge(df2_2 , df2_1)



final

final1 = pd.merge(final , df2_3)

final1

final1["datetime"]= pd.to_datetime(final1["datetime"].astype(str))

final3 = pd.merge(final1 , df)



final3["Day_time"] =final3["Day_time"].dt.total_seconds()/60

final3

pip install dataframe-image

import pandas as pd
import dataframe_image as dfi

final3.head()

from pandas import read_csv
from matplotlib import pyplot

for (class_1), group in final3.groupby(['Customer Class']):
     group.to_csv(f'{class_1}.csv', index=False)
     print(group.head())
     print(group.describe())
     for (class_2), group2 in group.groupby(['Postal Code']):
       
       uni_data = group2['Total Gallons']
       uni_data.index = group2['datetime']
       print(uni_data)
       uni_data.plot()
       plt.figure()
       plt.xlabel('Date') 
       plt.ylabel('Gallons used') 
       plt.title(f'{class_1}'+'_' + f'{class_2}')
       plt.plot(uni_data)
       plt.show()
       groups = [ 1, 2, 3  ,6]
       i = 1
       pyplot.figure()
       values = group2.values
       for group in groups:
         pyplot.subplot(len(groups), 1, i)
         pyplot.plot(values[:, group])
         plt.xlabel('Date in months') 
         #plt.ylabel('')
         pyplot.title(group2.columns[group]+"-2012-1 to 2020-9", y=0.5, loc='right')
         i += 1
         pyplot.show()

# Complete data prediction

for (class_1), group in final3.groupby(['Postal Code']):
     check = group.drop(["temp" ,'humidity' , 'Day_time'],  axis=1)
     print(check.head())
     print(check.describe())

#group2[-12:]

from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
 
# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg
i = 0
for (class_1), group in final3.groupby(['Customer Class']):
     group.to_csv(f'{class_1}.csv', index=False)
     print(group.head())
     print(group.describe())
     for (class_2), group2 in group.groupby(['Postal Code']):
       if i < 5 :
         dataset = pd.DataFrame(group2)
         i = i + 1
dataset.fillna(value='', inplace=True)
values = dataset.drop(['Postal Code' , 'Customer Class'] , axis = 1).values
# integer encode direction
# ensure all data is float
print(dataset["datetime"])
input = values[: , 1:]
#input = float("{:.2f}".format(input))
input = input.astype('float32')

dataset

input

n_train_hours = 100
#train = final[0:n_train_hours, :]
#test = final[n_train_hours:, :]
print(input)
mean = input[0:n_train_hours, :].mean(axis = 0)
print(mean)
std = input[0:n_train_hours, :].std(axis = 0)
print(std)
# design network
dataset1 = (input-mean)/std

def multivariate_data(dataset, target, start_index, end_index, history_size,
                      target_size, step, single_step=False):
  data = []
  labels = []

  start_index = start_index + history_size
  if end_index is None:
    end_index = len(dataset) - target_size

  for i in range(start_index, end_index):
    indices = range(i-history_size, i, step)
    data.append(dataset[indices])

    if single_step:
      labels.append(target[i+target_size])
    else:
      print(target[i:i+target_size] , target_size )
      labels.append(target[i:i+target_size])

  return np.array(data), np.array(labels)

TRAIN_SPLIT = 40

dataset1[: ,:].shape

from tensorflow.python.data.ops.dataset_ops import DatasetV1Adapter
future_target = 12
past_history = 24
STEP = 2
x_train_multi, y_train_multi = multivariate_data(dataset1[:, :], dataset1[:, 3], 0,
                                                 TRAIN_SPLIT, past_history,
                                                 future_target, STEP)
x_val_multi, y_val_multi = multivariate_data(dataset1, dataset1[:, 3],
                                             TRAIN_SPLIT, None, past_history,
                                             future_target, STEP)

import tensorflow as tf
BATCH_SIZE = 2
BUFFER_SIZE = 10

x_train_multi[:].shape

train_data_multi = tf.data.Dataset.from_tensor_slices((x_train_multi[:], y_train_multi))
train_data_multi = train_data_multi.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()

val_data_multi = tf.data.Dataset.from_tensor_slices((x_val_multi, y_val_multi))
val_data_multi = val_data_multi.batch(BATCH_SIZE).repeat()

def create_time_steps(length):
  return list(range(-length, 0))

def multi_step_plot(history, true_future, prediction):
  plt.figure(figsize=(12, 6))
  num_in = create_time_steps(len(history))
  num_out = len(true_future)

  plt.plot(num_in, np.array(history[:, 1]), label='History')
  plt.plot(np.arange(num_out)/STEP, np.array(true_future), 'bo',
           label='True Future')
  if prediction.any():
    plt.plot(np.arange(num_out)/STEP, np.array(prediction), 'ro',
             label='Predicted Future')
  plt.legend(loc='upper left')
  plt.show()

for x, y in train_data_multi.take(1):
  multi_step_plot(x[0], y[0], np.array([0]))

multi_step_model = tf.keras.models.Sequential()
multi_step_model.add(tf.keras.layers.LSTM(32,
                                          return_sequences=True,
                                          input_shape=x_train_multi.shape[-2:]))
multi_step_model.add(tf.keras.layers.LSTM(16, activation='relu'))
multi_step_model.add(tf.keras.layers.Dense(12))

multi_step_model.compile(optimizer=tf.keras.optimizers.RMSprop(clipvalue=1.0), loss='mae')

for x, y in val_data_multi.take(1):
  print (multi_step_model.predict(x).shape)

EPOCHS = 100
EVALUATION_INTERVAL = 20

multi_step_history = multi_step_model.fit(train_data_multi, epochs=EPOCHS,
                                          steps_per_epoch=EVALUATION_INTERVAL,
                                          validation_data=train_data_multi,
                                          validation_steps=50)

def multi_step_plot(history, true_future, prediction):
  plt.figure(figsize=(12, 6))
  num_in = create_time_steps(len(history))
  num_out = len(true_future)

  plt.plot(num_in, np.array(history[:, 1]), label='History')
  plt.plot(np.arange(num_out)/STEP, np.array(true_future), 'bo',
           label='True Future')
  if prediction.any():
    plt.plot(np.arange(num_out)/STEP, np.array(prediction), 'ro',
             label='Predicted Future')
  plt.legend(loc='upper left')
  plt.show()

def plot_train_history(history, title):
  loss = history.history['loss']
  val_loss = history.history['val_loss']

  epochs = range(len(loss))

  plt.figure()

  plt.plot(epochs, loss, 'b', label='Training loss')
  plt.plot(epochs, val_loss, 'r', label='Validation loss')
  plt.title(title)
  plt.legend()

  plt.show()

for x, y in train_data_multi.take(10):
  multi_step_plot(x[0], y[0], multi_step_model.predict(x)[0])

df2_1 = df2.groupby(pd.PeriodIndex(df2['datetime'], freq="M"))['temp'].sum().reset_index()
df2_2 = df2.groupby(pd.PeriodIndex(df2['datetime'], freq="M"))['humidity'].sum().reset_index()

df2_2

df2_1

df2["Day_time"] = pd.to_datetime(df2["sunset"]) -pd.to_datetime(df2['sunrise'])

df2_3 = df2.groupby(pd.PeriodIndex(df2['datetime'], freq="M"))["Day_time"].mean().reset_index()

final = pd.merge(df2_2 , df2_1)

final

df2



final1 = pd.merge(final , df2_3)

final1

df1_1 = df.groupby(pd.PeriodIndex(df['datetime'], freq="M"))['Total Gallons'].sum().reset_index()

final1

df1_1

final3 = pd.merge(final1 , df1_1)

final3.head()

a = final3.groupby(pd.PeriodIndex(final3['datetime'], freq="M"))["Day_time"].mean().reset_index()

b = final3.groupby(pd.PeriodIndex(final3['datetime'], freq="M"))["Total Gallons"].sum().reset_index()

c = final3.groupby(pd.PeriodIndex(final3['datetime'], freq="M"))["humidity"].mean().reset_index()

d = final3.groupby(pd.PeriodIndex(final3['datetime'], freq="M"))["temp"].mean().reset_index()

final = pd.merge(a , b)
final1 = pd.merge(final, c)
final2 = pd.merge(final1, d)

final2

input

final2["datetime"]= pd.to_datetime(final2["datetime"].astype(str))

final2["Day_time"] =final2["Day_time"].dt.total_seconds()/60

final2.values[:, 1]

input = final2.values[:, 1:]
input = input.astype('float32')
n_train_hours = 100
#train = final[0:n_train_hours, :]
#test = final[n_train_hours:, :]
print(input)
mean = input[0:n_train_hours, :].mean(axis = 0)
print(mean)
std = input[0:n_train_hours, :].std(axis = 0)
print(std)
# design network
dataset1 = (input-mean)/std

from tensorflow.python.data.ops.dataset_ops import DatasetV1Adapter
future_target = 12
past_history = 24
STEP = 2
x_train_multi, y_train_multi = multivariate_data(dataset1[:, :], dataset1[:, 3], 0,
                                                 TRAIN_SPLIT, past_history,
                                                 future_target, STEP)
x_val_multi, y_val_multi = multivariate_data(dataset1, dataset1[:, 3],
                                             TRAIN_SPLIT, None, past_history,
                                             future_target, STEP)

train_data_multi = tf.data.Dataset.from_tensor_slices((x_train_multi[:], y_train_multi))
train_data_multi = train_data_multi.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()

val_data_multi = tf.data.Dataset.from_tensor_slices((x_val_multi, y_val_multi))
val_data_multi = val_data_multi.batch(BATCH_SIZE).repeat()

multi_step_history = multi_step_model.fit(train_data_multi, epochs=EPOCHS,
                                          steps_per_epoch=EVALUATION_INTERVAL,
                                          validation_data=val_data_multi,
                                          validation_steps=50)

for x, y in val_data_multi.take(10):
  multi_step_plot(x[0], y[0], multi_step_model.predict(x)[0])
