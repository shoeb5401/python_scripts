from pathlib import Path

path = Path(str(input("Input the path of the File: ")))

if not path.exists():
    print(f"Enter a Valid path: {path} doesnot exist")
    exit(1)
elif not path.is_file():
    print(f"Enter a Valid File: {path} is not a File")
    exit(1)
line_count = 0
word_count = 0
char_count = 0
with open(path,'r') as file:
     for line in file:
        line_count += 1
        char_count += len(line)          
        word_count += len(line.split())  

print(f"Your file has: {line_count} Lines, {word_count} Words, {char_count} Characters")