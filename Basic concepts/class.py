#OOP -class
#-----------------------------

class people: #class people():
    name = ""
    surname = ""
    age = 0
    weight = 0


people1 = people()
print(people1.name + people1.surname,sep="-") #empty
people1.name = "onur"
people1.surname = "oduncu"
print(people1.name +" "+ people1.surname,sep="-") #onur oduncu
print(people1.age) #0
print(people1.weight) #0
print(people1) #<__main__.people object at 0x000001E72A2B7810>

people2 = people()
people2.name = "albert"
people2.surname = "einstein"
print(people2.name +" "+ people2.surname,sep="-") #albert einstein
print(people2) #<__main__.people object at 0x00000252DE6AFA50>

class birds():
    b_name = ""
    b_age = 0
    def tell(self):
        print("cik cik")
    def ageUp(self):
        self.b_age += 1
        print("my age is "+ str(self.b_age))
    def __init__(self): #yes it is working
        print("yes it is working")

canary = birds()
canary.tell() #cik cik
canary.b_age = 5
canary.ageUp() #my age is 6
canary.ageUp() #my age is 7

canary.b_name = "Lyla"
print(canary.b_name) #Lyla

class computer():
    brand = "lenovo"
    age = 1
    def __init__(self,brand,age):
        self.age = age
        self.brand = brand

myComputer = computer("Casper",3)
print(myComputer.age) #3
print(myComputer.brand) #Casper

class staff:
    name = ""
    surname = ""
    salary = 0
    department = ""
    def __init__(self, name, surname, salary, department):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.department = department
    
    def infos():
        print("new staff is created...")

class manager(staff):
    code =1234
    def __init__(self, name, surname, salary, department,code):
        super().__init__(name, surname, salary, department)
        self.code = code
    #overriding
    def infos():
        print("new manager is created...")
class servant(staff):
    pass
class technical(staff):
    pass
newStaff = manager("onur","oduncu",0,"BT",1423)
print(newStaff.department) #BT
print(newStaff.name) #onur
print(newStaff.surname) #oduncu
print(newStaff.salary) #0
print(newStaff.code) #1423
#before overriding
print(manager.infos()) #new staff is created...
#after overriding
print(manager.infos()) #new manager is created...

#multiple inheritance
class staff:
    def __init__(self,salary,age):
        self.salary = salary
        self.__age = age
        print(self.salary)
class manager:
    def __init__(self):
        self.salary = "3000"
        print(self.salary)

class generealManager(staff,manager):
    pass

newStaff = staff(100,10)
#print(newStaff.age) ##AttributeError: 'staff' object has no attribute 'age'

class employee:
    def __init__(self,salary,age):
        self.__salary = salary
        self.age = age
    def getSalary(self): #Pascal Case
        return self.__salary
    def setSalary(self,newValue):
        self.__salary = newValue

newStaff = employee(11000,20)
newStaff.setSalary(30000)
print(newStaff.getSalary()) #30000

#del command
del newStaff
print(newStaff.getSalary()) #NameError: name 'newStaff' is not defined