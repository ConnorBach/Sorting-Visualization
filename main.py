#!/usr/local/bin/python3
import graph
import sorting
import random
import time
#import matplotlib
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
import sys
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import pyqtgraph.examples
pyqtgraph.examples.run()

def usage(status):
    print('Sorting Visualization')
    print()

    print('''OPTIONS:
    -a [algorithm]      Sorting algorithms available:
                            1. Bubble
                            2. Quick
                            3. Insertion
                            4. Selection
                            5. Shell
                            6. Default
                            7. Merge In Place
                            8. Merge Recursive

    -n [size]           Size of data provided
    -g                  Enables graphing component
    -h                  Displays usage
    ''')

    if not status == 0:
        print('ERROR: There was a problem with the given input...')
    sys.exit(status)

def parse_arguments():
    algorithm = 2
    size = 100
    enableGraph = False

    try:
        if '-h' in sys.argv:
            usage(0)
        if '-a' in sys.argv:
            algorithm = int(sys.argv[sys.argv.index('-a')+1])
        if '-n' in sys.argv:
            size = int(sys.argv[sys.argv.index('-n')+1])
        if '-g' in sys.argv:
            enableGraph = True
    except:
        usage(1)

    return algorithm, size, enableGraph

def is_sorted(data):
    c = data.copy()
    return c == data

if __name__ == "__main__":

    algoDict = [sorting.insertion_sort,sorting.quicksort]

    algorithm, size, enableGraph = parse_arguments()
    print(algorithm, size, enableGraph)

    data = random.sample(range(1,size+1), size)

    ### PG
    win = pg.GraphicsWindow()
    plt = win.addPlot()
    curve = plt.plot(data)

    gen = algoDict[algorithm](curve,data)
    def rando():
        try:
            next(gen)
        except StopIteration:
            return None
    ### END
    if enableGraph:

        start = time.time()
        #algoDict[algorithm](curve,data)
        end = time.time()

    if not is_sorted(data):
        print('ERROR: Failure with Sorting Algorithm...')
        sys.exit(1)
    else:
        print('SUCCESS')
        '''plt.clf()
        plt.bar(range(1,len(data)+1), data, align='center', alpha=1, color='green')
        plt.draw()
        plt.pause(5)'''

    timer = pg.QtCore.QTimer()
    timer.timeout.connect(rando)
    timer.start(50)

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()
'''
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
'''
