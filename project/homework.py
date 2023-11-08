# family member dict that saves the name saves in the list, number of family member, 1st leter uppercase
members={}
while True:
    name=input("Name of family member: ")
    rel=input("Relation: ")
    members.update({rel:name})
    yn=input("Add a member(y/n):")
    if yn=="y":
        continue
    else:
        break

listm=[]
listm.append(members)
total=len(members)+1
print(members)

print(listm)
print(total)