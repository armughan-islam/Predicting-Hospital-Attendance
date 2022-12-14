import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

from google.colab import files
files.upload()
noShows = pd.read_csv('/content/KaggleV2-May-2016.csv')

noShows.head()

noShows.rename(columns = { 'Hipertension': 'Hypertension',
                          'Handcap':'Handicap'},inplace=True)

noShows.head()

noShows.columns

noShows['Gender'].unique()

noShows['Gender'] = noShows['Gender'].map({'F':1, 'M':0})

noShows['No-show'] = noShows['No-show'].map({'Yes':1, 'No':0})

noShows.head()

noShows['ScheduledDay'] = noShows['ScheduledDay'].apply(np.datetime64)

noShows['ScheduledDay'].dt.date

noShows['AppointmentDay'] = noShows['AppointmentDay'].apply(np.datetime64)

noShows['AppointmentDay'].dt.date

noShows['WaitingTime'] = noShows['AppointmentDay'].dt.date - noShows['ScheduledDay'].dt.date

noShows['WaitingTime']

noShows.head()

noShows = noShows.drop('PatientId',axis=1)

noShows = noShows.drop('AppointmentID',axis=1)

noShows.head()

noShows['Age'].unique()

noShows['Neighbourhood'].nunique()

dummy_col = ['Neighbourhood']
noShows = pd.get_dummies(noShows, columns = dummy_col)

len(noShows[noShows['Scholarship']==1])

noShows.drop(['ScheduledDay','AppointmentDay'],axis=1,inplace=True)

noShows['WaitingTime'] = noShows['WaitingTime'].apply(lambda date: date.days)

# Training neural network

from sklearn.model_selection import train_test_split
X = noShows.drop('No-show',axis=1)
y = noShows['No-show']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)

y_train.shape

from sklearn.neural_network import MLPClassifier

model = MLPClassifier(hidden_layer_sizes=(5,2))

model.fit(X_train,y_train)

predictions = model.predict_proba(X_test)[:,1]

import sklearn.metrics as metrics 
fpr,tpr,threshold = metrics.roc_curve(y_test,predictions)
plt.plot(fpr,tpr)
plt.plot(y_test,y_test,'r-.')

