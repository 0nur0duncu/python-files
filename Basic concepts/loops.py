#while loops
#---------------------

#infinite loop
#while True:
#    print("Hello World")

counter = 0
while counter < 10:
    counter +=1
    print(counter,end=" ")   
#1 2 3 4 5 6 7 8 9 10 
print()
#break and continue
while True:
    hold = int(input("I kept a number in my mind.Guess?:"))
    if hold == 5:
        print("good job.")
        break
    else:
        continue

number = 0
while True:
    number += 1
    print(number,end=" ")
    if number == 3:
        break
print()
#1 2 3

numbers = [1, 2, 3, 4, 5]
counter = 0
while counter <len(numbers):
    print(numbers[counter],end=" ")
    counter +=1
print()
#1 2 3 4 5

#For loop
#iterator
for i in "Python":
    print(i,end=" ")
print()
#P y t h o n

fruits = ["apple","Banana","tomato","orange"]
for j in fruits:
    print(j,end=" ")
print()
#apple Banana tomato orange

#for k in 1234:
#    print(k)
#TypeError: 'int' object is not iterable

#range function
for i in range(0 , 5):
    print(i,end=" ")
print()
#0 1 2 3 4
#last number is not include.

for i in range(2 , 20, 2):
    print(i,end=" ")
print()
#2 4 6 8 10 12 14 16 18

for i in enumerate("python"):
    print(i, end=" ")
print()
#(0, 'p') (1, 'y') (2, 't') (3, 'h') (4, 'o') (5, 'n')
for i in enumerate("python",3):
    print(i, end=" ")
print()
#(3, 'p') (4, 'y') (5, 't') (6, 'h') (7, 'o') (8, 'n')

#sorted function
print(sorted(numbers, reverse=True)) #[5, 4, 3, 2, 1]
print(numbers) #[1, 2, 3, 4, 5]
# sorted function is not permanent

#sum function
print(sum(numbers)) #15
print(sum(range(2,102,2))) #2550