#login agadi tapai register
#register username unique
#show users as number 3  if user are logged in 
users=[]
registered={}
islogin=False

def register():
    username=input("Username:")
    password=input("Password:")
    if username == registered.values():
        print("Username already exists.")
        return
    else:
        registered.update({"username":username,"password":password})
    users.append(registered)  
    print("Registration succuss.")   
    return
  
def login(username,password):
    if len(users)==0:
            print("User not registered.")
            yn=input("Register the user(y/n):")
            if yn=="y":
                register()
                return
    for user in users:
        if username == user['username'] and password == user['password']:
            global islogin
            islogin=True
        elif username == user['username'] and password != user['password']:
            print("Username or Password incorrect.")
            
        elif username != user['username']:
            print("Username or Password incorrect. Username may not exist")
            yn=input("Would you like to register account?(y/n):")
            if yn=="y":
                register()
                return
            
def checklog(username,password):
    for user in users:
        if username == user['username'] and password == user['password']:
            if islogin:
                print("User has logged in.")
                return
    print("User havent logged in.")

def logged():
    log=len(users)
    print(f"Logged in users: {log}")
            
while True:
    a=int(input("""
                1.Login
                2.Register
                3.Check if User is logged in
                4.Logged in users"""))

    if a==1:
        username=input("Enter Username:")
        password=input("Enter password:")
        login(username,password)
    elif a==2:
        register()
    elif a==3:
        username=input("Enter Username:")
        password=input("Enter password:")
        checklog(username,password)
    elif a==4:
        logged()