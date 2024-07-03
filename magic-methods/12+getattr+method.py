class MyClass:
    def __getattr__(self, name):
        return f'{name} is not defined'

obj = MyClass()
print(obj.some_attribute)  # Output: some_attribute is not defined

"""
Bir öznitelik bulunamadığında çağrılır.
"""