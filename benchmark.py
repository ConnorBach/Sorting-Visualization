# benchmarking utility for sorting-visualzation
import sys
import main
import subprocess
from subprocess import PIPE

algs = ['1', '2', '3', '4', '5', '6']
sizes = [10, 20, 50, 100]
times = []
swaps = []

for i, a in enumerate(algs):
    curTime = []
    curSwap = []
    for j, size in enumerate(sizes):
        # run program
        process = subprocess.Popen(['python3', 'main.py', '-a', str(a), '-n', str(size)], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

        # parse output
        outputStr = stdout.decode('utf-8')
        lines = outputStr.split('\n')
        for k, line in enumerate(lines):
            data = line.split(':  ')
            #print(data)
            if(k == 1):
                curTime.append(data[1])
            if(k == 0):
                curSwap.append(data[1])
    times.append(curTime)
    swaps.append(curSwap)

# print tables
print('\n********************** Times ***********************')
for i in range(len(algs)):
    print(i+1, end=' ')
    for j in range(len(sizes)):
        print(times[i][j], '\t', end=' ')
    print('')

print('********************** Swaps ***********************')
for i in range(len(algs)):
    print(i+1, end=' ')
    for j in range(len(sizes)):
        print(swaps[i][j], '\t',end=' ')
    print('')