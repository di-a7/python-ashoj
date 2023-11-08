person={"name":"Ritu",
        "age":21,
        'hobbies':['coding','music','drawing','Reading books'],
        'family_member':({
                'Father':'Ram',
                'Mother':'Sita',
                'Brother':'Harry',
                'Sister':'Nitu'
        },)
        }

# print(person)
# print(type(person))
# print(person['hobbies'][0])
# print(person['hobbies'][3][8:-1])  
print(person['family_member'][0])
print(person['family_member'][0]['Sister'])
  