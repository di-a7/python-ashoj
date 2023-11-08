class Person:
    def __init__(self):
        self.name="Ram"
        self._age=12
        self.__sell="17k"
    @property    
    def sell(self):
        return self.__sell
    @sell.setter
    def sell(self,sell):
        self.__sell=sell
    # salary=property(get_salary.set_salary)
person=Person()
print(person.name)
print(person._age)
# person.set_salary("19k")
# print(person.get_salary())
person.sell="19k"
print(person.sell)