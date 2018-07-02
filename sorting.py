def insertion_sort(g, nums, start=0, end=None):
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

def merge(g, nums, start, middle, end):
	# Initialization
	copy = []
	i1 = start
	i2 = middle
	# Merging 2 sorted lists
	while i1 < middle and i2 < end:
		if nums[i1] <= nums[i2]:
			copy.append(nums[i1])
			i1+=1
		else:
			copy.append(nums[i2])
			i2+=1
	# Leftover appending
	for i in range(i1, middle):
		copy.append(nums[i])
	for i in range(i2, end):
		copy.append(nums[i])
	# Move from copy to nums
	for i in range(start,end):
		nums[i]=copy[i-start]
		g.update(nums)


def merge_sort(g, nums, start=0, end=None):
	# Default Parameter Correction
	if end is None:
		end = len(nums)
	# Smaller Sorts --> insertion_sort
	# Larger Sorts --> merge_sort
	# Without using insertion, could go all the way to base
	if end-start <= 10:
		insertion_sort(g, nums, start, end)
	else:
		merge_sort(g, nums, start, (start+end)//2)
		merge_sort(g, nums, (start+end)//2, end)
		merge(g, nums, start, (start+end)//2, end)
