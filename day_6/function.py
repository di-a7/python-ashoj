# def hello():
#     print("Hello")

# hello()
# hello()
# hello()

# #function with parameter
# def hello(name,hobbie):
#     print(f"{name} have a great day.Enjoy {hobbie}")
    
# hello("JK","singing")


# create a simple calculator using function and if ,input and loop 
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

while True:   
    o=input("Operation to perform(+,-,*,/):")
    a=int(input("First Value:"))
    b=int(input("Second Value:"))
    if o=="+":
        print("Result:",add(a,b))
    elif o=="-":
        print("Result:",sub(a,b))
    elif o=="*":
        print("Result:",mul(a,b))
    elif o=="/":
        print("Result:",div(a,b))
    else:
        break
        
