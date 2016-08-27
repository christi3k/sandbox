import os
import sys
import subprocess

def one():
    return subprocess.call('./one.sh')

def two():
    return subprocess.call(['python','./two.py'])

def three():
    three = subprocess.Popen(['python', './three.py'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    #write both stdout and stderr to stdout
    for pipe in (three.stdout, three.stderr):
        for ln in pipe:
            sys.stdout.write(ln)
    return 0

functions = [one, two, three]
pids = []

for func in functions:
    pid = os.fork()
    if pid == 0:
        result = func()
        # without this .flush(), we won't see output from three() when run via ssh
        sys.stdout.flush()
        os._exit(result)
    pids.append(pid)
