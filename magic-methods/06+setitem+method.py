class MyList:
    def __init__(self, items):
        self.items = items
    
    def __setitem__(self, index, value):
        self.items[index] = value

my_list = MyList([10, 20, 30])
my_list[1] = 25
print(my_list[1])  # Output: 25

"""
Nesnenin elemanlarını indeksleme ile ayarlar.
"""