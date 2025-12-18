from pathlib import Path
from datetime import date

dir_path = input("Enter the Path of the Directory: ")
if not dir_path:
    print("Path cannot be empty")
    exit(1)
p = Path(dir_path)

if p.exists() and p.is_dir():
    print("\nPrinting all files and folders in the directory:")
    for file in p.iterdir():
        print(file)

    print("\nPrinting files older than 7 days:")
    for file in p.iterdir():
        file_date = date.fromtimestamp(file.stat().st_mtime)
        if (date.today() - file_date).days > 7:
            print(file)
            

else:
    print("Enter a valid directory path.")
