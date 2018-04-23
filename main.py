#!/usr/bin/local/python3
import graph
import sorting
import random
import matplotlib.pyplot as plt

print('Sorting Visualization')
print('Choose Algorithm:\n1. Bubble\n2. B\n3. C')
functdict =  {
    '1': sorting.bubble,
}

choice = input('Enter selection: ')

#set interactive
plt.ion()

#initial graph 
nums = random.sample(range(1,100), 10)
graph.graphData(plt, nums)
plt.show()

#call sorting function
functdict[choice](nums, graph, plt)

#show final graph
#TODO: Change color after plotting
'''
ax = plt.gca()
for bar in ax.get_children():
    if(type(bar) == plt.patches.Rectangle):
        print('here')
        bar.set_color(5)
'''
plt.show()
plt.pause(5)