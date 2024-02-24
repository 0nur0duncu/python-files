#Standart libraries (Random module)
#---------------------------------------
import random as rn

#random() func generate 0.0-0.1 number
print(rn.random()) #0.9458352877180172 #changable
print(rn.random()) #0.5802739902564997

print(rn.uniform(1,2)) #1.4709048329094765
print(rn.uniform(3,4)) #3.4799967178443962
print(rn.uniform(1.2,8.3)) #4.233466350338074

print(rn.randint(1,2)) #2
print(rn.randint(1,2)) #1

print(rn.randbytes(5)) #b'\xff\x05$\xec7'

numbers =[1, 2, 3, 4, 5]

print(rn.choice(numbers)) #1
print(rn.choice(numbers)) #5

rn.shuffle(numbers) #permanent changes
print(numbers) #[3, 1, 2, 5, 4]

chars = "Hello World"
#rn.shuffle(chars) #TypeError: 'str' object does not support item assignment

print(rn.randrange(5)) #1
print(rn.randrange(4,7)) #4  #second parameter is not include

print(rn.sample(numbers,2)) #[2, 3]
print(rn.sample(numbers,4)) #[4, 3, 5, 1]