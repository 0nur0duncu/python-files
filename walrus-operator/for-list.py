# Walrus operatörü olmadan
values = [1, 2, 3, 4, 5, 6]
filtered_values = []
for value in values:
    doubled = value * 2
    if doubled > 5:
        filtered_values.append(doubled)

# Walrus operatörü ile
values = [1, 2, 3, 4, 5, 6]
filtered_values = [doubled for value in values if (doubled := value * 2) > 5]
