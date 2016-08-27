import sys

sys.stdout.write('\nTEST 3: Python\n')
sys.stdout.write('..[3] stdout 1\n')
sys.stdout.write('..[3] stdout 2\n')
sys.stderr.write('\x1B[1;31m')
sys.stderr.write('..[3] stderr a\n')
sys.stderr.write('..[3] stderr b\n')
sys.stderr.write('\x1B[0m')
exit(1)
