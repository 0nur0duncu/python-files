#variables
#---------------
"""
we don't have to write the variables as following.
121abc
-abc
+abc
*abc
/abc
ğİç -->no turkish characters
abs -->function in python
1234
a b c
we should wrtite as following.
_abc
abc
a1

variable notations
------------------------
mySecretWorld -->camelcase
MySecretWorld -->pascal notation
PI_NUMBER or pi_number -->snake(underscore) notation
intTotal or strTotal -->hungarian notation
PINUMBER --> uppercase
pinumber --> lowercase
"""
#error
#print = "Hello world" #TypeError: 'str' object is not callable
#print("hi") 

a = "Hello world"
print(a) #Hello world
print(type(a)) #<class 'str'>

b = 5
print(type(b)) #<class 'int'>
c = 4.7
total = b + c
print(total) #9.7
mult = b * c
print(mult) #23.5
div = b / c
print(type(div)) #<class 'float'>
print(div) #1.0638297872340425
abst = b - c
print(abst) #0.2999999999999998
print(total * 2) #19.4

#variable swap
_a = 5
_b = 6
_c = 7
_d = 8

_a , _b = _c , _d

print(_a) #7
print(_b) #8

#assign variables each other
a = b
print(a) #5
print(b) #5

#single line assign value to variables
e = f = g = c
print(e) #4.7
print(f) #4.7
print(g) #4.7

#change the type of variable
print(type(_c)) #<class 'int'>
_c = str(_c)
print(type(_c)) #<class 'str'>

s = "abc"
t = "123"
print(type(s)) #<class 'str'>
print(type(t)) #<class 'str'>
#s = int(s) #ValueError: invalid literal for int() with base 10: 'abc'
t = int(t)
print(type(t)) #<class 'int'>