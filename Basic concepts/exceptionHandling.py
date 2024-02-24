#Exception Handling (try- except - finally)
#-------------------------------------------
def devam():
    def div(a,b):
        return a / b
while True:
    try:
        number1 = float(input("Please enter first number...: "))
        number2 = float(input("Please enter second number...: "))
        if number2 == 0.0:
            raise Exception ("Please correct second number. it cannot be zero")
        else:
            print(devam().div(number1,number2))
            break
    except ZeroDivisionError as message:
        print("Second number cannot be  zero. \nReason of error: ",message)
        raise
    except ValueError as message:
        print("Please enter numerical values.\nReason of error: ",message)
        raise
    else:
        print("Error resolved")
    finally:
        print("The program has been terminated.")

