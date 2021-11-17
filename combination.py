from readfile import ReadData
import pandas as pd
import numpy as np

class combination:
    datasetOri = []
    objData = ReadData()
    dataset = []
    y = []
    X = []

    def __init__(self):
        self.datasetOri = self.objData.readDiabetesDataset()
        self.getTarget()
        self.getFeature()
        self.viewData()
        # self.createData()

    def viewData(self):
        print("target Data ", self.y)
        print("feature data \n", self.X)
        print("len or rows ", len(self.datasetOri))
        print("len of columns ", len(self.datasetOri.columns))
        print("shape data ", self.datasetOri.shape)
        print("size ",self.datasetOri.size)

    def createData(self):
        df = self.datasetOri.iloc[:, 0]
        df1 = self.datasetOri.iloc[:, 1]
        df.append(df1)
        asu = df.values.tolist()
        print(df)

    def getCombination(self):
        pass

    def getTarget(self):
        end = len(self.datasetOri.columns)
        self.y = self.datasetOri.iloc[:,end-1]
        self.y = np.array(self.y)

    def getFeature(self):
        end = len(self.datasetOri.columns)
        self.X = self.datasetOri.iloc[:,0:end-1]
        self.X = np.array(self.X)