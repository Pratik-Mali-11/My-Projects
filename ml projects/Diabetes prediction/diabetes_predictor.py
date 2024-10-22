import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# Load the dataset
d_dataset = pd.read_csv('diabetes.csv')

# Inspect the dataset
head1 = d_dataset.head()
# print(head1)

describe1  = d_dataset.describe()
# print(describe1)

shape1 = d_dataset.shape
# print(shape1)

val_counts = d_dataset['Outcome'].value_counts()
# print(val_counts)

outcome_mean = d_dataset.groupby('Outcome').mean()
# print(outcome_mean)

# Split the dataset into features and target
x1 = d_dataset.drop(columns='Outcome', axis=1)
x2 = d_dataset['Outcome']

# Standardize the features
scal = StandardScaler()
std_data = scal.fit_transform(x1)

# Assign standardized data back to x1
x1 = std_data

# Split the dataset into training and testing sets
train_x1, test_x1, train_x2, test_x2 = train_test_split(x1, x2, test_size=0.2, stratify=x2)

# Create the SVM classifier
classifierr = svm.SVC(kernel='linear')

# Fit the classifier on the training data
classifierr.fit(train_x1, train_x2)

# Training data prediction
prediction_train = classifierr.predict(train_x1)
acc_score = accuracy_score(train_x2, prediction_train)  # Corrected the arguments
# print("Accuracy score for training: ", acc_score)

# Test data prediction
prediction_test = classifierr.predict(test_x1)
acc_score2 = accuracy_score(test_x2, prediction_test)  # Corrected the arguments
# print("Accuracy score for testing: ", acc_score2)

# Predictive input data
input_data = (1,85,66,29,0,26.6,0.351,31)

# Convert the input data to numpy array
input_numpy = np.asarray(input_data)

# Reshape the data for prediction
reshaped_data = input_numpy.reshape(1, -1)

# Standardize the input data
data_std = scal.transform(reshaped_data)

# Make a prediction
prediction = classifierr.predict(data_std)
# print("Prediction for input data: ", prediction)

if prediction[0]==0:
    print("The person has diabetes")
else:
    print("The person has diabetes")