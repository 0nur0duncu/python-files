#built-in functions
#-------------------------------

print(print) #<built-in function print>
s = "Hello World"
print(s + "!") #Hello World!

#Quotation Marks
print('hello') #hello
print("hello") #hello
print("""hello""") #hello
#print("Hello "my"world") #SyntaxError: invalid syntax.
print("""Hello 'my' world""") #Hello 'my' world
print("""Hello "my" world""") #Hello "my" world
print('Hello "my" world') #Hello "my" world
print('Hello """my""" world') #Hello """my""" world

#for writing the multiple line in print() function
print("""Hello
World
""") #Hello
     #World

print("P","y","t","h","o","n") #P y t h o n
print("P","y","t","h","o","n",sep="-") #P-y-t-h-o-n
print("P","y","t","h","o","n",sep="/") #P/y/t/h/o/n
#if you use end parameter next line will write side by side.
print("Python",end="!") #Python!
print()

#the length of strings, list and tuple
print(len("Python")) #6
print(len("")) #0
str = "Hello World"
print(len(str)) #11

print(len("a")) #1