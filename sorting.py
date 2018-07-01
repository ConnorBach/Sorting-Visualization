import pyqtgraph as pg
import sys

def insertion_sort(g,nums, start=0, end=None):
	# Default Parameter Correction
	if end is None:
		end = len(nums)
	# Sort
	for i in range(start+1,end):
		x = nums[i]
		j = i-1
		while j >= start and nums[j] > x:
			nums[j+1]=nums[j]
			j-=1
			g.update(nums)
		nums[j+1] = x

		g.update(nums)

	g.exit()

def swap(g, nums, index1, index2):
	nums[index1], nums[index2] = nums[index2], nums[index1]
	g.update(nums)

def quicksort(g, nums, start=0, end=None):
	# Default Parameter Correction
	if end is None:
		end = len(nums)
	# Smaller Sorts --> insertion_sort
	# Larger Sorts --> quicksort
	# Without using insertion, would need an if making sure length > 1
	if end-start <= 10:
		insertion_sort(g, nums, start, end)
	else:
		p = partition(g, nums, start, end)
		quicksort(g, nums, start, p)
		quicksort(g, nums, p+1, end)

	g.exit()

def partition(g, nums, start, end):
	# Initialization
	current = start
	# Sorting by pivot
	for i in range(start, end):
		if nums[i] < nums[end-1]:
			swap(g, nums, current, i)
			current+=1
	# Move pivot between sorted sections
	swap(g, nums, current, end-1)
	return current
