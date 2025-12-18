import subprocess
username = str(input("Input the Username: "))
if not username:
    print("Username cannot be empty")
    exit(1)
result = subprocess.run(["getent", "passwd",username],capture_output=True, text=True)
if result.returncode == 0:
    print(f"{username} is  present in the System")
else:
    print(f"{username} is not present in the System")