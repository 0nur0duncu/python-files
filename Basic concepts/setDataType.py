#Set Data Type (collections)
#unordered and unsigned so, random order
#only one argument
#-----------------------------------------

mySet = set()
print(type(mySet)) #<class 'set'>
#int variables not assign
#mySet = set(1) #TypeError: 'int' object is not iterable

mySet = set("State")
print(mySet) #{'a', 'e', 't', 'S'}
print(type(mySet)) #<class 'set'>

myList = ["bee", "duck", "bear"]
mySet = set(myList)
print(mySet) #{'duck', 'bear', 'bee'}

#mySet = set("C", "A", "R") #TypeError: set expected at most 1 argument, got 3

values = {"1", "2", "3", "4", "5"}
mySet = set(values)
print(mySet) #{'5', '1', '3', '2', '4'}

#same elements write unrepeatly
values = {"1", "2", "3", "4", "5", "1", "2", "3"}
mySet = set(values)
print(mySet) #{'4', '3', '2', '1', '5'}

values = "hello"
mySet = set(values)
mySet.add("!")
print(mySet) #{'o', 'h', 'e', 'l', '!'}
mySet.remove("o")
print(mySet) #{'!', 'l', 'h', 'e'}
print(len(mySet)) #4
mySet2 = mySet.copy()
mySet3 = mySet2
print(id(mySet)) #2543957380448
print(id(mySet2)) #2543957378656
print(id(mySet3)) #2543957378656
mySet2.add("D")
print(mySet2.difference(mySet)) #{'D'}
#or
print(mySet2 - mySet) #{'D'}

mySet.discard("h")
mySet.discard("K") #not error even advantage
print(mySet) #{'l', '!', 'e'}
mySet.remove("!") 
print(mySet)#{'e', 'l'}
#mySet.remove("K") #KeyError: 'K'
print(mySet.pop()) #l ->random deleted element
print(mySet) #{'e'}

mySet.clear()
print(mySet) #set()
print(mySet2.intersection(mySet3)) #{'h', 'D', 'e', 'l', '!'}
#or
print(mySet2 & mySet3) #{'h', 'D', 'e', 'l', '!'}
mySet4 = {1,3,7}
print(mySet2.union(mySet4)) #{1, 'l', 3, 'D', 'h', '!', 7, 'e'}
#or
print(mySet2 | mySet4) #{1, 'l', 3, 'D', 'h', '!', 7, 'e'}

text ="Python"
print(type(frozenset(text))) #<class 'frozenset'>
fSet = frozenset(text)
print(fSet) #frozenset({'P', 'n', 'y', 'h', 'o', 't'})

a = set([1,3,5])
b = set([4,5,6])
print(a.symmetric_difference(b)) #{1, 3, 4, 6}
a.intersection_update(b)
print(a) #{5}