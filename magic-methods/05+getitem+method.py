class MyList:
    def __init__(self, items):
        self.items = items
    
    def __getitem__(self, index):
        return self.items[index]

my_list = MyList([10, 20, 30])
print(my_list[1])  # Output: 20

"""
Nesnenin elemanlarına indeksleme ile erişimi sağlar.
"""