# import numpy as np
# from sklearn.linear_model import LinearRegression
#
# x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
# y = np.array([5, 20, 14, 32, 22, 38])
#
# # print(x)
# # model = LinearRegression()
# # model.fit(x, y)
#
# model = LinearRegression().fit(x, y)
#
# r_sq = model.score(x, y)
# print('coefficient of determination:', r_sq)
# print('intercept:', model.intercept_)
# print('slope:', model.coef_)
#
# y_pred = model.predict(x)
# print('predicted response: ', y_pred, sep='\n')


import matplotlib.pylab as plt
import numpy as np
# matplotlib inline
from sklearn.linear_model import LinearRegression
from sklearn import datasets

diabetes = datasets.load_diabetes()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.2, random_state=0)
# There are three steps to model something with sklearn
model = LinearRegression().fit(X_train, y_train)

y_pred = model.predict(X_test)
plt.plot(y_test, y_pred, '.')

# plot a line, a perfit predict would all fall on this line
x = np.linspace(0, 330, 100)
y = x
plt.plot(x, y)
plt.show()