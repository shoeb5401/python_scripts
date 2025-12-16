import shutil as disk 
total_disk = round(disk.disk_usage(path="/")[0]/ 1024 ** 3,2)
used_disk = round(disk.disk_usage(path="/")[1]/ 1024 ** 3,2)
free_disk = round(disk.disk_usage(path="/")[2]/ 1024 ** 3,2)

disk_mark = 50
print("Printing Your Disk Info:\n" 
"#########################################################################"
)

print(f"Total Disk Space(GB): {total_disk}")
print(f"Total Used Space(GB): {used_disk}")
print(f"Total Free Space(GB): {free_disk}")

if (used_disk  * 100 / total_disk) > disk_mark:
    print("Your Disk Usage Exceed your disk mark(50%).")
print(
"#########################################################################"
)
