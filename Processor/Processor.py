import random
import threading
import queue
import time

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

class CPU:
    def __init__(self):
        self.current_process = None

    def execute(self, process):
        print(f"Executing Process {process.pid} with Burst Time {process.burst_time}")
        time.sleep(process.burst_time)  # Simulating CPU execution time
        print(f"Process {process.pid} executed.")

class ProcessScheduler(threading.Thread):
    def __init__(self, queue, quantum_time, percentage):
        threading.Thread.__init__(self)
        self.queue = queue
        self.quantum_time = quantum_time
        self.percentage = percentage

    def run(self):
        while not self.queue.empty():
            process = self.queue.get()
            cpu.execute(process)
            process.turnaround_time = time.time() - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            print(f"Process {process.pid} Turnaround Time: {process.turnaround_time:.2f}")
            print(f"Process {process.pid} Waiting Time: {process.waiting_time:.2f}")

def generate_processes(num_processes):
    processes = []
    for pid in range(num_processes):
        burst_time = random.randint(1, 20)  # Replace 20 with your desired maximum burst time
        processes.append(Process(pid, burst_time))
    return processes

def distribute_processes_to_queues(processes):
    rr1_queue = queue.Queue()
    rr2_queue = queue.Queue()
    fcfs_queue = queue.Queue()

    for process in processes:
        rand = random.uniform(0, 1)
        if rand < 0.6:
            rr1_queue.put(process)
        elif rand < 0.9:
            rr2_queue.put(process)
        else:
            fcfs_queue.put(process)

    return rr1_queue, rr2_queue, fcfs_queue

if __name__ == "__main__":
    cpu = CPU()
    num_processes_per_queue = 1000

    processes = generate_processes(num_processes_per_queue * 3)
    rr1_queue, rr2_queue, fcfs_queue = distribute_processes_to_queues(processes)

    rr1_scheduler = ProcessScheduler(rr1_queue, quantum_time=8, percentage=0.6)
    rr2_scheduler = ProcessScheduler(rr2_queue, quantum_time=16, percentage=0.3)
    fcfs_scheduler = ProcessScheduler(fcfs_queue, quantum_time=float('inf'), percentage=0.1)

    rr1_scheduler.start()
    rr2_scheduler.start()
    fcfs_scheduler.start()

    rr1_scheduler.join()
    rr2_scheduler.join()
    fcfs_scheduler.join()

    # Calculate average waiting time and turnaround time for each queue
    # ...

    print("Simulation completed.")
