import threading as th

""" for i in dir(threading):
    if '__' not in i:
        print(i) """

import logging as log

""" for i in dir(log):
    if '__' not in i:
        print(i)
 """
def calc(state: any | int =10, *args) -> int:
    print(*args)


calc(10,20,30,40)
