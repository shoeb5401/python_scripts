from pathlib import Path

path = Path(str(input("Input the path of the File: ")))

if not path.exists():
    print(f"Enter a Valid path: {path} doesnot exist")
    exit(1)
elif not path.is_file():
    print(f"Enter a Valid File: {path} is not a File")
    exit(1)
with open(path, 'r') as file:
    for line in file:
        Path(line.strip()).mkdir(parents=True, exist_ok=True)
# with open(path, 'r') as file:
#     for line in file:
#         Path(line.strip()).rmdir()