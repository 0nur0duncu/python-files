class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, value):
        self.value = value

obj = MyClass(10)  # Output: "Creating instance"

"""
Yeni bir nesne örneği oluşturulduğunda çağrılır. __init__ metodundan önce çağrılır.
"""