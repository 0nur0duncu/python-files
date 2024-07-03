# Walrus operatörü olmadan
line = input("Enter some text: ")
while line != "quit":
    print(f"You entered: {line}")
    line = input("Enter some text: ")

# Walrus operatörü ile
while (line := input("Enter some text: ")) != "quit":
    print(f"You entered: {line}")
