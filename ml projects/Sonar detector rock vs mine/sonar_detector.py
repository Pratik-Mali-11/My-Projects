import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Data collection and processing

#loading dataset to pandas dataframe

data = pd.read_csv('sonar_data.csv',header=None)

print('data head: ',data.head(),'\n')

print('data description:',data.describe(),'\n')

print('data shape: ',data.shape,'\n')

print('group by','\n',data.groupby(60).mean(),'\n')

X= data.drop(columns=60,axis=1)
Y= data[60]
print('X','\n',X,'\n')
print('Y','\n',Y,'\n')

X_train ,X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=1)

print(X.shape,X_train.shape,X_test.shape)

print(X_train)
print(Y_train)

log_model = LogisticRegression()

log_model.fit(X_train,Y_train)

X_train_prediction = log_model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train,X_train_prediction)

print("Training Accuracy:",training_data_accuracy)

X_test_prediction = log_model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test,X_test_prediction)

print("Test Accuracy:",test_data_accuracy)

ip_data=(0.0087,0.0046,0.0081,0.0230,0.0586,0.0682,0.0993,0.0717,0.0576,0.0818,0.1315,0.1862,0.2789,0.2579,0.2240,0.2568,0.2933,0.2991,0.3924,0.4691,0.5665,0.6464,0.6774,0.7577,0.8856,0.9419,1.0000,0.8564,0.6790,0.5587,0.4147,0.2946,0.2025,0.0688,0.1171,0.2157,0.2216,0.2776,0.2309,0.1444,0.1513,0.1745,0.1756,0.1424,0.0908,0.0138,0.0469,0.0480,0.0159,0.0045,0.0015,0.0052,0.0038,0.0079,0.0114,0.0050,0.0030,0.0064,0.0058,0.0030)

#chaning the data to numpy array
ipdata_numpyarr = np.asarray(ip_data)

#reshaping the input data

ipdata_reshaped = ipdata_numpyarr.reshape(1,-1)

prediction = log_model.predict(ipdata_reshaped)
print(prediction)

if(prediction[0]=='R'):
  print("The object is a rock")
else:
  print("The object is a mine")