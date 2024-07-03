class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f'MyClass with value {self.value}'

obj = MyClass(10)
print(obj)  # Output: MyClass with value 10

"""
Nesnenin string (users) temsilini döner.
"""