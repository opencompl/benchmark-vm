#!/usr/bin/env python3

import tempfile
import os
import platform
import datetime
from termcolor import colored



gitcache = "GIT_ALTERNATE_OBJECT_DIRECTORIES=~/.gitcache/llvm-project.git/objects:~/.gitcache/mathlib4.git/objects"
gitcacheScratch = "GIT_ALTERNATE_OBJECT_DIRECTORIES=/local/scratch/compilers/llvm-project.git/objects"
gitcacheNFS = "GIT_ALTERNATE_OBJECT_DIRECTORIES=/auto/groups/compilers/llvm-project.git/objects"

def machineinfo():
    print(colored("Hostname",  attrs=["bold"]))
    os.system("hostname")
    print(colored("CPU",  attrs=["bold"]))
    os.system("lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('")
    os.system("cat /proc/cpuinfo| grep 'model name'| head -n 1")
    print(colored("Memory",  attrs=["bold"]))
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # e.g. 4015976448
    mem_gib = mem_bytes/(1024.**3)  # e.g. 3.74
    print(str(mem_gib) + "GB")
    print(colored("Working Directory",  attrs=["bold"]))
    os.system("pwd")


def benchmark(directory):
    commands = [
        f"cd {directory.name}; {gitcacheScratch} git clone git@github.com:llvm/llvm-project.git; git checkout llvmorg-18.1.8",
        f"cd {directory.name}/llvm-project; mkdir build; cd build; cmake -G Ninja -DCMAKE_BUILD_TYPE=Release ../llvm",
        f"cd {directory.name}/llvm-project/build; ninja",

        #f"cd {directory.name}; {gitcache} git clone git@github.com:leanprover-community/mathlib4.git",
        #f"cd {directory.name}/mathlib4; lake build",
        f"rm -rf {directory.name}",
    ]

    times = []
    for c in commands:
        print(c)
        start = datetime.datetime.now()
        os.system(c)
        end = datetime.datetime.now()
        delta = end-start
        times.append(delta)
        print(delta)
    return (commands, time)

def print_benchmark(commands, times)
    for x in zip(commands, times):
        print(colored(x[0], attrs=["bold"]))
        print("\t"+ str(x[1]))

temp_dir = tempfile.TemporaryDirectory(dir="/dev/shm")

commands, times = benchmark(temp_dir)
machineinfo()
print_benchmark(commands, times)
