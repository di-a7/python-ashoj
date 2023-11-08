# def sum(a,b):
#     return a+b

# sum=lambda a,b:a+b
# print(sum(1,2))

# def fun(n):
#     return lambda a:a*n
# double=fun(2)
# print(double(10))
# print(double(50))

def fun(n):
    return lambda a:a*n
tri=fun(3)
print(tri(2))
print(tri(4))

# def fun(n):
#     return lambda a:a*n
# four=fun(4)
# print(four(2))
# print(four(4))

# cli,simple calculator or tic tac toe