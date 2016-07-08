
import numpy as np
from random import *
import pandas as pd
from sklearn.decomposition import PCA
from sklearn import  *



sto = pd.read_excel('yl_factors.xls')
label = pd.read_excel('YL3.xls')

#将数据按列归一化到[-1,1]
MinMax = preprocessing.MinMaxScaler([-1,1])
sto_scale = MinMax.fit_transform(sto)

#求出主成分和各自的比例,选择合适的主成分
pca = PCA(n_components=8)
newsto = pca.fit_transform(sto_scale)


trainData = sto_scale[:,12:24]
Label = np.reshape(label.iloc[:].values,[1200,])
best_score = 0

for j in np.linspace(1,1,1):
    for i in np.linspace(0.01,1,20):
        clf = svm.SVC(C = i, gamma = j, kernel = 'linear')
        # clf.fit(trainData,Label)
        score = cross_validation.cross_val_score(clf,trainData,Label,cv=5)
        score = score.mean()
        print(score)
        if score > best_score:
            best_score = score
            best_c = i
            best_g = j

# clf = svm.SVC(kernel = 'linear')
# clf.fit(trainData,Label)
# score = cross_validation.cross_val_score(clf, trainData, Label, cv=5)
# print(score)

print('result')
print(best_score)
print(best_c)
print(best_g)

