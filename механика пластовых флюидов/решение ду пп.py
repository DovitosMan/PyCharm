import sympy as sp
import matplotlib.pyplot as plt
Pk = 10
Pg = 8
L = 100
x = sp.Symbol('x')
p = sp.Function('p')
C1, C2, Lk = sp.symbols('C1 C2 Lk')
eq = sp.Eq(p(x).diff(x, x), 0)
solution = sp.dsolve(eq, p(x))
print(solution)
constants = sp.solve([solution.subs(x, 0), solution.subs(x, L)], (C1, C2))
print(constants)
final_solution = solution.subs(constants)
print(final_solution)
values = []
x_values = range(L+1)
for i in x_values:
    final_solution_2 = final_solution.subs([(p(0), Pk), (p(L), Pg), (x, i)])
    value = final_solution_2.rhs
    values.append(value)
plt.plot(x_values, values)
plt.xlabel('x')
plt.ylabel('p')
plt.title('График функции p = x*(-p(0)/Lk + p(Lk)/Lk) + p(0)')
plt.grid(True)
plt.show()
