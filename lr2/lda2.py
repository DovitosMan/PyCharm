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

clf = svm.SVC()
y_pred = clf.fit(X_train, y_train).predict(X_test)
print((y_test != y_pred).sum())
print(clf.score(X, Y) * 100)
print(clf.score(X_test, y_test) * 100)

print(clf.support_vectors_)
print(clf.support_)
print(clf.n_support_)


def estimate_clf(clf):
    size_range = np.arange(0.05, 0.95, 0.05)
    test_results = []
    for size in size_range:
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=size, random_state=234199)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        fault = (y_test != y_pred).sum()
        score = clf.score(X_test, y_test) * 100
        test_results.append([size, fault, score])
    return np.array(test_results)


def show_result(clf, results):
    plt.plot(results[:, 0], results[:, 1], label='# of faults')
    plt.plot(results[:, 0], results[:, 2], label='% of score')
    plt.title(clf.__name__)
    plt.legend()
    plt.show()


test_results = estimate_clf(svm.SVC())
# show_result(svm.SVC, test_results)

for kernel in ['linear', 'poly', 'rbf', 'sigmoid']:
    test_results = estimate_clf(svm.SVC(kernel=kernel))
    # show_result(svm.SVC, test_results)

for degree in range(3, 10):
    test_results = estimate_clf(svm.SVC(kernel='poly', degree=degree))
    # show_result(svm.SVC, test_results)

for max_iter in [-1, 50, 100, 500]:
    test_results = estimate_clf(svm.SVC(max_iter=max_iter))
    # show_result(svm.SVC, test_results)

test_results = estimate_clf(svm.NuSVC(nu=0.01))
# show_result(svm.NuSVC, test_results)
test_results = estimate_clf(svm.LinearSVC(dual=True, max_iter=5000))
# show_result(svm.LinearSVC, test_results)
