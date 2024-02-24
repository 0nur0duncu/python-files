# numerical Types (INT - FLOAT - COMPLEX)
#-----------------------------------------------

"""
operators
----------------
* multiplication
+ summation
- subtraction
/ divide
"""

#integer type there is no dot.
print(3) #3

#float type there is dot. 
print(2.5) #2.5

#complex type real and imaginary section
print(2 + 10j) #(2+10j)

#sum of two float
print(2.3 + 2.7) #5.0

#sum of float and integer
print(2.3 + 2) #4.3

#sum of two integer
print(4 + 2) #6

#sum of two complex type
print((2 + 10j) + (5 + 4j)) #(7+14j)

#sum of complex and int
print(5 + (5 + 4j)) #(10+4j)

#sum of complex and float
print(5.9 + (5 + 4j)) #(10.9+4j)

#sum of string and int
#print("hello" + 5) #TypeError: can only concatenate str (not "int") to str

#sum of string and float
#print(2.4 + "hello") #TypeError: unsupported operand type(s) for +: 'float' and 'str'

#subtract of two float
print(2.3 - 2.7) #-0.40000000000000036

#subtract of float and integer
print(2.3 - 2) #0.2999999999999998

#subtract of two integer
print(4 - 2) #2

#subtract of two complex type
print((2 + 10j) - (5 + 4j)) #(-3+6j)

#subtract of complex and int
print(5 - (5 + 4j)) #-4j

#subtract of complex and float
print(5.9 - (5 + 4j)) #(0.9000000000000004-4j)

#subtract of string and int
#print("hello" - 5) #TypeError: unsupported operand type(s) for -: 'str' and 'int'

#subtract of string and float
#print(2.4 - "hello") #TypeError: unsupported operand type(s) for -: 'float' and 'str'

#multiply by two float
print(2.3 * 2.7) #6.21

#multiply by float and integer
print(2.3 * 2) #4.6

#multiply by two integer
print(4 * 2) #8

#multiply by two complex type
print((2 + 10j) * (5 + 4j)) #(-30+58j)

#multiply by complex and int
print(5 * (5 + 4j)) #(25+20j)

#multiply by complex and float
print(5.9 * (5 + 4j)) #(29.5+23.6j)

#multiply by string and int
print("hello" * 5) #hellohellohellohellohello

#multiply by string and float
#print(2.4 * "hello") #TypeError: can't multiply sequence by non-int of type 'float'

#divided by two float
print(2.3 / 2.7) #0.8518518518518517

#divided by float and integer
print(2.3 / 2) #1.15

#divided by two integer
print(4 / 2) #2.0

#divided by two complex type
print((2 + 10j) / (5 + 4j)) #(1.2195121951219514+1.024390243902439j)

#divided by complex and int
print(5 / (5 + 4j)) #(0.6097560975609757-0.48780487804878053j)

#divided by complex and float
print(5.9 / (5 + 4j)) #(0.7195121951219513-0.5756097560975612j)

#divided by string and int
#print("hello" / 5) #TypeError: unsupported operand type(s) for /: 'str' and 'int'

#divided by string and float
#print(2.4 / "hello") #TypeError: unsupported operand type(s) for /: 'float' and 'str'

print(2 * 5 / 7 + 9) #10.428571428571429
print(2 + 5 /(2 * 9 + 4) / 9) #2.025252525252525