import subprocess
port = int(input("Input the Port Number: "))
if not port:
    print("Port cannot be empty")
    exit(1)
elif not isinstance(port,int):
    print("Port can only be an integer value")
    exit(1)

result = subprocess.run(["lsof","-i",f":{port}"],text=True,capture_output=True)
if result.returncode == 0:
    print(f"{port} Port is Open on Localhost")
else:
    print(f"{port} Port is Closed")