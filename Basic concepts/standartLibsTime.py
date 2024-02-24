#python standart libraries (time)
#-------------------------------------

import time

print(time.gmtime(0)) #time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
print(time.time()) #1670317779.9210508 #gmtime-now
print(time.localtime()) #time.struct_time(tm_year=2022, tm_mon=12, tm_mday=6, tm_hour=12, tm_min=10, tm_sec=17, tm_wday=1, tm_yday=340, tm_isdst=0)
print(time.asctime()) #Tue Dec  6 12:10:44 2022
print(time.strftime('%m')) #12
print(time.strftime('%x')) #12/06/22
history = '19 May 1919'
#datetime strptime() function same
print(time.strptime(history,'%d %B %Y')) #time.struct_time(tm_year=1919, tm_mon=5, tm_mday=19, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=139, tm_isdst=-1)
print('Hello',end=" ")
time.sleep(2)
print("World",end="")
time.sleep(2)
print('!')
print()