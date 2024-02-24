print("""
##########################
#     Calculator         #
#   (+)  addition        #
#   (-)  subtraction     #
#   (*)  multiplication  #
#   (/)  division        #
#   (**) exponentiation  #
#   (%)  mod             #
##########################
""")
state = True
while(state):
    number1 = float(input("1. number: "))
    number2 = float(input("2. number: "))
    selection = input("Please select a operation: ")
    if selection == "+":
        print("{0} + {1} = {2}".format(number1,number2,number1+number2))
    elif selection == "-":
        print("{0} + {1} = {2}".format(number1,number2,number1-number2))
    elif selection == "*":
        print("{0} + {1} = {2}".format(number1,number2,number1*number2))
    elif selection == "/":
        print("{0} + {1} = {2}".format(number1,number2,number1/number2))
    elif selection == "**":
        print("{0} + {1} = {2}".format(number1,number2,number1**number2))
    elif selection == "+":
        print("{0} + {1} = {2}".format(number1,number2,number1%number2))
    else:
        print("Invalid selection")
    print("do you break? Yes(Y) No(N)")
    selection2 = input("--> ")
    if selection2 == "Y":
        state =False
