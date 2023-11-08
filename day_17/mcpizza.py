class pizza:
    def base(self):
        print("Pizza Base")
        return self
    def sauce(self):
        print("Sauce")
        return self
    def veggies(self):
        print("Veggies")
        return self
    def cheese(self):
        print("cheese")
        return self
    def topping(self):
        print("Toppings")
        return self
p=pizza()
p.base().sauce().veggies().cheese().topping().cheese()