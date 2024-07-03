class DescriptorExample:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return f"Descriptor value for {self.name}"
    
    def __set__(self, instance, value):
        print(f"Setting {self.name} to {value}")

class MyClass:
    descriptor = DescriptorExample("my_descriptor")

obj = MyClass()
obj.descriptor = 42  # Output: "Setting my_descriptor to 42"

"""
Descriptor'a değer atandığında çağrılır.
"""