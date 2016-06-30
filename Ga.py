
import numpy as np
from random import *
import pandas as pd
from sklearn.decomposition import PCA
from sklearn import  *



sto = pd.read_excel('yl_factors.xls')
label = pd.read_excel('YL.xls')

MinMax = preprocessing.MinMaxScaler([-1,1])
sto_scale = MinMax.fit_transform(sto)
print(type(sto_scale))
pca = PCA(n_components=12)
newsto = pca.fit_transform(sto_scale)


trainData = newsto
Label = np.reshape(label.iloc[:].values,[1200,])
best_score = 0

for j in np.linspace(0.01,1,100):
    for i in np.linspace(0.1,100,100):
        clf = svm.SVC(C = i, gamma = j, kernel = 'rbf')
        # clf.fit(trainData,Label)
        score = cross_validation.cross_val_score(clf,trainData,Label,cv=5)
        score = score.mean()
        print(score)
        if score > best_score:
            best_score = score
            best_c = i



print(best_score)
print(best_c)

