import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('high_quality_synthetic_data.csv')
X = data[['IR', 'IY', 'IB', 'VR', 'VY', 'VB']]
y = data[['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8']]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model for each relay
models = {}
for i in range(1, 9):
    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train[f'L{i}'])
    models[f'L{i}'] = model

# Make predictions and evaluate
predictions = {}
accuracies = {}
for i in range(1, 9):
    pred = models[f'L{i}'].predict(X_test)
    predictions[f'L{i}'] = pred
    accuracies[f'L{i}'] = accuracy_score(y_test[f'L{i}'], pred)

# Average accuracy
average_accuracy = np.mean(list(accuracies.values()))
print(f'Average Accuracy: {average_accuracy}')

# Print individual accuracies and predictions
for i in range(1, 9):
    print(f'Accuracy for L{i}: {accuracies[f"L{i}"]}')
    print(f'Predictions for L{i}: {predictions[f"L{i}"]}')
