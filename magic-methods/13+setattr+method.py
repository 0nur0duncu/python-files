class MyClass:
    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        print(f'Set {name} to {value}')

obj = MyClass()
obj.some_attribute = 10  # Output: Set some_attribute to 10

"""
Bir öznitelik ayarlandığında çağrılır.
"""