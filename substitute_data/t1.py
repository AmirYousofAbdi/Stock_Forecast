import pandas as pd
from sklearn import preprocessing
url = 'dt.txt'

names = ['Date','Open','High','Low','Close','Volume','OpenInt']

dataset = pd.read_csv(url,names = names)

dataset = dataset.drop('Date',axis = 1)
dataset = dataset.drop('OpenInt',axis = 1)
dataset = dataset.drop(0,axis = 0)
#   دیتاست بدون ستون دیت و اپن اینت و ردیف اول آماده است

data_normaliser = preprocessing.MinMaxScaler()
dataset = data_normaliser.fit_transform(dataset)
