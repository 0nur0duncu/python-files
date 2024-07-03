# Walrus operatörü olmadan
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    n = numbers[i]
    print(n)
    i += 1

# Walrus operatörü ile
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers) and (n := numbers[i]) < 6:
    print(n)
    i += 1

