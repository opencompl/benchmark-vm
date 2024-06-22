#!/usr/bin/env python3

import tempfile
import os
import datetime
from termcolor import colored



gitcache = "GIT_ALTERNATE_OBJECT_DIRECTORIES=~/.gitcache/llvm-project.git/objects"


def benchmark(directory):
    commands = [
        f"cd {directory.name}; {gitcache} git clone git@github.com:llvm/llvm-project.git",
        f"cd {directory.name}/llvm-project; mkdir build; cd build; cmake -G Ninja -DCMAKE_BUILD_TYPE=Release ../llvm",
        f"cd {directory.name}/llvm-project/build; ninja",
        f"cd {directory.name}; {gitcache} git clone git@github.com:llvm/llvm-project.git",
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

    for x in zip(commands, times):
        print("\033[1m" + colored(x[0], 'blue') + "\033[0m")
        print("\t"+ str(x[1]))

temp_dir = tempfile.TemporaryDirectory()

benchmark(temp_dir)
