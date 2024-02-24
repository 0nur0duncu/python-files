#properties of data types
#---------------------------

numbers= [1, 2, 3, 4, 5, 6, 7]
print(numbers[0]) #1
print(numbers[1]) #2
print(numbers[-1]) #7
print(numbers[-2]) #6
print(numbers[:3]) #[1, 2, 3]
print(numbers[2:4]) #[3, 4]
print(numbers[4:]) #[5, 6, 7]
print(numbers[4:-2]) #[5]
print(numbers[:]) #[1, 2, 3, 4, 5, 6, 7]
print(numbers[::2]) #[1, 3, 5, 7]
print(numbers[::-2]) #[7, 5, 3, 1]
print(numbers[::-1]) #[7, 6, 5, 4, 3, 2, 1]
numbers[2:4] = [8,6]
print(numbers) #[1, 2, 8, 6, 5, 6, 7]
del numbers[1:3]
print(numbers) #[1, 6, 5, 6, 7]