a, b = 5, 6

print(a,b)

# Good usage
a, b = b, a

print(a,b)

# Bad usage
a, b = 5, 6

temp = a
a = b
b = temp

print(a, b)