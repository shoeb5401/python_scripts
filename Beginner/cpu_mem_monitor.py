import psutil, time

iteration  = int(input("Input the number of iterations you want: "))
for i in range(iteration):
    print(f"\nCPU Usage: {psutil.cpu_percent(interval=None)}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%\n")
    time.sleep(1)

