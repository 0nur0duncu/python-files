#tuple data type(collections) ()
#it cannot change in elements. Because it is immutable.
#--------------------------------------

myTuple = ()
print(type(myTuple)) #<class 'tuple'>

#built-in functions
myTuple2 = tuple()
print(type(myTuple2)) #<class 'tuple'>

#number of elements
numbers = (1, 2, 3, 4, 5)
print(len(numbers)) #5

myTuple3 = ("sample")
print(len(myTuple3)) #6
print(myTuple3) #sample
print(type(myTuple3)) #<class 'str'>
print(myTuple3[0]) #s
print(myTuple3[5]) #e
myTuple3 = ("sample",)
print(type(myTuple3)) #<class 'tuple'>

#single element or more is diffrent statues
myTuple4 = ("sample","state" )
print(len(myTuple4)) #2
print(myTuple4) #('sample', 'state')
print(type(myTuple4)) #<class 'tuple'>
print(myTuple4[0]) #sample
print(myTuple4[1]) #state
#print(myTuple4[3]) #IndexError: tuple index out of range
#myTuple4[0] = "new" #TypeError: 'tuple' object does not support item assignment

print(min(numbers)) #1
print(max(numbers)) #5

mixedState = (True , 'a', 12.4, 7, 5j)
print(mixedState) #(True, 'a', 12.4, 7, 5j)
print(type(mixedState[1])) #<class 'str'>

#clone the tuple like list it hold same address again
mixedState2 = mixedState
print(id(mixedState)) #2210371804416
print(id(mixedState2)) #2210371804416
mixedState2 = tuple(mixedState)
print(id(mixedState)) #1418384383232
print(id(mixedState2)) #1418384383232
#because it cannot changable the python already know it so it cannot allocate new adress

newtuple = (myTuple,myTuple2,myTuple3,myTuple4)
print(newtuple) #((), (), 'sample', ('sample', 'state'))

newtext = "Python"
newtuple2 = tuple(newtext)
print(newtuple2) #('P', 'y', 't', 'h', 'o', 'n')

#the functions of tuple data type
print(dir(tuple))