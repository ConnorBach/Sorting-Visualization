#!/usr/bin/local/python3
import graph
import sorting
import random
import time
import matplotlib
import matplotlib.pyplot as plt

print('Sorting Visualization')
print('''Choose Algorithm:
        1. Bubble
        2. Quick
        3. Insertion
        4. Selection
        5. Shell
        6. Default 
        ''')
functdict =  {
    '1': sorting.bubble,
    '2': sorting.quick,
    '3': sorting.insertion,
    '4': sorting.selection,
    '5': sorting.shell,
    '6': sorting.default_sort
}

choice = input('Enter selection: ')
sz = int(input('Enter size of data: '))
#set interactive
plt.ion()

#initial graph 
nums = random.sample(range(1,sz+1), sz)
graph.graphData(plt, nums, sz)
plt.show()

#call sorting function
start = time.time()
swaps = functdict[choice](nums, sz, graph, plt)
end = time.time()

#Change color after plotting
ax = plt.gca()
children = ax.get_children()
bars = list(filter(lambda x : isinstance(x, matplotlib.patches.Rectangle), children))
for bar in bars[0:len(bars)-1]:
    bar.set_color('g')

#show final graph
print('**************************\n')
print('Swaps: ', swaps)
print('Time: ', end-start)
plt.show()
plt.pause(3)