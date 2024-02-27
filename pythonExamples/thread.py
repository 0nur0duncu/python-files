import threading

def worker():
    print("Worker thread started")
    # do some work here...
    print("Worker thread finished")

# create multiple worker threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)

# start all threads
for t in threads:
    t.start()

# wait for all threads to finish
for t in threads:
    t.join()

print("All worker threads finished")
