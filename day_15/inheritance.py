class grandfather:
    def __init__(self):
        print(f"Grandfather owns {self.car}")
    car="lambo"
    
class father(grandfather):
    def __init__(self):
        self.car="ferrari"
        super().__init__()
        print(f"Father owns {self.car}")
    house="luxery house"
    
class mother:
    jewel="diamond necklace"
class son(father,mother):
    game="ps5"
s=son()
# f=father()
# print(isinstance(father,object))
# print(f.car)

# print(s.house)
# print(s.car)
# print(s.jewel)
# print(s.game)


