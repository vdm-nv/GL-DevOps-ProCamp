import psutil
import sys


metric_to_print = sys.argv[1]


if metric_to_print == "cpu":
    cpu = psutil.cpu_times(percpu=False)
    print('#'*20+'CPU'+'#'*20)
    print(f'system.cpu.idle {cpu.idle}')
    print(f'system.cpu.user {cpu.user}')
    print(f'system.cpu.guest {cpu.guest}')
    print(f'system.cpu.iowait {cpu.iowait}')
    print(f'system.cpu.stolen {cpu.steal}')
    print(f'system.cpu.system {cpu.system}')
    print('#' * 43)
elif metric_to_print == "mem":
    mem = psutil.virtual_memory()
    swapm = psutil.swap_memory()
    print('#' * 20 + 'MEMORY' + '#' * 20)
    print(f'virtual total {mem.total}')
    print(f'virtual used {mem.used}')
    print(f'virtual free {mem.free}')
    print(f'virtual shared {mem.shared}')
    print(f'swap total {swapm.total}')
    print(f'swap used {swapm.used}')
    print(f'swap free {swapm.free}')
    print('#' * 46)
else:
    print('\nWrong argument!\nPlease use (cpu | mem)\n')
