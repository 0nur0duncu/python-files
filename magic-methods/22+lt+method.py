class MyNumber:
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, other):
        return self.value < other.value

a = MyNumber(10)
b = MyNumber(20)
print(a < b)  # Output: True

"""
Küçüktür karşılaştırması için çağrılır.
"""