import os 

custom_env = str(input("Input the env variable you want to search: ")).upper()
if not custom_env:
    print("env cannot be empty")
    exit(1)

if os.getenv(custom_env) == None:
    print("Enter a Valid ENV variable")
else:
    print(f"{custom_env}: {os.getenv(custom_env)}")
# for (env, val) in envs.items():
#     if custom_env.lower() in env.lower():
#         print(f"{env}: {val}")
#     # print(f"{env}: {val}")
