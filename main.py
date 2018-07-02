#!/usr/local/bin/python3
from graph import Grapher
import sorting
import random
import time
import sys
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
#import pyqtgraph.examples
#pyqtgraph.examples.run()

def usage(status):
	print('SORTING VISUALIZATION')
	print()

	print('''OPTIONS:
	-a [algorithm]      Sorting algorithms available:
				0. Default
				1. Insertion
				2. Quick
				3. Merge Recursive
				4. Selection
				5. Bubble
				6. Shell (NOT COMPLETE)
				7. Default (NOT COMPLETE)
				8. Merge In Place (NOT COMPLETE)
				9. Heap Sort (NOT COMPLETE)

	-n [size]           Size of data provided
	-g                  Enables graphing component
	-h                  Displays usage
	''')

	if not status == 0:
		print('ERROR: There was a problem with the given input...')
	sys.exit(status)

def parse_arguments():
	algorithm = 0
	size = 500
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
	except Exception:
		usage(1)

	return algorithm, size, enableGraph

def is_sorted(data, start=0, end=None):
	if end is None:
		end = len(data)

	c = data.copy()
	c[start:end] = sorted(c[start:end])
	return c == data

if __name__ == "__main__":

	algoDict = [sorting.quicksort, sorting.insertion_sort, sorting.quicksort, \
				sorting.merge_sort, sorting.selection_sort, sorting.bubble_sort]
	algorithm, size, enableGraph = parse_arguments()
	data = random.sample(range(1,size+1), size)
	#data = [random.lognormvariate(0,1) for i in range(size)]
	#data = [random.paretovariate(1) for i in range(size)]
	#data = [random.vonmisesvariate(0.75,2) for i in range(size)]

	g = Grapher(data, enableGraph)

	if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
		startTime = time.time()
		algoDict[algorithm](g,data,size//4,size//2)
		endTime = time.time()

		if not is_sorted(data,size//4,size//2):
			print('ERROR: Failure with Sorting Algorithm...')
			sys.exit(1)
		else:
			print('RUNTIME: '+'{:.2f}'.format(endTime-startTime)+' sec')



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
