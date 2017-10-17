from sklearn.neural_network import MLPRegressor
import csv
import numpy as np
from sklearn.metrics import mean_squared_error as MSE
from math import sqrt

X = []
y = []

def readDataSet():
    with open('../data/Treningsdata/normalisert_training_data_without_header.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
                row = list(map(lambda x: float(x), row))
                X.append(row[:-1])
                y.append(row[-1])


readDataSet()

#http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html
mlp = MLPRegressor()
mlp.fit(X, y)

print("Training set score: %f" % mlp.score(X, y))


p = mlp.predict(X);
mse = MSE( y, p )
rmse = sqrt( mse )
print rmse
