import pandas as pd

from joblib import load
import json
import os

from sklearn.metrics import accuracy_score


# Set path for the input (model)

model_file = 'model.joblib'


# Set path for the input (test data)

test_data_file = 'test.csv'




# Load model
logit_model = load(model_file)

# Load data
df = pd.read_csv(test_data_file, sep=",")


# Split data into dependent and independent variables
X_test = df.drop('income', axis=1)
y_test = df['income']

# Predict
logit_predictions = logit_model.predict(X_test)

# Compute test accuracy
test_logit = accuracy_score(y_test,logit_predictions)

print("test accuracy:",test_logit)








