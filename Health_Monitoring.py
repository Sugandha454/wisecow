import psutil
import os

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        print(f"High CPU usage detected: {cpu_percent}%")

def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > MEMORY_THRESHOLD:
        print(f"High memory usage detected: {memory_percent}%")

def check_disk_space():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        print(f"High disk usage detected: {disk_usage}%")

def check_running_processes():
    processes = psutil.process_iter()
    for process in processes:
        try:
            process_name = process.name()
            process_memory = process.memory_percent()
            if process_memory > MEMORY_THRESHOLD:
                print(f"High memory usage by process '{process_name}': {process_memory}%")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()
    check_running_processes()

if __name__ == "__main__":
    main()
