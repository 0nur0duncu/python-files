#Standart python libraries(DateTime)
#date,time,datetime
#------------------------------------

from datetime import datetime as dt
import locale as lc

now = dt.now() #or today()
print(now) #2022-12-06 11:41:22.248933

print(now.year) #2022
print(now.month) #12
print(now.day) #6
print(now.hour) #11
print(now.minute) #41
print(now.second) #22

today = dt.ctime(now)
print(today) #Tue Dec  6 11:44:34 2022 #readable english format
print(dt.strftime(now,'%a')) #Tue
print(dt.strftime(now,'%A')) #Tuesday
print(dt.strftime(now,'%b')) #Dec
print(dt.strftime(now,'%B')) #December
print(dt.strftime(now,'%c')) #Tue Dec  6 11:48:28 2022
print(dt.strftime(now,'%d')) #06
print(dt.strftime(now,'%j')) #340
print(dt.strftime(now,'%m')) #12
print(dt.strftime(now,'%U')) #49
print(dt.strftime(now,'%y')) #22
print(dt.strftime(now,'%Y')) #2022
print(dt.strftime(now,'%x')) #12/06/22
print(dt.strftime(now,'%X')) #11:48:28

print(lc.setlocale(lc.LC_ALL,'Turkish_Turkey.1254')) #Turkish_Turkey.1254
print(lc.setlocale(lc.LC_ALL,'Turkish')) #Turkish_Turkey.1254

time = dt.timestamp(now)
print(time) #1670317284.283695
print(type(time)) #<class 'float'>

actualTime = dt.fromtimestamp(time)
print(actualTime) #2022-12-06 12:03:09.330164

print(now-actualTime) #0:00:00 #difference between time