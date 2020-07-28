import pandas as pd
from sklearn.metrics import accuracy_score  # az inam mishe estefade kard


def loadData():
    


    
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

    dataset = pd.read_csv('iris22.csv',names=names)

    x = []
    y = []



    for flower in range(len(dataset['class'])):
        
        sepal_area = dataset['sepal-width'][flower] * dataset['sepal-length'][flower]
        petal_area = dataset['petal-width'][flower] * dataset['petal-length'][flower]
        x.append([sepal_area,petal_area])
        y.append(dataset['class'][flower])

    
    return x,y


def knn_ALGORITHM(x_test , x_train , y_train , y_test ):
    k = 7
    difference = []

    for each_flower in range(len(x_test)):
        ls = []
        for flower in range(120):
            sepal_difference = abs(x_test[each_flower][0] - x_train[flower][0])
            petal_difference = abs(x_test[each_flower][1] - x_train[flower][1])
            ls.append([sepal_difference+ petal_difference,y_train[flower]])
        ls.sort()
        difference.append(ls)


    for each_flower in range(len(difference)):
        class_virginica = 0
        class_versicolor = 0
        class_setosa = 0
        for nn in range(k):

            
            if difference[each_flower][nn][1] == 'Iris-setosa':
                class_setosa +=1
            elif difference[each_flower][nn][1] == 'Iris-versicolor':
                class_versicolor +=1
            elif difference[each_flower][nn][1] == 'Iris-virginica':
                class_virginica +=1
        
        classes = [[class_virginica,'Iris-virginica'],[class_versicolor,'Iris-versicolor'],
                   [class_setosa,'Iris-setosa']]
        
        classes.sort()
        y_test.append(classes[2][1])
        
      
    return y_test

def acc_CAL(real,pred):

    incorrect = 0
    
    for i in range(len(real)):
        if real[i] != pred[i]:
            incorrect += 1

    return 1 - ((incorrect * 1) / 30)


x , y = loadData()

acc = 0

for each_shift in range(5):

    x_train , x_test = x[:each_shift * 30] + x[(each_shift + 1) * 30:] , x[each_shift * 30:(each_shift + 1) * 30]
    
    y_train , real_y_test = y[:each_shift * 30] + y[(each_shift + 1) * 30:] , y[each_shift * 30:(each_shift + 1) * 30]

    
    acc += acc_CAL(real_y_test,knn_ALGORITHM(x_test , x_train , y_train , []))
    
print(acc / 5)
