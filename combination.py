from readfile import ReadData
import pandas as pd
import numpy as np
from itertools import permutations

class combination:
    datasetOri = []
    objData = ReadData()
    dataset = []
    y = []
    X = []
    index = []

    def __init__(self):
        self.datasetOri = self.objData.readDiabetesDataset()
        self.getTarget()
        self.getFeature()
        # self.viewData()
        self.getCombination()
        print(self.index)
        print(len(self.index))

    def viewData(self):
        print("target Data ", self.y)
        print("feature data \n", self.X)
        print("len or rows ", len(self.datasetOri))
        print("len of columns ", len(self.datasetOri.columns))
        print("shape data ", self.datasetOri.shape)
        # print("size ",self.datasetOri.size)

    def createData(self):
        df = self.datasetOri.iloc[:, 0]
        df1 = self.datasetOri.iloc[:, 1]
        df.append(df1)
        print(df)

    def getCombination(self):
        coloumns = self.__createIndex()
        for k in range(2, len(coloumns)):
            perm = permutations(coloumns, k)
            for i in list(perm):
                self.index.append(i)

    def __createIndex(self):
        col = []
        n = len(self.datasetOri.columns)
        for i in range(n):
            col.append(i)
        return col

    def getTarget(self):
        end = len(self.datasetOri.columns)
        self.y = self.datasetOri.iloc[:,end-1]
        self.y = np.array(self.y)

    def getFeature(self):
        end = len(self.datasetOri.columns)
        self.X = self.datasetOri.iloc[:,0:end-1]
        self.X = np.array(self.X)