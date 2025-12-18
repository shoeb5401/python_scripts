import subprocess
service = str(input("Input the Service name you want the status of: "))
if not service:
    print("Service cannot be empty")
    exit(1)
result = subprocess.run(
    ["systemctl", "is-active", service],
    capture_output=True,
    text=True
)
status = result.stdout.strip()
print(f"Your {service} is {status.capitalize()}")

