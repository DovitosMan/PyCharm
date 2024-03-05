import math
import random
import matplotlib.pyplot as plt
import sympy as sp
from sympy import sympify

N_Well = 5
Rk = 120
Fk = 8000
Fc = []
r = 0.1
X = []
Y = []
random.seed(5)
P = [8.5, 9, 7, 9.5, 11]  # МПа
mu = 2 * 10 ^ (-3)  # Па*с
k = 80 * 10 ^ (-3)  # Д
equation = []
for i in range(N_Well):
    X.append(random.randint(0, 100))
    Y.append(random.randint(0, 100))
for i in range(N_Well):
    # Fc = sp.symbols(f"Fc{i}")
    summ = []
    sum = ""
    iter_score = int(0)
    Fc.append(P[i] * k / mu)
    for j in range(N_Well):
        q = sp.symbols(f"q{j}")
        if i == j:
            summ.append(q * sp.log(Rk / r))
        else:
            r_well = math.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
            summ.append(q * sp.log(Rk / r_well))
        sum += f"{1/math.pi:.3}*{summ[j]}"
        if iter_score < N_Well - 1:
            sum += f" + "
            iter_score += 1

    equation.append(sp.Eq(sympify(Fk - Fc[i]), sympify(sum)))
for i in range(N_Well):
    q = sp.symbols(f"q{i}")
    print(q)
    solution = sp.solve(equation[i], (q))
    print(equation[i])
    # print(solution)
    # print(q)
    # print(type(equation))
    # print(type(q))
    # print(type(solution))
# print(solution)
# print(solution)
plt.scatter(X, Y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.grid(True)
# plt.show()
