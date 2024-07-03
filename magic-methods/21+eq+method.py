class MyNumber:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value

a = MyNumber(10)
b = MyNumber(10)
print(a == b)  # Output: True

"""
Eşitlik karşılaştırması için çağrılır.
"""