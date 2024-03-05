import sympy as sp
from sympy import diff, Eq
import matplotlib.pyplot as plt

# Дано
L = 14000
Pk = 10
Pg = 8
Rc = 14


def creating_plot(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.xlabel("Расстояние от скважины, см")
    plt.ylabel("Давление, МПа")
    plt.ylim(8, Pk)
    plt.xlim(0, L)
    plt.title("График функции d^2*P/dx^2")
    plt.grid(True)
    plt.show()


def solver(length, well_radius):
    r = sp.Symbol("r")
    p = sp.Function("p")
    C1, C2, Lk = sp.symbols("C1 C2 Lk")
    eq = Eq(diff(p(r), r, r) + (1 / r) * diff(p(r), r), 0)
    print(f"Я напечатал eq \n {eq}")
    solution = sp.dsolve(eq, p(r))
    print(f"Я напечатал solution \n {solution}")
    constants = sp.solve(
        [
            solution.subs({r: well_radius, p(well_radius): Pk}),
            solution.subs({r: length, p(length): Pg}),
        ],
        (C1, C2),
    )
    print(f"Я напечатал constants \n {constants}")
    final_solution = solution.subs(constants)
    print(f"Я напечатал final_solution \n{final_solution}")
    pressure = []
    x_values = range(Rc, L + 1, 10)
    for i in range(Rc, L + 1, 10):
        if i == 0:
            continue
        final_solution_2 = final_solution.subs({p(Rc): Pg, p(L): Pk, r: i})
        final_solution_2 = final_solution_2.evalf()
        final_solution_3 = final_solution_2.subs("p(14)", 8)
        pressure.append(final_solution_3.rhs)
        print(final_solution_3)
    # print(x_values)
    # print(pressure)
    creating_plot(x_values, pressure)
    return final_solution


result_of_eq = solver(L, Rc)
