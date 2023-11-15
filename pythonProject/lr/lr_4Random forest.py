import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# import dataset
df = pd.read_csv('/Users/dovitosman/Documents/GitHub/Python/pythonProject/csv/glass.csv')
var_names = list(df.columns)
labels = df.to_numpy('int')[:, -1]  # метки классов
data = df.to_numpy('float')[:, :-1]  # описательные признаки
data = preprocessing.minmax_scale(data)

# make plots
# fig, axs = plt.subplots(2, 4)
# for i in range(data.shape[1] - 1):
#     axs[i // 4, i % 4].scatter(data[:, i], data[:, (i + 1)], c=labels, cmap='hsv')
#     axs[i // 4, i % 4].set_xlabel(var_names[i])
#     axs[i // 4, i % 4].set_ylabel(var_names[i + 1])
# plt.show()

# PCA components
pca = PCA(n_components=4)
pca_data = pca.fit_transform(data)
print(pca.explained_variance_ratio_)

# print(pca.singular_values_)
# plt.scatter(pca_data[:, 0], pca_data[:, 1], c=labels, cmap='hsv')
# plt.show()

# новые данные на обучение и тест 1PCA
cdf = pca_data
new_cdf = np.insert(cdf, 4, [labels], axis=1)
# print(new_cdf)
X1 = new_cdf[:, :-1]
y1 = new_cdf[:, -1]
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2)
sl = RandomForestRegressor(n_estimators=100, oob_score=True, random_state=1)
sl.fit(X1_train, y1_train)
a1 = sl.predict(X1_test)

# новые данные на обучение и тест 2PCA
cdf1 = data
new_cdf1 = np.insert(cdf1, 9, [labels], axis=1)
X2 = new_cdf1[:, :-1]
y2 = new_cdf1[:, -1]
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2)
sel = RandomForestRegressor(n_estimators=100, oob_score=True, random_state=1)
sel.fit(X2_train, y2_train)
a2 = sel.predict(X2_test)

# плоты после снижения размерности
plt.subplot(1, 2, 1)
plt.scatter(y2_test, a2, color="red")
plt.title('1st')
plt.subplot(1, 2, 2)
plt.title('2nd')
plt.scatter(y1_test, a1, color="yellow")
plt.show()
# Проверка до
print('Accurancy on training set before PCA :', (sel.score(X2_train, y2_train)))
print('Accurancy on test_set before PCA :', (sel.score(X2_test, y2_test)))
# Проверка после
print('Accurancy on training set after PCA :', (sl.score(X1_train, y1_train)))
print('Accurancy on test_set after PCA :', (sl.score(X1_test, y1_test)))