import sympy as sp
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt
from sympy import sympify

x = sp.Symbol('x')
p = sp.Function('p')
C1, C2, Lk = sp.symbols('C1 C2 Lk')
eq = sp.Eq(p(x).diff(x, x), 0)
solution = sp.dsolve(eq, p(x))
print(solution)
constants = sp.solve([solution.subs(x, 0), solution.subs(x, 100)], (C1, C2))
# constants = sp.solve([solution.subs({x: xk}, {p: pk}), solution.subs({x: xg}, {p: pg})], (C1, C2))
print(constants)
final_solution = solution.subs(constants)
print(final_solution)
Pk = 10
Pg = 8
L = 100
values = []
for i in range(101):
    final_solution_2 = final_solution.subs([(p(0), Pk), (p(100), Pg), (x, i)])
    value = final_solution_2.rhs
    values.append(value)
x_values = range(101)
plt.plot(x_values, values)
plt.xlabel('x')
plt.ylabel('p')
plt.title('График функции p = x*(-p(0)/Lk + p(Lk)/Lk) + p(0)')
plt.grid(True)
plt.show()
