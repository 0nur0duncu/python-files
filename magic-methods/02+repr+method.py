class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f'MyClass(value={self.value})'

obj = MyClass(10)
print(repr(obj))  # Output: MyClass(value=10)


"""
Nesnenin resmi (developers) temsilini döner.
"""