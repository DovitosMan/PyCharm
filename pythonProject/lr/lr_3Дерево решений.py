import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/dovitosman/Documents/GitHub/Python/pythonProject/csv/glass.csv')
X = df.drop('Type', axis=1)
y = df['Type']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
clf = DecisionTreeClassifier(criterion='entropy', max_depth=3)
y_pred = clf.fit(X_train, y_train).predict(X_test)
print((y_test != y_pred).sum())
print(accuracy_score(y_test, y_pred))
print(clf.tree_.n_leaves)
plt.subplots(1, 1, figsize=(10, 10))
tree.plot_tree(clf, filled=True)
plt.show()
#
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import tree
# from sklearn.decomposition import PCA
# from sklearn.model_selection import train_test_split
#
# df = pd.read_csv('/Users/dovitosman/Documents/GitHub/Python/pythonProject/csv/glass.csv')
#
# # Распределяем новые данные на трейн и тест
# labels = df.to_numpy('int')[:,-1] #последней цифры
# data = df.to_numpy('float')[:,:-1] #информация о строках
# pca = PCA(n_components =4)
# pca_data = pca.fit(data).transform(data)
# cdf = pca_data
#
# new_cdf = np.insert(cdf,4, [labels],axis = 1)
# X = new_cdf[:,:-1]
# y = new_cdf[:,-1]
# train_X, test_X, train_y, test_y = train_test_split(X,y, test_size= 0.2)
#
#
# # Обращаемся к дереву
# clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
# get_n_leaves = 6
# clf.fit(train_X, train_y)
# y_pred =clf.predict(test_X)
#
# # Проверка переобучения
# print('Accurancy on training set :',format(clf.score(train_X, train_y)))
# print('Accurancy on test_set:',format(clf.score(test_X,test_y)))
#
#
# # смотрим на итоговое дерево
# plt.subplots(1,1, figsize = (10,10))
# tree.plot_tree(clf, filled = True)
# plt.show()