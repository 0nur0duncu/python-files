# Good usage
chars = ['o', 'n', 'u', 'r']
name = ''.join(chars)
print(name) # Safe

# Bad usage
name = ''
for char in chars:
  name += char
print(name) 