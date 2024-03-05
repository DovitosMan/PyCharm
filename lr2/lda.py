import pandas as pd
import numpy as np
from sklearn import preprocessing
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
print((y_test != y_pred).sum())
print(clf.score(X_test, y_test)*100)


def estimate_clf(clf_1):
    size_range = np.arange(0.05, 0.95, 0.05)
    test_results1 = []
    for size in size_range:
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=size, random_state=234199)
        clf_1.fit(X_train, y_train)
        y_pred = clf_1.predict(X_test)
        fault = (y_test != y_pred).sum()
        score = clf_1.score(X_test, y_test) * 100
        test_results1.append([size, fault, score])
    return np.array(test_results1)


def show_result(clf2, results):
    plt.plot(results[:, 0], results[:, 1], label='faults')
    plt.plot(results[:, 0], results[:, 2], label='score')
    plt.title(clf2.__name__)
    plt.legend()
    plt.show()


test_results = estimate_clf(LinearDiscriminantAnalysis())
show_result(LinearDiscriminantAnalysis, test_results)

# data_transformed = clf.transform(X_train)
# labels = ['setosa', 'versicolor', 'virginica']
# plt.figure()
# colors = ['red', 'green', 'blue']
# for color, i, label_ in zip(colors, [0, 1, 2], labels):
#     plt.scatter(data_transformed[y_train == i, 0], data_transformed[y_train == i, 1], alpha=.8, color=color, label=label_)
# plt.legend(loc='best', shadow=False, scatterpoints=1)
# plt.show()

for solver in ['svd', 'lsqr', 'eigen']:
    test_results = estimate_clf(LinearDiscriminantAnalysis(solver=solver))
    # show_result(LinearDiscriminantAnalysis, test_results)

for shrinkage in ['auto', None]:
    test_results = estimate_clf(LinearDiscriminantAnalysis(shrinkage=shrinkage, solver='lsqr'))
    # show_result(LinearDiscriminantAnalysis, test_results)

priors = np.zeros(len(set(labels)))
# print(priors)
priors[0] = 0.7
priors[1:] = 0.3 / (len(set(labels)) - 1)
test_results = estimate_clf(LinearDiscriminantAnalysis(priors=priors))
show_result(LinearDiscriminantAnalysis, test_results)
