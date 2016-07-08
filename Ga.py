import numpy as np
import pandas as pd
from random import *
#from sklearn import *


Data = pd.read_excel('yl_factors.xls')
label = pd.read_excel('YL3.xls')
Lbael = np.reshape(label.iloc[:].value,[1200,])

PopuNum = 100
IterNum = 1000

Biont = []

class Biont():
    gen = np.ones([PopuNum,164],np.int32)
    acc = np.zeros(PopuNum)
    adapt = np.zeros(PoPuNum)
    def __init__(self):
        for j in range(PopuNum):
            for i in range(164):
                self.gen[j][i] = randint(0,1)

    def CalAcc(self):
        TrainData = self.GenTraindata()
        clf = svm.SVC()   #定义SVM参数
        self.acc = cross_validation.cross_val_score(clf,TrianData,Label,cv5)
        return self.acc

    def GenTraindata(self):
        index = []
        for i in gen:
            index.append(bool(i))
        TrainData = Data.iloc[:,index]
        return TrainData

def init():
    Biont = Biont()

def choose():
    AccSum = 0
    Luck = []
    tmp = Biont.gen[:]
    for i in range(PopuNum):
        if Biont.acc[i] < 50
            Biont.acc[i] = 0
        else:
            Biont.acc[i] = (Biont.acc[i] - 50)**2
        #远小于50是否应该标记出来
        AccSum += Biont[i].acc
    for i in range(PopuNum):
        Biont[i].adapt = Biont[i].acc/AccSum

    for i in range(PopuNum-20):
        r = random()
        sum = 0
        for j in range(PopuNum):
            sum += Biont.adapt[j]
            if sum > r
                Luck.append(i) = j
    
    for i in range(Popunum):             
        if i < PopuNum - 20
            gen[i][:] = tmp[Luck[i]][:]
        else:
            gen[i] =  tmp[acc.index(sorted(acc)[i+20-PopuNum])]

def cross():
    tmp = Biont.gen[:]
    Parent = list(range(PopuNum))
    shuffle(Parent)
    for i in range(0,Popunum,2):
        StarPoint = randint(0,162)
        EndPoint = StarPoint + randint(1,163-StarPoint)
        tmpslice = tmp[Parent[i][StarPoint:EndPoint]
        tmp[Parent[i]][StarPoint:EndPoint] = tmp[Parent[i+1]][StarPoint:EndPoint] 
        tmp[Parent[i+1]][StarPoint:EndPoint] = tmpslice 





def bianyi():
    for i in range(PopuNum):
        r = random()
        if r < P:
            StarPoint = randint(1,162)
            EndPoint  = randint(1,164-StarPoint) + StarPoint
        Boint.gen[i][StarPoint:EndPoint] = abs(Boint.gen[i][StarPoint:EndPoint] - 1)



int __maint__():
    init()
    choose()
    cross()
    bianyi()
    Boint.CalAcc()
