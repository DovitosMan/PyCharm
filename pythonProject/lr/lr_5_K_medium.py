import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.decomposition import PCA

# import dataset
dt = pd.read_csv('/Users/dovitosman/Documents/GitHub/Python/pythonProject/csv/data.csv')
dt = dt.drop(dt.columns[[1, 2, 3, 10,11,12,13,20,21,22,23,24,25,27,28,31,32]], axis=1)
labels = dt.to_numpy('int')[:,-1]

# нули вместо пропусков
dt = dt.fillna(0)

# проверка на отсутствующие данные
x = dt.isnull().sum()
x = dt.values[:, :]

# создание нового датасента из 5 компонент
dtset = preprocessing.minmax_scale(x)
pca = PCA(n_components=5 )
pca_dtset = pca.fit(dtset).transform(dtset)

# насколько информативная каждая компонента
y = sum(pca.explained_variance_ratio_)
print("pca.explained_variance_ratio_is ", y)

# берем самые информативные компоненты
plt.scatter(pca_dtset[:,0],pca_dtset[:,1],c=labels,cmap='brg',)
new_pca = pca_dtset[:,:-2]
# по первым двум компонентам
plt.show()

# разбиваем по методу локтя
clusterNum = 8
k_means = KMeans(init='k-means++', n_clusters=clusterNum, n_init='auto') # максимальное удаление от первой
k_means.fit(new_pca)
labels = k_means.labels_ #причисляет точки какому-то кластеру
print(labels)

# расстояние от центроида до точек
wcss = []
for i in range(1, 15):
    kmeans = KMeans(n_clusters=i, init='k-means++', n_init='auto')
    kmeans.fit(new_pca)
    wcss.append(kmeans.inertia_)
plt.plot (range(1, 15), wcss)
plt.title('Метод локтя')
plt.xlabel('Количество кластеров')
plt.ylabel('WCSS')
plt.show()

# итоговый плот
plt.scatter(pca_dtset[:,0],pca_dtset[:,1],c=labels,cmap='hsv',label = labels)
plt.show()
