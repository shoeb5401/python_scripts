import subprocess
service = str(input("Input the Service name you want the status of: "))

result = subprocess.run(
    ["systemctl", "is-active", service],
    capture_output=True,
    text=True
)
status = result.stdout.strip()
print(f"Your {service} is {status.capitalize()}")

