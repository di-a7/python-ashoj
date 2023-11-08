# def hello():
#     print("Hello World")
#     hello()
# hello()
def num(n=0):
    print(n)
    if n==10:
        return
    num(n+1)
num()





# print(list(range(2,10)))



#using recursion recreate range function