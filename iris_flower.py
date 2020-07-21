import pandas as pd

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

dataset = pd.read_csv('iris22.csv',names=names)

x_train = []
y_train = []
n = int(input('Train data: '))
k = 7
for flower in range(150):
    
    sepal_area = dataset['sepal-width'][flower] * dataset['sepal-length'][flower]
    petal_area = dataset['petal-width'][flower] * dataset['petal-length'][flower]
    x_train.append([sepal_area,petal_area])
    y_train.append(dataset['class'][flower])

x_test , x_train , y_train = x_train[n:] , x_train[:n] , y_train[:n]

difference = []

for i in range(len(x_test)):
    ls = []
    for flower in range(n):
        sepal_difference = abs(x_test[i][0] - x_train[flower][0])
        petal_difference = abs(x_test[i][1] - x_train[flower][1])
        ls.append([sepal_difference+ petal_difference,y_train[flower]])
    ls.sort()
    difference.append(ls)

y_test = []
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
    
    classes = [[class_virginica,'Iris-virginica'],[class_versicolor,'Iris-versicolor'],[class_setosa,'Iris-setosa']]
    
    classes.sort()
    y_test.append(classes[2][1])
print(*y_test,sep='\n')
