dict={'name':'diya','age':21,'gender':'female'}

print(len(dict))

print(dict.keys())

print(dict.values())

for key,value in dict.items():
    print(f"{key}|{value}")
    
print(dict.get("name"))
print(dict.get("names","nothing"))

dict.pop("name")

dict.update({"age":20})

print(dict)