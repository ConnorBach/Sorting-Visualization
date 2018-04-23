#!/usr/bin/local/python3
import graph
import sorting
import random
import time
import matplotlib
import matplotlib.pyplot as plt

print('Sorting Visualization')
print('Choose Algorithm:\n1. Bubble\n2. Quick\n3. C')
functdict =  {
    '1': sorting.bubble,
    '2': sorting.quick,
}

choice = input('Enter selection: ')
sz = int(input('Enter size of data: '))
#set interactive
plt.ion()

#initial graph 
nums = random.sample(range(1,100), sz)
graph.graphData(plt, nums, sz)
plt.show()

#call sorting function
start = time.time()
swaps = functdict[choice](nums, sz, graph, plt)
end = time.time()

#show final graph
#TODO: Change color after plotting
ax = plt.gca()
children = ax.get_children()
bars = list(filter(lambda x : isinstance(x, matplotlib.patches.Rectangle), children))
#print(bars)
for bar in bars[0:len(bars)-1]:
    print(bar)
    bar.set_color('g')

print('Swaps: ', swaps)
print('Time: ', end-start)
plt.show()
plt.pause(3)