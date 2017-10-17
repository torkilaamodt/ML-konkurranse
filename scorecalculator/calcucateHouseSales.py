import csv
from math import sqrt
from math import pow

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

def insideRange(prediction, target):
    rangeOver = target * 1.15
    rangeUnder = target * 0.85
    return prediction < rangeOver and prediction > rangeUnder

def calculateDiff(target, prediction):
    return sqrt(pow(target - prediction, 2))

def housesSold(groupPredictions):
    y = readTarget()

    housesSoldForGroup = [0]*(len(groupPredictions))

    for i in range (len(y)):
        closestGroupIndex = -1
        closestGroupValue = 1000000000

        for j in range(len(groupPredictions)):
            target = y[i]
            prediction = groupPredictions[j][i]
            diff = calculateDiff(target, prediction)
            if diff < closestGroupValue: # and insideRange(prediction, target)
                closestGroupIndex = j
                closestGroupValue = diff

        if closestGroupIndex != -1:
            housesSoldForGroup[closestGroupIndex] +=1

    for i in range(len(housesSoldForGroup)):
        print "Gruppe", i+1 , " solgte ", housesSoldForGroup[i], " hus"


numberOfGroups = 2; # number of groups / teams
groupPredictions = []

for i in range (1, numberOfGroups+1):
    groupPredictions.append(readDataSet("gruppe{0}".format(i)))


housesSold(groupPredictions);
