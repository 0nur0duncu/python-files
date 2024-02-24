#Arithmetic operators
#------------------------------
"""
Arithmetic operators
-----------------------
* multiplication
+ summation
- subtraction
/ divide
% mod
** exponentiation
// full division

comparison operators
------------------------
== equal
!= not equal
> greater than
< smaller than
>= greater and equal
<= smaller and equal

logical operators
and
or
not

assignment operators
------------------------
= assign right to left
+= value = rightValue + leftValue
-= value = rightValue - leftValue
*= value = rightValue * leftValue
/= value = leftValue / rightValue
%= value = leftValue % rightValue
//= value = leftValue // rightValue
**= value = leftValue ** rightValue
"""

#Arithmetic operators
print(2*2) #4
print(2-2) #0
print(2+2) #4
print(2 / 2) #1.0
print(2**2) #4
print(6 & 3) #2
print(8 / 3) #2.6666666666666665
print(8 // 3) #2

#comparison operators
print(5 > 3) #True
print(5 < 3) #False
print(5 == 3) #False
print(5 != 3) #True
print(3 >= 3) #True
print(4 <= 3) #False
print("Aa" > "aa") #False
print("Aa" < "aa") #True
print("aa" == "aa") #True
print("aa" != "aa") #False
print("car" > "cat") #False

#logical operators
print(4 == 4 and 3 == 3) #True
print(4 > 3 and 3 == 5) #False
print(4 == 4 or 3 == 3) #True
print(4 > 3 or 3 == 5) #True
print(not (5 > 3)) #False
print(not False) #True

#assignment operators
a = 5
print(a) #5
a += 3
print(a) #8
a -= 4
print(a) #4
a /= 2
print(a) #2.0
a *= 7
print(a) #14.0
a %= 3
print(a) #2.0
a //= 2
print(a) #1.0
a **= 4
print(a) #1.0

#address in ram comparison
c = 1000
d = 1000
print(c is d) #True
#when we use id() command the address of variable changable.
print(id(c)) #2770160692240
print(id(d)) #2770160692240
c += 1
print(id(c)) #2732462181168
print(c is d) #False

text = "Hello World"
print('m' in text) #False
print('H' in text) #True
print('He' in text) #True