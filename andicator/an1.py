import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

url = 'C:\\Users\\Lenovo\\Desktop\\Sani\\andicatot\\data.txt'
    #########################

names = ['Date','Open','High','Low','Close','Volume','OpenInt']

dataset = pd.read_csv(url,names = names)

dataset = dataset.drop(0,axis = 0)
dataset = dataset.drop('Date',axis = 1)
dataset = dataset.drop('OpenInt',axis = 1)
for i in range(1,6):
    for k in range(1,3202):
        dataset[names[i]][k] = float(dataset[names[i]][k])
# len = 3201
# learn = [0:2731]
# test = [2731:3201]

data_normaliser = preprocessing.MinMaxScaler()
dataset = data_normaliser.fit_transform(dataset)

deltap = []
for i in range(1,3201):
    deltap.append(dataset[i-1][0] - dataset[i][0])
deltat = deltap[:2731]
for i in range(2731,3200):
    deltat.append(deltap[i-1]-deltap[i])
plt.plot(deltap,color = 'red')
plt.plot(deltat,color = 'green')
style = plt.gcf()
style.set_size_inches(12,10)
plt.show()