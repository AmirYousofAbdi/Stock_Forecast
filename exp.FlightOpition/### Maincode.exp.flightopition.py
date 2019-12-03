##############################################   importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
'''from sklearn import model_selection
import seaborn as sns, numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from scipy import misc
import matplotlib.pyplot as plt'''
##############################################    Making the dataset
sys.__stdout__ = sys.stdout
url = "exp.flight.data.txt"
names = ['Airline','Airline ID','Source Airport','Source Airport ID','Destination Airport','Destination Airport ID','Codeshare','Stops','Equipment']
dataset = pd.read_csv(url,names=names)
ori = input().upper()
des = input().upper()
for i in range(67663):
    data_sou = dataset['Source Airport']
    data_des = dataset['Destination Airport']
    #f = dataset
    if data_sou[i] == ori:
        if data_des[i] == des:
            print(dataset.loc[i])
            print('########################################       other flights')
'''#print(dataset.head(5))


##############################################    Function defining
#des = {
#    "LosAngles" : 200
#    "Shanghai" : 150
#    "Dubai" : 100
#    "Tehran" : 80
#    }
def price_f(a,b):
    ls=[]
    for i in range(4):
        price = 0
        z = dataset['Departure'].values
        j = dataset['Flight During'].values
        b = int(j[i])
        a = int(z[i])
        price = 85 * b
        if 5 < a < 10:
            price += 100
        elif 10 < a < 14:
            price += 200
        else:
            price += 50
        ls.append(price)
    return ls
print(price_f(dataset["Departure"],dataset["Flight During"]))
'''
