############################################################################### Load libraries
import pandas
#############################################
import seaborn as sns, numpy as np
#############################################
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
############################################################################### Variables
mon = ["0:00","0:15","0:30","0:45","1:00","1:15","1:30","1:45","2:00","2:15","2:30","2:45","3:00","3:15","3:30","3:45","4:00","4:15","4:30","4:45","5:00","5:15","5:30","5:45","6:00"]
mon = ["January","February","March","April","May","June","July","August","September ","October","November","December"]
cos = ["45","46","47","48","49","50","51","52","53",'54','55','56','57','58','59','60']
############################################################################### Load the dataset
#### Load dataset
url = 'exp.graph.data.txt'
names = ["Time","Euro"]
dataset = pandas.read_csv(url, names=names)
############################################################################### Summerizing the Data
##### head
#print(dataset.head(5:6))
import matplotlib.pyplot as plt 
  
# x axis values چيزايي که در نمودار ايکس نشان داده مي شود و از ديتا ست و سي اس وي ميگيرد
x = dataset["Time"]
# corresponding y axis values 
y = dataset["Euro"] 
  
# plotting the points  
plt.plot(x, y, color='green', linestyle='solid', linewidth = 2) 
  
# setting x and y axis range 
plt.ylim(0.8955,0.8970) 
plt.xlim(1,24) 
  
# naming the x axis 
plt.xlabel('Time') 
# naming the y axis 
plt.ylabel('EURo') 
  
# giving a title to my graph 
plt.title('Each Dollar per Euro Diagram') 
  
# function to show the plot 
plt.show() 

#January,50
#February,52
#March,48
#April,54
#May,57
#June,59
#July,56
#ugust,49
#September,48
#October,52
#November,51
#December,55
#, marker='o', markerfacecolor='red', markersize=6
ls = []
a = dataset.at[4,'Euro']
for i in range(1,24):
    a = dataset.at[i,'Euro']
    g = dataset.at[i-1,'Euro']
    #print(a,g)
    #print("********************")
    if a > g:
        ls.append("Up")
    elif a < g:
        ls.append("Down")
    else:
        ls.append("straight")
up = 0
do = 0
st = 0
for k in range(23):
    print(ls[k])
    if ls[k] == "Up":
        up = up + 1
    elif ls[k] == "Down":
        do = do + 1
    else:
        st = st + 1
if st > do and st > up:
    if ls[22] == st:
        if do < up:
            print("######down")
        else:
            print("######Up")
    elif ls[22] == do:
        if do < up:
            print("######up")
        else:
            print("######st or down")
    else:
        if do < up:
            print("######down")
        else:
            print("######st or down")
#############################################3
elif do > st and do > up:
    if ls[22] == st:
        if do < up:
            print("######down")
        else:
            print("######Up")
    elif ls[22] == do:
        if do < up:
            print("######up")
        else:
            print("######st or up")
    else:
        if do < up:
            print("######down")
        else:
            print("######st or down")
###################################################
if up > do and up > st:
    if ls[22] == st:
        if do < up:
            print("######down")
        else:
            print("######Up")
    elif ls[22] == do:
        if do < up:
            print("######up")
        else:
            print("######st or down")
    else:
        if do < up:
            print("######down")
        else:
            print("######st or down")
