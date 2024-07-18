import pandas as pd

import json
import os
import joblib

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Set path to inputs

train_data_file = 'train.csv'


# Read data
df = pd.read_csv(train_data_file, sep=",")

# Split data into dependent and independent variables
X_train = df.drop('income', axis=1)
y_train = df['income']


# Model 
logit_model = LogisticRegression(max_iter=10000)
logit_model = logit_model.fit(X_train, y_train)

print("Trained model accuracy:",accuracy_score(logit_model.predict(X_train),y_train))

# save
joblib.dump(logit_model, "model.joblib") 







