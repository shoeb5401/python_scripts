import platform, psutil

class system_info:

    def info(self) -> None:

        print("Printing System Info:\n" 
        "#########################################################################"
        )
        memory = psutil.virtual_memory()
        GB = 1024 **3
        hostname = platform.node()
        os_name = platform.system()
        os_arch = platform.machine()
        os_version = platform.release()
        cpu_count = psutil.cpu_count(logical= True)
        total_mem = round(memory.total / GB, 2)
        avail_mem = round(memory.available / GB, 2)
        used_mem = total_mem - avail_mem
        mem_mark = round(memory.available / GB, 2) < 3.00
        print(f"Hostname: {hostname}")
        print(f"OS name: {os_name}")
        print(f"OS architecture: {os_arch}")
        print(f"OS version: {os_version}")
        print(f"CPU count: {cpu_count} Cores")
        print(f"Total Memory: {total_mem} GB")
        print(f"Used Memory: {used_mem} GB")
        print(f"Available Memory: {avail_mem} GB")
        if  mem_mark :
            print("Memory is exceeding the 50% usage mark, Check what causes this Spike")

        print( 
        "#########################################################################"
        )

def main() -> None:
    system1 = system_info()
    system1.info()

if __name__ == '__main__':
    main()

