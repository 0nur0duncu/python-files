#user interaction(input)
#------------------------------

input() #>>

print(input()) #>>hello hello
print(input("Please enter a number: ")) #>>10 10

a=input()
print(a) #>>10 10

#default string type
print(type(a)) #<class 'str'>

b = input("Please enter your name: ")
print("Hello" ,b) #Hello sir
#or
print("Hello " +b) #Hello sir

c = input("Please enter a number: ") #>>5
mult = c * 6
print(mult) #555555

d = input("Please enter a number: ") #>>10
d = int(d) #string to int casting
mult2 = d * 6
print(mult2) #60
#or
e = int(input("Please enter a number: "))
