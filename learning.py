from sympy import symbols, Eq, solve

# Создание списка уравнений
equations = ["x + y - 5", "2*x - y - 1"]

# Создание символьных переменных
x, y = symbols("x y")

# Преобразование уравнений в объекты типа Eq
eq_objects = [Eq(eval(equation), 0) for equation in equations]
print(eq_objects)
print(type(eq_objects))
# Решение системы уравнений
solution = solve(eq_objects, (x, y))

print(solution)
