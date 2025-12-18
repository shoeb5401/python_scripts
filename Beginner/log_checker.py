path = str(input("Input the path of the log file you want to read: "))
if not path:
    print("Path cannot be empty")
    exit(1)
word = str(input("Input the word you want to find in the log file: "))
if not word:
    print("Word cannot be empty")
    exit(1)
count = 0
with open(path, 'r') as file:
    for line in file:
        if word.lower() in line.lower():
            count += 1
            print(line)
            print(f"Your Word count: {count}")
        
