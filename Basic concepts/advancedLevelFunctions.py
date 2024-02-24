#Advanced Level Functions
#---------------------------------

#Nested functions

def hi(): #outer function
    print("Hi everyone...")
    def hello(): #inner function
        print("Hello everyone...")
    hello()
#hi()
#hi().hello()#AttributeError: 'NoneType' object has no attribute 'hello'

#closure and decorators

def hi(): #outer function
    print("Hi everyone...")
    def hello(): #inner function
        print("Hello everyone...")
    return hello
#test = hi()
#test()
#hi() #Hi everyone...#only outer func

def hi(name): #outer function

    def hello(): #inner function
        print("Hello "+name)
    return hello
#test = hi("edward") #Hello edward
#test()

def shape(func):
    def prnt():
        print("*****\n" + func() + "\n*****")
    return prnt
"""def test(): 
    return "Nicolai"
prnt_shape = shape(test) #decorator
prnt_shape() #*****
             #Nicolai
             #***** """
#or

@shape #decorator
def test(): 
    return "Nicolai"
#test() #*****
       #Nicolai
       #*****

def dash(func):
    def prnt():
        return "----------\n" + func() + "\n----------"
    return prnt


def asterisk(func):
    def prnt():
        return "**********\n" + func() + "\n**********"
    return prnt

@dash #outer
@asterisk #inner
def test():
    return "Trump"

#print(test())
"""
----------
**********
Trump
**********
----------
"""

#recursive function

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    return fibonacci(number-1) + fibonacci (number - 2)

#for i in range(10):
#    print(fibonacci(i),end=" ")
#0 1 1 2 3 5 8 13 21 34 

#Anonymous func-lambda

def cube(number):
    return number * number * number
#print(cube(10))

#or

cube = lambda x: x*x*x
#print(cube(10)) #1000
#nameSurname = lambda name,surname : f"Hi {name.title()} {surname.title()}" #first char is greater.
#print(nameSurname("onur","oduncu")) #Hi Onur Oduncu

#or

nameSurname = (lambda name,surname : f"Hi {name.title()} {surname.title()}") ("onur","oduncu") #first char is greater.
#print(nameSurname) #Hi Onur Oduncu

age = 18
driverLicence = lambda age: "You can get it." if age>=18 else "Sorry"
print(driverLicence(age)) #You can get it.

#iterator

numbers = (1,2,4,6,8,9) #array tuple list etc.
iterator = iter(numbers)

print(next(iterator)) #1
print(next(iterator)) #2
print(next(iterator)) #4
print(next(iterator)) #6
print(next(iterator)) #8
print(next(iterator)) #9
#print(next(iterator)) #StopIteration

#generator

generator = (x for x in range(20))
for i in generator:
    print(i,end=" ")

#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
print()
for j in generator:
    print(j,end=" ")
#no output

#or
def generator(x):
    for i in x:
        yield i

produce = generator([1,2,3,4,5])
for i in produce:
    print(i,end=" ")

#1 2 3 4 5

for j in produce:
    print(j,end=" ")
#no output

print()
#built-in functions
#print() len() input()

#bin
print(bin(20)) #0b10100

#bytes--unchangable
value = bytes(5)
print(value) #b'\x00\x00\x00\x00\x00'
print(value[0]) #0
print(value[1]) #0
print(value[2]) #0
print(value[3]) #0
#print(value[5]) #IndexError: index out of range
#value[0] = 5 #TypeError: 'bytes' object does not support item assignment

#bytearray --changable
value = bytearray(5)
print(value) #bytearray(b'\x00\x00\x00\x00\x00')
print(value[0]) #0
print(value[1]) #0
print(value[2]) #0
print(value[3]) #0
value[0] = 5 

print(chr(250)) #ú
print(chr(256)) #Ā

print(dir()) #variables,functions etc.
"""
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'age', 'asterisk', 'cube', 'dash', 'driverLicence', 'fibonacci', 'generator', 'hi', 'i', 'iterator', 'nameSurname', 'numbers', 'produce', 'shape', 'test', 'value']
"""
print(dir(list()))
"""
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""

#eval() it can use variables
x = 10
print(eval("x + 2*5")) #20
print(eval("2*5 + 5**5")) #3135

#exec() it can do assign and other command
print(exec("5*5")) #None #it cannot return a value
exec("k = 10")
exec("print('hi')") #hi #it can implement execute only print() built in function
print(dir())
"""
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'age', 'asterisk', 'cube', 'dash', 'driverLicence', 'fibonacci', 'generator', 'hi', 'i', 'iterator', 'k', 'nameSurname', 'numbers', 'produce', 'shape', 'test', 'value', 'x']
"""

#filter --logical (*)
number = range(10)
def isSingle(x):
    if x % 2 ==1:
        return True
    return False

s_numbers = filter(isSingle,number)
# it have to write '*' in front of the  variable
print(*s_numbers) #1 3 5 7 9

#format() function
print(format(5,".3f")) #5.000
print(format(500,"8.3f")) #500.000

#help() function

#print(help(help))
#print(?append)

#isinstance() function
print(isinstance("onur",str)) #True
print(isinstance(2j,complex)) #True

#map() function
number2 = range(10)
print(*map(cube, number2)) #0 1 8 27 64 125 216 343 512 729
print(map(cube, number2)) #<map object at 0x0000029D361136D0>

#ord() function

print(ord("5")) #53
print(ord("*")) #42

#zip() function

members = ["a", "b", "c"]
number3 = [1, 2, 3]
print(zip(members,number3)) #<zip object at 0x00000160BA005F80>
print(*zip(members,number3)) #('a', 1) ('b', 2) ('c', 3)
mn = zip(members,number3)
mn = list(mn)
print(mn) #[('a', 1), ('b', 2), ('c', 3)]

import builtins
print(dir(builtins))
"""
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
"""