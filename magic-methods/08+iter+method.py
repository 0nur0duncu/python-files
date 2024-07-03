class MyList:
    def __init__(self, items):
        self.items = items
    
    def __iter__(self):
        return iter(self.items)

my_list = MyList([10, 20, 30])
for item in my_list:
    print(item)
# Output:
# 10
# 20
# 30

"""
Nesnenin iteratörünü döner.
"""