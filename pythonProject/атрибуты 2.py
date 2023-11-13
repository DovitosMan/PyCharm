class Person():
    name = ""
    money = 0

    def out(self):  # self - ссылка на экземпляр класса
        print(self.name, 'has', self.money, 'dollars.')

    def changemoney(self, newmoney):
        self.money = newmoney


obj1 = Person()
obj2 = Person()
obj1.name = 'Bob'
obj2.name = 'Masha'
obj1.out()
obj2.out()
obj1.changemoney(150)
obj1.out()
