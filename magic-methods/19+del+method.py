class MyClass:
    def __del__(self):
        print("Instance is being deleted")

obj = MyClass()
del obj  # Output: "Instance is being deleted"

"""
Nesne yok edilmeden hemen önce çağrılır.
"""