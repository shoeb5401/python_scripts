import os, psutil
print("Printing Your System Info:\n" 
"#########################################################################"
)

hostname = os.uname()[1]
os_name = os.uname()[0]
os_arch = os.uname()[4]
os_version = os.uname()[2]
cpu_count = os.cpu_count()
total_mem = round(psutil.virtual_memory()[0] / 1024 **3, 2)
avail_mem = round(psutil.virtual_memory()[1] / 1024 **3, 2)
mem_mark = round(psutil.virtual_memory()[1] / 1024 **3, 2) < 3.00
print(f"Your Hostname: {hostname}")
print(f"Your OS name:{os_name}")
print(f"Your OS architecture: { os_arch}")
print(f"Your OS version: {os_version}")
print(f"Your CPU count: {cpu_count}")
print(f"Your Total Memory(GB): { total_mem}")
print(f"Your Available Memory(GB): { avail_mem}")
if  mem_mark :
    print("Your Memory is exceeding the 50% usage mark, Check what causes this Spike")

print( 
"#########################################################################"
)
