import sympy as sp
import matplotlib.pyplot as plt

# Дано
L = 100
Pk = 10
Pg = 8


def creating_plot(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.xlabel("Расстояние от скважины, м")
    plt.ylabel("Давление, МПа")
    plt.ylim(0, Pk)
    plt.xlim(0, L)
    plt.title("График функции d^2*P/dx^2")
    plt.grid(True)
    plt.show()


def solver(length):
    x = sp.Symbol("x")
    p = sp.Function("p")
    C1, C2 = sp.symbols("C1 C2")
    print(p)
    eq = sp.Eq(p(x).diff(x, x), 0)
    print(f"Я напечатал eq \n {eq}")
    solution = sp.dsolve(eq, p(x))
    print(f"Я напечатал solution \n {solution}")
    constants = sp.solve([solution.subs(x, 0), solution.subs(x, length)], (C1, C2))
    print(f"Я напечатал constants \n {constants}")
    final_solution = solution.subs(constants)
    print(f"Я напечатал final_solution \n{final_solution}")
    pressure = []
    x_values = range(L + 1)
    for i in x_values:
        final_solution_2 = final_solution.subs([(p(0), Pk), (p(L), Pg), (x, i)])
        print(final_solution_2)
        value = final_solution_2.rhs
        pressure.append(value)
    creating_plot(x_values, pressure)
    return final_solution


result_of_eq = solver(length=L)
print(result_of_eq)
