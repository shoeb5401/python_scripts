import os 

custom_env = str(input("Input the env variable you want to search: "))

envs = os.environ

for (env, val) in envs.items():
    if custom_env.lower() in env.lower():
        print(f"{env}: {val}")
    # print(f"{env}: {val}")
