import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Current_Data.csv')
X = dataset.iloc[:, 1:5].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X_train, y_train)
regressor.score(X_test,y_test)

# Predicting a new result
y_pred = regressor.predict(X_test)

# Visualising the Random Forest Regression results (higher resolution)    
# plotting the points  
plt.plot(X_test, y_pred, color='white', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12, label = 'Predicted Reading')
plt.plot(X_test, y_test, color='white', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='red', markersize=12, label = 'Real Reading')   
# naming the x axis 
plt.xlabel('Parameters') 
# naming the y axis 
plt.ylabel('Fault Current') 
# giving a title to my graph 
plt.title('New Graph') 
# function to show the plot 
plt.show() 
