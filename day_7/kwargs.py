# def person(**desc):
#     print(desc["name"],desc["age"])
#     print(desc)
    
# person(name="asdf",age=31,gender="male")

#5 people
# my name is ____ and age is ____ and my hobies
def desc(**d):
    print(f"My name is {d['name']}, age is {d['age']} and my hobbies are {d['hobby'][0]}, {d['hobby'][1]}.")
    
desc(name="zayn",age=35,hobby=("drawing","cooking"))
desc(name="Meril",age=19,hobby=("sleeping","reading"))
desc(name="Aliza",age=25,hobby=("knitting","singing"))
desc(name="Zion",age=20,hobby=("gamming","reading"))
desc(name="Lisa",age=28,hobby=("dancing","eating"))
