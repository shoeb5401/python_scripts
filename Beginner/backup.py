from pathlib import Path

source = Path(str(input("Input the source Directory: ")))
destination = Path(str(input("Input the destination Directory: ")))

if source.exists() and source.is_dir():
    
        if destination.exists() and destination.is_dir():
            print(f"Copying {source} to {destination}")
            source.copy_into(target_dir=destination)
            print("Backup is Successful.")
        
        
        else: 
            print(f"""{destination} doesnot exist\n
              Creating the {destination} folder.""")
            destination.mkdir()
            print(f"Copying {source} to {destination}")

            source.copy_into(target_dir=destination)
            print("Backup is Successful.")
   
else:
    print(f"{source} doesnot exist or it is not a directory.")
