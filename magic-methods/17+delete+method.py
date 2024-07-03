class DescriptorExample:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return f"Descriptor value for {self.name}"
    
    def __set__(self, instance, value):
        print(f"Setting {self.name} to {value}")
    
    def __delete__(self, instance):
        print(f"Deleting {self.name}")

class MyClass:
    descriptor = DescriptorExample("my_descriptor")

obj = MyClass()
del obj.descriptor  # Output: "Deleting my_descriptor"


"""
Descriptor'dan değer silindiğinde çağrılır.
"""