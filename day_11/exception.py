while True:
    try:
        number=int(input("Enter a number:"))
        num=int(input("Enter second number:"))
        print(number/num)
    except ZeroDivisionError:
        print("Number cannot be divided by zero.")
    # except ValueError:
    #     print("Integer not entered.")
    except Exception as e:
        raise Exception("Unexpected error occured")
        print("Unexpected error occured.")
