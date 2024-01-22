class Person():  # Создание пустого класса
    pass
Person.money = 150  # Создание атрибута объекта класса

obj1 = Person()  # Создание экземпляра класса
obj2 = Person()  # Создание экземпляра класса
obj1.name = 'Bob'	# Создание атрибута экземпляра класса
obj2.name = 'Masha'	# Создание атрибута экземпляра класса

print(obj1.name, 'has', obj1.money, 'dollars.')  # Вывод
print(obj2.name, 'has', obj2.money, 'dollars.')  # Вывод


