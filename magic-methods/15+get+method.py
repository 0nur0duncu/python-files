class DescriptorExample:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return f"Descriptor value for {self.name}"

class MyClass:
    descriptor = DescriptorExample("my_descriptor")

obj = MyClass()
print(obj.descriptor)  # Output: "Descriptor value for my_descriptor"

"""
Descriptor protokolü için kullanılır. Bir sınıf özniteliği olarak tanımlanan descriptor'a erişildiğinde çağrılır.
"""