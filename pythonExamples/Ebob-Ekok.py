def ebob(number1,number2):
    great = number1
    if(number2 > number1):
        great = number2
    while(True):
        if(great % number1 == 0 and great % number2 ==0 ):
            return great
            break
        great += 1

def ekok(number1,number2):
    small = number1
    if(number2 < number1):
        small = number2
    while(True):
        if(number1 % small == 0 and number2 % small ==0 ):
            return small
            break
        small -= 1