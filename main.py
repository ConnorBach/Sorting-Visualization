#!/usr/bin/local/python3
import graph
import sorting
import random
import time
import matplotlib
import matplotlib.pyplot as plt
import sys

CHOICE = '1'
SZ = 0
GRAPHICS = False 

def usage(status):
    print('Sorting Visualization')
    print('USAGE: main.py -a [ALGORITHM] -n [SIZE OF DATA]')
    print('''Algorithms:
            1. Bubble
            2. Quick
            3. Insertion
            4. Selection
            5. Shell
            6. Default 
            7. Merge In Place
            8. Merge Recursive
            ''')
    sys.exit(status)

functdict =  {
    '1': sorting.bubble,
    '2': sorting.quick,
    '3': sorting.insertion,
    '4': sorting.selection,
    '5': sorting.shell,
    '6': sorting.default_sort,
    '7': sorting.inMerge,
    '8': sorting.merge
}

# Parse command line arguments
i = 1
if len(sys.argv) == 2:
    if sys.argv[1] == '-h':
        usage(0)

while i < len(sys.argv) - 1:
    arg = sys.argv[i]
    if arg == '-h':
        usage(0)
    elif arg == '-a':
        i += 1
        CHOICE = sys.argv[i]
    elif arg == '-n':
        i += 1
        SZ = int(sys.argv[i])
    elif arg == '-g':
        i += 1
        GRAPHICS = sys.argv[i]
    else:
        usage(1)
    i += 1

choice = CHOICE
sz = SZ
#set interactive
if GRAPHICS:
    plt.ion()

#initial graph 
nums = random.sample(range(1,sz+1), sz)
if GRAPHICS:
    graph.graphData(plt, nums, sz)
    plt.show()

#call sorting function
start = time.time()
swaps = functdict[choice](nums, sz, graph, plt, GRAPHICS)
end = time.time()

#Change color after plotting
if GRAPHICS:
    ax = plt.gca()
    children = ax.get_children()
    bars = list(filter(lambda x : isinstance(x, matplotlib.patches.Rectangle), children))
    for bar in bars[0:len(bars)-1]:
        bar.set_color('g')

#show final graph
print('Swaps: ', swaps)
print('Time: ', "{0:.2f}".format((end-start)))

if GRAPHICS:
    plt.show()
    plt.pause(3)