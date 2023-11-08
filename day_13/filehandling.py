import os
from time import sleep
try:
    f=open('helo.txt','x')
    # print(f.read())
    # print(f.readlines())
    # print(f.readline())
    # print(f.read(5))
    # f.write("\nSend me your location.")
    f.close()
    sleep(4)
    os.remove('helo.txt')
except FileExistsError:
    print("File already exists.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred.",e)
    