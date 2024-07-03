# Walrus operatörü olmadan
value = input("Enter a number: ")
if value.isnumeric():
    num = int(value)
    print(f"You entered the number: {num}")

# Walrus operatörü ile
if (value := input("Enter a number: ")).isnumeric():
    num = int(value)
    print(f"You entered the number: {num}")
