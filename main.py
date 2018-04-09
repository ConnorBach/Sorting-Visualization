#!/usr/bin/local/python3
import graph
import random
import matplotlib.pyplot as plt

print('Sorting Visualization')
print('Choose Algorithm:\n1. A\n2. B\n3. C')

choice = input('Enter selection: ')

#set interactive
plt.ion()

#initial graph 
nums = random.sample(range(1,100), 10)
graph.graphData(plt, nums)
plt.show()

for x in range(1,10):
    nums = random.sample(range(1,100), 10)
    graph.updateGraph(plt, nums)
    plt.pause(0.001)

plt.show()
