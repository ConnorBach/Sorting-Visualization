import sys
import main
import subprocess
from subprocess import PIPE

f = open('check.txt')

# correctness
print('Testing correctness...')
for line in f:
    if(line != 'Correct'):
        print('Failed')
    else:
        print('Correct')

# performance
print('Testing performance...')
process = subprocess.Popen(['python3', 'benchmark.py'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

# memory
print('Testing memory...')
for line in f:
    if(line == 'Failed'):
        print('Failed')
    else:
        print('Correct')