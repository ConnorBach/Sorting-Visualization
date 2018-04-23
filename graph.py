#!/usr/bin/local/python3
import random

# input: list of numbers
# output: matplotlib plot of the numbers 
def graphData(plt, data):
    x_rng = [x for x in range(1,11)]
    plt.bar(x_rng, data, align='center', alpha=0.5)
    plt.draw()

def updateGraph(plt, data):
    #print('updating graph')
    plt.clf()
    x_rng = [x for x in range(1,11)]
    plt.bar(x_rng, data, align='center', alpha=0.5)
    plt.draw()