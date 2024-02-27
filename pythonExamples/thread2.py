import threading

def task1():
    print("Starting task 1")
    # do some work here...
    print("Task 1 finished")
    return True

def task2():
    print("Starting task 2")
    # do some work here...
    print("Task 2 finished")

# create two threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# start both threads
thread1.start()

thread2.start()

# wait for both threads to finish
thread1.join()
thread2.join()

print("Both tasks are finished")
