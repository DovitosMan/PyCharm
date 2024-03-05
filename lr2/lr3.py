import tensorflow as tf
import pandas as pd
import keras
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from keras import Input
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.layers import Dense
from keras.models import Sequential

'''def plot_color_palette(palette: str):
    figure = sns.palplot(sns.color_palette())
    plt.xlabel("Color palette: " + palette)
    plt.show(figure)


palettes = ["deep", "muted", "pastel", "bright", "dark", "colorblind"]
for palette in palettes:
    sns.set(palette=palette)
    plot_color_palette(palette)'''
my_dataset = pd.read_csv('/Users/dovitosman/Documents/GitHub/Python/csv/wdbc.data', header=None)
# my_dataset = my_dataset.dropna()
X, y = my_dataset.drop(my_dataset[[0, 1]], axis=1), my_dataset[1]
y = y.replace({'B': 0, 'M': 1})
print(y.dtypes)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=1, stratify=y)
classifier = Sequential([
    Input(shape=(30,)),
    Dense(16, activation='relu'),
    Dense(8, activation='relu'),
    Dense(6, activation='relu'),
    Dense(1, activation='sigmoid')
])
classifier.compile(optimizer='rmsprop', loss='binary_crossentropy')
# classifier.summary()
classifier.fit(X_train, y_train, batch_size=1, epochs=100)
Y_pred = classifier.predict(X_test)  # подаём на вход обученной НС тестовый набор данных
Y_pred = [1 if y >= 0.5 else 0 for y in Y_pred]
total = 0
correct = 0
wrong = 0
y_test = y_test.values
for i in range(len(Y_pred)):
    total = total + 1
    if y_test[i] == Y_pred[i]:
        correct = correct + 1
    else:
        wrong = wrong + 1
print("Total " + str(total))
print("Correct " + str(correct))
print("Wrong " + str(wrong))
