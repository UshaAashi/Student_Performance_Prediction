# -*- coding: utf-8 -*-
"""Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/161S6FGY9C2xPd7a6HDK-9JvEyT27kJk6
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('/content/student_data.csv')

"""**1.2 Exploratory Data Analysis**"""

dataset.head()

dataset.tail()

dataset.info()

print(dataset.describe())

import seaborn as sns
plt.figure(figsize=(8, 6))
sns.histplot(data=dataset, x="Performance", bins=20, kde=True)
plt.title("Distribution of Student Performance")
plt.xlabel("Student Performance")
plt.ylabel("Frequency")
plt.show()

sns.pairplot(dataset, vars=["Hours Studied", "Previous Scores", "Duration of Sleep", "Sample Question Papers Practiced"], hue="Performance")
plt.show()

plt.scatter(dataset['Hours Studied'], dataset['Performance'], alpha=0.5)
plt.title('Scatter plot of Performance with Hours Studied')
plt.xlabel('Hours Studied')
plt.ylabel('Performance')
plt.show()

plt.scatter(dataset['Previous Scores'], dataset['Performance'], alpha=0.5)
plt.title('Scatter plot of Performance with Previous Scores')
plt.xlabel('Previous Scores')
plt.ylabel('Performance')
plt.show()

plt.scatter(dataset['Duration of Sleep'], dataset['Performance'], alpha=0.5)
plt.title('Scatter plot of Performance with Duration of Sleep')
plt.xlabel('Duration of Sleep')
plt.ylabel('Performance')
plt.show()

plt.scatter(dataset['Sample Question Papers Practiced'], dataset['Performance'], alpha=0.5)
plt.title('Scatter plot of Performance with Sample Question Papers Practiced')
plt.xlabel('Sample Question Papers Practiced')
plt.ylabel('Performance')
plt.show()

sns.boxplot(x="Extracurricular Activities", y="Performance", data=dataset)
plt.title("Extracurricular Activities vs Performance")
plt.show()

corr_matrix = dataset.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

"""**1.3 Split data set in train and test (80:20) ratio**"""

dataset['Extracurricular Activities'] = dataset['Extracurricular Activities'].replace(to_replace="Yes", value=1)
dataset['Extracurricular Activities'] = dataset['Extracurricular Activities'].replace(to_replace="No", value=0)

#Split Dataset in Train and Test (80:20) ratio
from sklearn.model_selection import train_test_split
X = dataset.drop("Performance", axis=1)
y = dataset["Performance"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

dataset.head()

dataset.info()

"""**1.4 Code for Model Training using Gradient Descent (Linear Regression)**"""

def model(X_train, y_train, learning_rate, iteration):
  m = y_train.size
  theta = np.zeros(X_train.shape[1],)
  loss_list = []

  for i in range(iteration):
    y_pred = np.dot(X_train, theta)
    loss = (1/(2*m))*np.sum(np.square(y_pred - y_train))
    d_theta = (1/m)*np.dot(X_train.T, y_pred - y_train)
    theta = theta - learning_rate*d_theta
    loss_list.append(loss)
    if(i%(iteration/10) == 0):
      print("Loss is:", loss)
  return theta, loss_list

iteration = 10000
theta, loss_list = model(X_train, y_train, 0.0001, 10000)

"""**1.5 Loss vs Epoch Curve**"""

rng = np.arange(0, iteration)
plt.plot(rng, loss_list)
plt.title('Loss vs Epoch curve')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()

"""**1.6 Performance Estimation**"""

student_data = np.array([[7, 95, 1, 7, 6]])
predicted_performance = np.dot(student_data, theta)
print(predicted_performance)

"""**1.7 Performance Evaluation**"""

#MSE error
y_pred = np.dot(X_test, theta)
error = (1/X_test.shape[0])*(np.sum(np.square(y_pred - y_test)))
print(error)

#R2 Score
r2 = 1 - (np.sum(np.square(y_test - y_pred)) / np.sum(np.square(y_test - np.mean(y_test))))
print(r2)

#Adjusted R2 Score
adjusted_r2 = 1 - ((1 - r2) * (len(y_test) - 1)) / (len(y_test) - X_test.shape[1] - 1)
print(adjusted_r2)