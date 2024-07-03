class MyCollection:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)

collection = MyCollection([1, 2, 3])
print(len(collection))  # Output: 3

"""
Nesnenin uzunluğunu döner.
"""