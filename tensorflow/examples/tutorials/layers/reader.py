import numpy as np
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import skimage, os
import numpy as np


def readtrain(path):
    arr = np.array([])
    for i in range(2):
        filename = path + "/train" + str(i + 1) + ".png"
        ByArray = open(filename, "rb").read()
        matrix = np.fromfile(filename,dtype=np.uint16)
        l = len(matrix)
        padding = np.zeros(20000 - l);
        matrix = np.append(matrix, padding)
        l = len(matrix)
        print(l)
        matrix[matrix<500] =0
        matrix[matrix>=500] =1
        matrix = 1-matrix
        matrix = matrix.reshape(160, 125)
        matrix = matrix[0:100, 0:100]
        arr = np.append(arr, matrix)
    arr = arr.reshape(2, 100, 100)
    print(arr.shape)
    return arr

def readtrainlabel(path):
    labels = np.array([0, 1])
    labels = labels.astype(int)
    return labels

def readpred(path):
    arr = np.array([])
    for i in range(2):
        filename = path + "/predict" + str(i + 1) + ".png"
        ByArray = open(filename, "rb").read()
        matrix = np.fromfile(filename,dtype=np.uint16)
        l = len(matrix)
        padding = np.zeros(20000 - l);
        matrix = np.append(matrix, padding)
        l = len(matrix)
        print(l)
        matrix[matrix<500] =0
        matrix[matrix>=500] =1
        matrix = 1-matrix
        matrix = matrix.reshape(160, 125)
        matrix = matrix[0:100, 0:100]
        arr = np.append(arr, matrix)
    arr = arr.reshape(2, 100, 100)
    print(arr.shape)
    arr = arr.astype(int)
    return arr

def readpredlabel(path):
    labels = np.array([0, 1])
    labels = labels.astype(int)
    return labels



