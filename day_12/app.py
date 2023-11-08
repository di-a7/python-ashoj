users=[{"username":"user1","password":"12345"},{"username":"user2","password":"1234567"}]
islogin=False
def login(username,password):
    for user in users:
        if username == user['username'] and password == user['password']:
            global islogin
            islogin=True
        
def checklog():
    if islogin:
        print("User has logged in.")
        return
    print("User havent logged in.")
while True:
    a=int(input("""
                1.Login
                2.Check if User is logged in"""))
    if a==1:
        username=input("Enter Username:")
        password=input("Enter password:")
        login(username,password)
    else:
        checklog()

