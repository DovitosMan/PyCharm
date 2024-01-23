import pandas as pd
import numpy as np
from sklearn import preprocessing, svm
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/dovitosman/Documents/GitHub/Python/csv/iris.data', header=None)
var_names = list(data.columns)  # получение имен признаков
X = data.iloc[:, :4].to_numpy()
labels = data.iloc[:, 4].to_numpy()
le = preprocessing.LabelEncoder()
Y = le.fit_transform(labels)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.5, random_state=0)
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

clf = LinearDiscriminantAnalysis()
y_pred = clf.fit(X_train, y_train).predict(X_test)
print((y_test != y_pred).sum())  # количество наблюдений, который были неправильно определены
print(clf.score(X_test, y_test))


def estimate_clf(clf):
    size_range = np.arange(0.05, 0.95, 0.05)
    test_results = []
    for size in size_range:
        X_train, X_test, y_train, y_test = \
            train_test_split(X, Y, test_size=size, random_state=234199)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        fault = (y_test != y_pred).sum()
        score = clf.score(X_test, y_test) * 100
        test_results.append([size, fault, score])
    return np.array(test_results)


def show_result(clf, results, param=''):
    plt.plot(results[:, 0], results[:, 1], label='# of faults')
    plt.plot(results[:, 0], results[:, 2], label='% of score')
    plt.title(clf.__name__)
    plt.legend()
    # plt.show()


test_results = estimate_clf(LinearDiscriminantAnalysis())
show_result(LinearDiscriminantAnalysis, test_results)

data_transformed = clf.transform(X_train)
labels = ['setosa', 'versicolor', 'virginica']
plt.figure()
colors = ['deepskyblue', 'coral', 'palegreen']
lw = 2
for color, i, label_ in zip(colors, [0, 1, 2], labels):
    plt.scatter(data_transformed[y_train == i, 0], data_transformed[y_train == i, 1], alpha=.8, color=color,
                label=label_)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.show()