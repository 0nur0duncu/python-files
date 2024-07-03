class MyList:
    def __init__(self, items):
        self.items = items
    
    def __delitem__(self, index):
        del self.items[index]

my_list = MyList([10, 20, 30])
del my_list[1]
print(my_list.items)  # Output: [10, 30]

"""
Nesnenin elemanlarını indeksleme ile siler.
"""