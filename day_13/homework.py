import os
while True:
    x=input("""
1.Create Note
2.Enter note
3.Open a file
4.Display list of files
5.Delete file
>>>""")
    if x=="1":
        a=input("Enter the file name:")
        f=open(f'{a}.txt','x')
        f.close()
    if x=="2":
        a=input("Enter the file name:")
        f=open(f'{a}.txt','a')
        b=input("Enter the Note:")
        f.write(b)
        f.close()
    if x =="3":
        a=input("Enter the file name:")
        f=open(f'{a}.txt')
        print(f.read())
        f.close()
    if x=="4":
        for x in os.listdir():
            if x.endswith('.txt'):
                print(x)
    if x=="5":
        d=input("File to delete:")
        os.remove(f"{d}.txt")