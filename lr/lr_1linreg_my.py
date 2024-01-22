import matplotlib.pylab as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
data = pd.read_csv('/Users/dovitosman/Documents/GitHub/Python/pythonProject/csv/cost_revenue_clean.csv')
# print(data.describe())
# print(data)

x = pd.DataFrame(data.production_budget_usd)
y = pd.DataFrame(data.worldwide_gross_usd)
model = LinearRegression().fit(x, y)

# сколько получим с 1го доллора
# print(model.coef_)

# отклонение
# print(model.intercept_)

plt.figure(figsize=(10,6))
plt.scatter(data.production_budget_usd, data.worldwide_gross_usd, alpha=0.3)
plt.plot(x, model.predict(x), color = 'red', linewidth = 3)
plt.xlabel('Бюджет')
plt.ylabel('Кассовый сбор')
plt.ylim(0,3000000000)
plt.xlim(0,450000000)
plt.show()

# коэф детерминации
print(model.score(x,y))

# сколько заработает фильм
print(model.predict([[200000000]]))

# не исползуемое
# X_train, X_test, y_train, y_test = train_test_split(spotify_youtube.Views, spotify_youtube.Stream, test_size=0.2, random_state=0)
# from sklearn.model_selection import train_test_split
# y_pred = model.predict(X_test)
# # plot a line, a perfit predict would all fall on this line
# x = np.linspace(0, 330, 100)
# y = x
# plt.plot(x, y)
# plt.show()