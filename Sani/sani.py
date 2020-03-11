import pandas as pd
from sklearn import preprocessing
import numpy as np
import keras
from keras.models import Model
from keras.layers import Dense, Dropout, LSTM, Input, Activation
from keras import optimizers
np.random.seed(4)
import tensorflow as tf
tf.random.set_seed(4)

history_points = 21
def datamaker():
    url = 'data.txt'
    #########################
    history_points = 21
    names = ['Date','Open','High','Low','Close','Volume','OpenInt']

    dataset = pd.read_csv(url,names = names)
    
    dataf = dataset.copy()
    
    dataset = dataset.drop('Date',axis = 1)
    dataset = dataset.drop('OpenInt',axis = 1)
    dataset = dataset.drop(0,axis = 0)
    data = dataset.copy()
    #   Dataset without Date,OpenInt and first row is ready

    data_normaliser = preprocessing.MinMaxScaler()
    data_normalised = data_normaliser.fit_transform(dataset)
    #  Normalised data is ready

    history_points = 21

    ohlcv_histories_normalised =      np.array([data_normalised[i  : i + history_points].copy() for i in range(len(data_normalised) - history_points)])
    next_day_open_values_normalised = np.array([data_normalised[i + history_points][0].copy() for i in range(len(data_normalised) - history_points)])
    next_day_open_values_normalised = np.expand_dims(next_day_open_values_normalised, -1)

    next_day_open_values = np.array([data['Open'][i + history_points] for i in range(len(data) - history_points)])
    next_day_open_values = np.expand_dims(next_day_open_values, -1)

    y_normaliser = preprocessing.MinMaxScaler()
    y_normaliser.fit( next_day_open_values )

    def calc_ema(values, time_period):

            sma = np.mean(values[:, 3])
            ema_values = [sma]
            k = 2 / (1 + time_period)
            for i in range(len(his) - time_period, len(his)):
                close = his[i][3]
                ema_values.append(close * k + ema_values[-1] * (1 - k))
            return ema_values[-1]

    technical_indicators = []
    for his in ohlcv_histories_normalised:

        sma = np.mean(his[:, 3])
        macd = calc_ema(his, 12) - calc_ema(his, 26)
        technical_indicators.append(np.array([sma]))


    technical_indicators = np.array(technical_indicators)

    tech_ind_scaler = preprocessing.MinMaxScaler()
    technical_indicators_normalised = tech_ind_scaler.fit_transform(technical_indicators)

    assert ohlcv_histories_normalised.shape[0] == next_day_open_values_normalised.shape[0] == technical_indicators_normalised.shape[0]
    return dataf,ohlcv_histories_normalised, next_day_open_values_normalised, next_day_open_values, y_normaliser


data,ohlcv_histories, next_day_open_values, unscaled_y, y_normaliser = datamaker()

test_split = 0.9
n = int(ohlcv_histories.shape[0] * test_split)

ohlcv_train = ohlcv_histories[:n]
y_train = next_day_open_values[:n]

ohlcv_test = ohlcv_histories[n:]
y_test = next_day_open_values[n:]

unscaled_y_test = unscaled_y[n:]

print(ohlcv_train.shape)
print(ohlcv_test.shape)


# model architecture

lstm_input = Input(shape=(history_points, 5), name='lstm_input')
x = LSTM(50, name='lstm_0')(lstm_input)
x = Dropout(0.2, name='lstm_dropout_0')(x)
x = Dense(64, name='dense_0')(x)
x = Activation('sigmoid', name='sigmoid_0')(x)
x = Dense(1, name='dense_1')(x)
output = Activation('linear', name='linear_output')(x)

model = Model(inputs=lstm_input, outputs=output)
adam = optimizers.Adam(lr=0.0005)
model.compile(optimizer=adam, loss='mse')
model.fit(x=ohlcv_train, y=y_train, batch_size=32, epochs=50, shuffle=True, validation_split=0.1)


# evaluation

y_test_predicted = model.predict(ohlcv_test)
y_test_predicted = y_normaliser.inverse_transform(y_test_predicted)
y_predicted = model.predict(ohlcv_histories)
y_predicted = y_normaliser.inverse_transform(y_predicted)

assert unscaled_y_test.shape == y_test_predicted.shape
#print(y_test_predicted)
#np.subtractunscaled_y_test, y_test_predicted) 
#real_mse = np.mean(np.square(np.subtract(unscaled_y_test, y_test_predicted)))
#scaled_mse = real_mse / (np.max(unscaled_y_test) - np.min(unscaled_y_test)) * 100
#print(scaled_mse)
def dtm(ls):
    ls2 = [
            ]
    for i in ls:
        #print(i[0])
        ls2.append(float(i[0]))
    return ls2
import matplotlib.pyplot as plt

unscaled_y_test = dtm(unscaled_y_test.tolist())
y_test_predicted = dtm(y_test_predicted.tolist())

#for i in range(100):
    #print(type(y_test_predicted[i][0]))

y1 = unscaled_y_test[:153]

x1 = [data['Date'][i]for i in range(0,len(data),21)]
# plotting the line 1 points 

plt.plot(x1, y1, label = "pred")
# line 2 points
y2 = y_test_predicted[:153]
#x2 = [data[i][0]for i in range(0,len(data),21)]
# plotting the line 2 points 

plt.plot(x1, y2, label = "real")
plt.xlabel('Time period')
# Set the y axis label of the current axis.
plt.ylabel('Price')
# Set a title of the current axes.
#plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
# Display a figure.

plt.show()

#from datetime import datetime
#model.save(f'basic_model.h5')
