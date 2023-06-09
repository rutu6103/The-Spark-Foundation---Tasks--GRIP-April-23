# -*- coding: utf-8 -*-
"""GRIP- Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UWBnNTm4zCS9G2TYqpmRs6QEazla0I4J

#TASK 1 : PREDICTION USING SUPERVISED Machine Learning

Predict the percentage of a student based on number of study hours

Presentor : Rutuja Kadam

# Importing libraries
"""

#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

"""

#Reading the data"""

Url = "http://bit.ly/w-data"
data = pd.read_csv(Url)

data.head(10)

data.tail(10)

data.info()

data.shape

data.describe()

data.isnull().sum()

data.duplicated().sum()

"""# Data Visualization"""

data.plot(x = "Hours", y = "Scores", style = "o")
plt.title("HOURS V/S PERCENTAGE")
plt.xlabel("Hours studied")
plt.ylabel("Percentage scored")
plt.show()

"""# Predict Outcomme Using Supervised Machine Learning

# Split the dataset for training
"""

x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 10)

"""# Select the model and train it"""

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x_train, y_train)

print("Successfully trained")

"""# PLotting regression line"""

line = reg.coef_*x + reg.intercept_

#plotting of test data
plt.scatter(x,y)
plt.plot(x, line, color="red")
plt.title("Hours V/S Percentage")
plt.xlabel("Hours studied")
plt.ylabel("Percentage Scored")
plt.show()

"""# Predicting the test set results"""

print(x_test)                     #Test data : in hours
y_pred = reg.predict(x_test)      #Predicting scores on the basis of test data
print(y_pred)

reg.score(x_test, y_test)
print("The R-square of the model is", reg.score(x_test, y_test))

"""# Visualizing the training set results"""

plt.scatter(x_train, y_train, color = "green")
plt.plot(x_train, reg.predict(x_train), c="r")
plt.title("Hours V/S Percentage\n Training set results")
plt.xlabel("Hours studied")
plt.ylabel("Percentage Scored")
plt.show()

"""# Visualizing Test results"""

plt.scatter(x_test, y_test, color="red")
plt.plot(x_train, reg.predict(x_train), color="blue")
plt.title("Hours V/S Percentage\n Test set results")
plt.xlabel("Hours studied")
plt.ylabel("Percentage Scored")
plt.show()

"""# Predicting the percentage of marks scored"""

#Comparing Actual vs Predicted values
df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
df

"""# Error Metrics


"""

from sklearn import metrics
print("Mean absolute error", metrics.mean_absolute_error(y_test, y_pred))

"""# Testing our data"""

hours = 9.25
our_pred = reg.predict([[hours]])
print("Number of hours = {}".format(hours))
print("Predicted score = {}".format(our_pred[0]))

"""Hence, the predicted score for a person studying 9.25 hours is 93.43229053722453% in an exam"""