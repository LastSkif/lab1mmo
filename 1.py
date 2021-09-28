# from google.colab import files
import csv
import random
import math
import operator


def loadDataset(trainingSet=[], testSet=[]):
    nol = 0
    with open("data3.csv", 'rt') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            if (x == 0):
                continue
            for y in range(3):
                dataset[x][y] = int(dataset[x][y])
            if (dataset[x][2]):
                nol += 1
            if (random.random() < 0.66):
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
    return nol / 10000


def main():
    train = []
    test = []

    nolP = loadDataset(train, test)
    edP = 1 - nolP

    distk = [0] * len(train)
    index = [0] * 100000

    ch = 200
    result = 0
    result2 = 0
    for i in range(len(test)):
        gh = 0
        for j in range(len(train)):
            distk[j] = ((test[i][0] - train[j][0]) ** 2 + (test[i][1] - train[j][1]) ** 2) ** 0.5
            index[int(distk[j])] = train[j][2]

        distk.sort()

        n = 0
        e = 0
        for k in range(ch):
            if (int(index[int(distk[k])]) == 0):
                n += edP ** k
            else:
                e += nolP ** k
                gh += 1

        if ((n > e and train[i][2] == 0) or (e > n and train[i][2] == 1)):
            result += 1
        if ((gh > ch / 2 and train[i][2] == 1) or (gh < ch / 2 and train[i][2] == 0)):
            result2 += 1

        if (i % 100 == 0):
            print(i)
    print("4 ves =", result / 30, " obichnaya = ", result2 / 30)


main()
