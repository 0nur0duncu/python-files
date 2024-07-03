class MyNumber:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return MyNumber(self.value + other.value)

a = MyNumber(10)
b = MyNumber(20)
c = a + b
print(c.value)  # Output: 30

"""
+ operatörü ile toplama işlemi için çağrılır.
"""