import numpy as np
from sklearn import svm
import csv
import pandas as pd 
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

X = pd.read_csv("c:/users/pratyushsnehi10/desktop/project_ml/train_X.csv", header=None)
Y = pd.read_csv("c:/users/pratyushsnehi10/desktop/project_ml/train_Y.csv", header=None)
test_X = pd.read_csv("c:/users/pratyushsnehi10/desktop/project_ml/test_X.csv", header=None)
test_Y = pd.read_csv("c:/users/pratyushsnehi10/desktop/project_ml/test_Y.csv", header=None)

model = svm.SVC(kernel='linear', C=1, gamma = 1)
model.fit(X,Y.values.ravel())
predict_Y = model.predict(test_X)
print predict_Y
acc = accuracy_score(test_Y.values.ravel(),predict_Y)
print acc

clf = GaussianNB()
clf.fit(X,Y.values.ravel())
predict1_y = clf.predict(test_X)
print predict1_y
acc1 = accuracy_score(test_Y.values.ravel(),predict1_y)
print acc1

rf = RandomForestClassifier(n_estimators=100)
rf.fit(X, Y.values.ravel())
results = rf.predict(test_X)
print results
acc2 = accuracy_score(test_Y.values.ravel(),results)
print acc2 
