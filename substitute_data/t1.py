import pandas as pd

url = 'dt.txt'

names = ['Date','Open','High','Low','Close','Volume','OpenInt']

dataset = pd.read_csv(url,names = names)
print(dataset['Date'][1:10])

dataset = dataset.drop('Date',axis = 1)
dataset = dataset.drop('OpenInt',axis = 1)
dataset = dataset.drop(0,axis = 0)
print(dataset[1:10])
