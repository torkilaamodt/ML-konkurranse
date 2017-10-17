from sklearn.metrics import mean_squared_error as MSE
import csv
import numpy as np
from math import sqrt

def readDataSet(groupname):
    y = []
    with open(groupname, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
                y.append(float(row[-1]))
    return y

def readTarget():
    y_predicted = []
    with open('target', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
                y_predicted.append(float(row[0]))
    return y_predicted

def score(groupname):
    y_predicted = readDataSet(groupname)
    y = readTarget()

    mse = MSE( y, y_predicted )
    rmse = sqrt( mse )

    print "group: ", groupname, ": score: ", rmse

score("gruppe1");
score("gruppe2");
score("gruppe3");
score("gruppe4");
score("gruppe5");
score("gruppe6");
