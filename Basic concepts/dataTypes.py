#data types
#---------------------

#Integer (4 bytes)
number1 = 2147483647
print(type(number1)) #<class 'int'>

#Float (8 bytes)
number2 = 4.5
print(type(number2)) #<class 'float'>

#complex
number3 = 4+2j
print(type(number3)) #<class 'complex'>

#boolean
state1 = True
state2 = False
print(type(state1)) #<class 'bool'>
print(type(state2)) #<class 'bool'>

#string
text = "Python"
print(type(text)) #<class 'str'>

#list []
#it can same or not values with data types. changable
myList = ["a", 1 ,2.4, True, 2j]
print(type(myList)) #<class 'list'>

#tuple ()
#it can same or not values with data types. unchangable only readable
myTuple = ("a", 1 ,2.4, True, 2j)
print(type(myTuple)) #<class 'tuple'>

#dictionary {} -> curly brackets
#it can same or not values with data types. unchangable only readable
myDict = {1:"a",2:1 ,3:2.4, 4:True, 5:2j}
print(type(myDict)) #<class 'dict'>

#casting
a = "Hello"
#a = int(a) #ValueError: invalid literal for int()
b = '1234'
b = int(b)
print(type(b)) #<class 'int'>
b = float(b)
print(type(b)) #<class 'float'>