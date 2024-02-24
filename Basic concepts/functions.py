#Functions
#a function is defined using the def keyword.
#the functions must defined top of the program.
#------------------

#unparameters functions
def printText():
    print("Hello World")
printText()

#predefined functions
def welcome(name,split = " "):
    print("Welcome" +split+name)
print(welcome(input("Please enter your name: "),split="/"))
#print(welcome()) #TypeError: welcome() missing 1 required positional argument: 'name'

def mult(number1,number2):
    print("{0} * {1} = {2}".format(number1,number2,number1*number2))
mult(float(input("First number:")),float(input("Second number:")))

#order is not necessary.
def mult(number1,number2,number3):
    print("{0} * {1} = {2}".format(number1,number2,number1*number2*number3))
mult(number2 = float(input("First number:")),number1 = float(input("Second number:")),number3 = 10)
#mult(number2 = 8,number1 = 3,float(input("Second number:"))) #SyntaxError: positional argument follows keyword argument

def mult(number1,number2):
    return ("{0} * {1} = {2}".format(number1,number2,number1*number2))
print(mult(float(input("First number:")),float(input("Second number:"))))

def mult1(number1,number2):
    return number1 * number2
def mult2(number1,number2):
    print(number1 * number2)
print(mult1(14, 13))
print(mult2(14, 13))

def strText():
    x = "Hello" #local variable
    print(x)
strText()
#print(x) #NameError: name 'x' is not defined

y = "Hello"
def strText():
    y = "World" #local variable
strText()
print(y) #Hello

def strText():
    global z
    z = "World" #local variable
strText()
print(z) #NameError: name 'z' is not defined

def strText():
    global t
    t = "World" #local variable
strText() 
print(t)

def numbers(*infinite):
    print(infinite)
numbers(1,2,3,4,5,6)

def sayMyName(**infinite):
    print(infinite)
sayMyName(name="hazel",surname = "Nickholson")
#{'name': 'hazel', 'surname': 'Nickholson'}

#def strText1(p1): #IndentationError: expected an indented block after function definition on line 61
#strText1()
#print(p1)