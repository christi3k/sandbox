import sys

sys.stdout.write('\nTEST 2: Python\n')
sys.stdout.write('..[2] line 1\n')
sys.stdout.write('..[2] line 2\n')
sys.stderr.write('\x1B[1;31m')
sys.stderr.write('..[2] error a\n')
sys.stderr.write('..[2] error b\n')
sys.stderr.write('\x1B[0m')
exit(1)
