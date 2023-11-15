import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

# import dataset
df = pd.read_csv('/Users/dovitosman/Documents/GitHub/Python/pythonProject/csv/glass.csv')
var_names = list(df.columns) #получение названий столбцов
labels = df.to_numpy('int')[:,-1] #последней цифры
data = df.to_numpy('float')[:,:-1] #информация о строках
data = preprocessing.minmax_scale(data)

# make plots
# fig, axs = plt.subplots(2,4)
# for i in range (data.shape[1]-1):
#     axs[i // 4, i % 4].scatter(data[:,i],data[:,(i+1)], c = labels, cmap='hsv')
#     axs[i//4, i % 4].set_xlabel(var_names[i])
#     axs[i // 4, i % 4]. set_ylabel(var_names[i+1])
#     fig.set_size_inches(20, 10)
# plt.show()

# PCA components
pca = PCA(n_components =4)
pca_data = pca.fit(data).transform(data)
print(sum(pca.explained_variance_ratio_),' д.ед.')

# print(pca.singular_values_)
# plt.scatter(pca_data[:,0],pca_data[:,1],c=labels,cmap='hsv',)
# plt.show()

# новые данные на обучение и тест
cdf = pca_data
new_cdf = np.insert(cdf,4, [labels],axis = 1)
X = new_cdf[:,:-1]
y = new_cdf[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size= 0.2)

# обращение к дереву
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
get_n_leaves = 6
clf.fit(X_train, y_train)
y_pred =clf.predict(X_test)

# Проверка
print('Accurancy on training set :',format(clf.score(X_train, y_train)))
print('Accurancy on test_set:',format(clf.score(X_test, y_test)))
# Итоговое дерево
plt.subplots(1,1, figsize = (25,25))
tree.plot_tree(clf, filled = True, fontsize=15)
plt.show()