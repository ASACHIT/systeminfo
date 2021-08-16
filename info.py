import platform
from datetime import datetime

import GPUtil
import psutil

gpus = GPUtil.getGPUs()
uname = platform.uname()
cpufreq = psutil.cpu_freq()
mem = psutil.virtual_memory()
gpus = GPUtil.getGPUs()

sys = uname.system
proccessor = uname.processor
machine = uname.machine
core = psutil.cpu_count(logical=True)
cpu_freq_mx = cpufreq.max
mem_total = (int(mem.total))/(1024 * 1024 * 1024)

gpu_list = []
for gpu in gpus:
    gpu_name = gpu.name
    gpu_total_memory = f"{gpu.memoryTotal}MB"
    gpu_temperature = f"{gpu.temperature} °C"
    gpu_list.append((gpu_name, gpu_total_memory))
    
g_pu = (gpu_list[0])[0]
g_pu_mem = (gpu_list[0])[1]

print(f'''
{"="*20} SYSTEM Info {"="*20}

        System       - {sys}
        Processor    - {proccessor}
        Total Cores  - {core} Cores
        Max Cpu Freq - {cpu_freq_mx}MHZ
        Total Ram    - {round(mem_total)}GB
        Gpu          - {g_pu}
        Gpu Memory   - {g_pu_mem}
                                
''')
