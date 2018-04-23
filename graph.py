#!/usr/bin/local/python3
import random

# input: list of numbers
# output: matplotlib plot of the numbers 
def graphData(plt, data, sz):
    x_rng = [x for x in range(1,sz+1)]
    plt.bar(x_rng, data, align='center', alpha=0.5)
    plt.draw()

def updateGraph(plt, data, sz):
    #print('updating graph')
    plt.clf()
    x_rng = [x for x in range(1,sz+1)]
    plt.bar(x_rng, data, align='center', alpha=0.5)
    plt.draw()