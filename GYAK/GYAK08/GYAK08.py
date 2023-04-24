import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from LinearRegressionSkeleton import LinearRegression
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
X = df['petal width (cm)'].values
y = df['sepal length (cm)'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr = LinearRegression(epochs = 10000, lr = 0.001)
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

plt.scatter(X_test, y_test)
plt.plot([min(X), max(X)], [min(y_pred), max(y_pred)], color='red') 
plt.show()


# class LinearRegression:
#     def __init__(self, epochs: int = 1000, lr: float = 1e-3):
#         self.epochs = epochs
#         self.lr = lr
#         self.m = 0 #meredekség
#         self.c = 0 #metszés az x tengellyel

#         def fit(self, X: np.array, y: np.array):
#             n = float(len(X))

#             losses = []
#             for i in range(self.epochs):
#                 y_pred = self.m*X + self.c

#                 residuals = y_pred - y
#                 loss = np.sum(residuals ** 2)
#                 losses.append(loss)
#                 D_m = (-2/n) * sum(X * residuals)
#                 D_c = (-2/n) * sum(residuals)
#                 self.m = self.m + self.lr * D_m
#                 self.c = self.c + self.lr * D_c

#     def predict(self, X):
#         return self.m*X + self.c

    # def fit(self, X: np.array, y: np.array):
    #     self.X = X
    #     self.y = y
    #     self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    #     self.build()

    # def build(self):
    #     # Building the model
    #     n = float(len(self.X_train)) # Number of elements in X

    #     # Performing Gradient Descent 
    #     losses = []
    #     for i in range(self.epochs): 
    #         y_pred = self.m*self.X_train + self.c  # The current predicted value of Y

    #         residuals = y_pred - self.y_train #meghatározzuk a távolságot
    #         loss = np.sum(residuals ** 2)
    #         losses.append(loss)
    #         D_m = (-2/n) * sum(self.X_train * residuals)  # Derivative wrt m -> mennyivel kell változtatni m-t
    #         D_c = (-2/n) * sum(residuals)  # Derivative wrt c -> mennyivel kell változtatni c-t
    #         self.m = self.m + self.lr * D_m  # Update m
    #         self.c = self.c + self.lr * D_c  # Update c
    #         if i % 100 == 0:
    #             print(np.mean(self.y_train-y_pred))
    

    # def predict(self, X):
    #     return self.m*X + self.c