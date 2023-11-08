class house:
    
    def __init__(self,color,windows,door):
        self.color=color
        self.windows=windows
        self.door=door
    def __str__(self) -> str:
        return f"{self.color} House"
      
    def get_color(self):
        return f"This person house color is {self.color}"
    def set_color(self,color):
        self.color=color

ramhouse=house("yellow",6,1)
print(ramhouse)
