# -*- coding: utf-8 -*-
"""
Created on Tue Sep 5 00:15:15 2017

@author: prabhav
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

#Taking care of missing data
from sklearn.preprocessing import Imputer 
imputer = Imputer(missing_values='NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[: , 1:3])
X[: , 1:3] = imputer.transform(X[: , 1:3])

#Encoding categorical data
from sklearn.preprocessing import LabelEncoder ,OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0]) #Problem : Since 0<1<2 , it might appear that there is a relational order in countries 

onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)


from sklearn.cross_validation import train_test_split
X_train , X_test, Y_train , Y_test = train_test_split(X,Y,test_size = 0.2 , random_state = 0 )

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
X_train = sc_x.fit_transform(X_train)
X_test = sc_x.transform(X_test)