import pandas as pd
from sklearn import preprocessing
#import keras
import numpy as np


url = 'dt.txt'

names = ['Date','Open','High','Low','Close','Volume','OpenInt']

dataset = pd.read_csv(url,names = names)

dataset = dataset.drop('Date',axis = 1)
dataset = dataset.drop('OpenInt',axis = 1)
dataset = dataset.drop(0,axis = 0)
data = dataset.copy()
#   دیتاست بدون ستون دیت و اپن اینت و ردیف اول آماده است

data_normaliser = preprocessing.MinMaxScaler()
data_normalised = data_normaliser.fit_transform(dataset)
# ديتاست نورمالايز شده اماده است

history_points = 21

ohlcv_histories_normalised =      np.array([data_normalised[i  : i + history_points].copy() for i in range(len(data_normalised) - history_points)])
next_day_open_values_normalised = np.array([data_normalised[i + history_points][0].copy() for i in range(len(data_normalised) - history_points)])
next_day_open_values_normalised = np.expand_dims(next_day_open_values_normalised, -1)

next_day_open_values = np.array([data['Open'][i + history_points] for i in range(len(data) - history_points)])
next_day_open_values = np.expand_dims(next_day_open_values_normalised, -1)

y_normaliser = preprocessing.MinMaxScaler()
y_normaliser.fit(np.expand_dims( next_day_open_values,axis=1 ))
