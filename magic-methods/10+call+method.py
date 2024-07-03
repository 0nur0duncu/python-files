class MyCallable:
    def __init__(self, value):
        self.value = value
    
    def __call__(self, increment):
        self.value += increment
        return self.value

callable_obj = MyCallable(10)
print(callable_obj(5))  # Output: 15
print(callable_obj(10)) # Output: 25

"""
Nesnenin fonksiyon gibi çağrılmasını sağlar.
"""