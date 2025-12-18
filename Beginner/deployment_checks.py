import shutil as disk
import subprocess
from pathlib import Path
disk_space = float(input("Input the Required Disk Space in GB: "))
folders = [ x.strip() for x in input("Input the Folders name: ").split()]
ports = list(map(int, input("Input the Ports numbers: ").split()))

avail_space = round(disk.disk_usage('/').free / 1024 **3,2)
print( "Disk Space: PASS" if avail_space >= disk_space else "Disk Space: FAIL")


port_pass = True
for port in ports:
    result = subprocess.run(['lsof','-i',f":{port}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    if result == 0:
        port_pass = False
        break

print("Port: PASS" if port_pass == True else "Port: FAIL")

folder_pass = True
for folder in folders:
    path = Path(folder)
    if not path.is_dir():
        folder_pass = False
        break
print("Folder: PASS" if folder_pass == True else "Folder: FAIL")
