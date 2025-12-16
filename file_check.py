import os 


file_path = str(input("Input a file path, You want to Check:"))
exist = os.path.exists(file_path)
print(f"Your file path is: {file_path}\n")
if exist and file_path.startswith(('/','.','..')):
    print("Your file path exist")
elif file_path.startswith(('/','.','..')):
    print("Your Path doesnot exist\n")
    
    ans = str(input("Do you want to create a file in this path(Y or N):\n"))
    if ans == 'Y' or 'y':
        with open(file_path,'w') as f:
            
            pass
        print("File created sucessfully")
    else: print("Aborting....")
else : 
    print("Check Your File path")