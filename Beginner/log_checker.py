path = str(input("Input the path of the log file you want to read: "))
word = str(input("Input the word you want to find in the log file: "))
count = 0
with open(path, 'r') as file:
    for line in file:
        if word.lower() in line.lower():
            count += 1
            print(line)
            print(f"Your Word count: {count}")
        
