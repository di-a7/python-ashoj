class burger:
    def bun(self):
        print("bun")
        return self
    
    def patty(self):
        print("patty")
        return self
    
    def sauce(self):
        print("sauce")
        return self
    
b=burger()

b \
    .bun() \
    .patty() \
    .sauce() \
    .patty() \
    .bun()