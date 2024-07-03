class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

my_range = MyRange(1, 4)
for num in my_range:
    print(num)
# Output:
# 1
# 2
# 3

"""
Nesnenin bir sonraki elemanını döner.
"""