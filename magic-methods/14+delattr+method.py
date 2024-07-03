class MyClass:
    def __delattr__(self, name):
        super().__delattr__(name)
        print(f'Deleted {name}')

obj = MyClass()
obj.some_attribute = 10
del obj.some_attribute  # Output: Deleted some_attribute

"""
Bir öznitelik silindiğinde çağrılır.
"""