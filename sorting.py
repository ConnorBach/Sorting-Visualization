#contains all sorting algorithms

'''
FUNCTION bubble
@param nums - list of numbers to sort
@param sz - size of list
@param graph - module for graphing
@param plt - matplotlib plt
@return number of swaps
'''
def bubble(nums, sz, graph, plt, GRAPHICS):
    swaps = 0
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if(nums[j] > nums[j+1]):
                #swap element
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
                swaps += 1
            #update graph
            if GRAPHICS:
                graph.updateGraph(plt, nums, sz)
                plt.pause(0.001)
    return swaps
#TODO: Add more sorting algorithms

'''
FUNCTION partion
Quick sort helper function
'''
def partition(nums, begin, end):
    pvt = begin
    swaps = 0
    for i in range(begin+1 , end+1):
        if(nums[i] <= nums[begin]):
            pvt += 1
            nums[i], nums[pvt] = nums[pvt], nums[i]
            swaps += 1
    nums[pvt], nums[begin] = nums[begin], nums[pvt]
    swaps += 1
    return [pvt, swaps]

'''
FUNCTION quick
quick sort function
@return number of swaps
'''
def quick(nums, sz, graph, plt, GRAPHICS):
    begin = 0
    end = (sz-1)
    swaps = 0

    def _quicksort(nums, begin, end, swaps, GRAPHICS):
        if begin >= end:
            return swaps 
        val = partition(nums, begin, end)
        pvt = val[0]
        swaps = val[1]
        if GRAPHICS:
            graph.updateGraph(plt, nums, sz)
            plt.pause(0.001)
        swaps += _quicksort(nums, begin, pvt-1, swaps, GRAPHICS)
        swaps += _quicksort(nums, pvt+1, end, swaps, GRAPHICS)
        return swaps

    swaps = _quicksort(nums, begin, end, swaps, GRAPHICS)
    return swaps

def insertion(nums, sz, graph, plt, GRAPHICS):
    swaps = 0
    for i in range(1, sz):
        val = nums[i]
        pos = i
        while pos > 0 and nums[pos-1] > val:
            nums[pos] = nums[pos-1]
            pos -= 1
            swaps += 1
            if GRAPHICS:
                graph.updateGraph(plt, nums, sz)
                plt.pause(0.001)
        nums[pos] = val
    return swaps

def selection(nums, sz, graph, plt, GRAPHICS):
    swaps = 0
    for i in range(sz):
        minElementIndex = i
        for j in range(i+1, sz):
            if(nums[j] < nums[minElementIndex]):
                minElementIndex = j
        if(minElementIndex != i):
            tmp = nums[i]
            nums[i] = nums[minElementIndex]
            nums[minElementIndex] = tmp
            swaps += 1
            if GRAPHICS:
                graph.updateGraph(plt, nums, sz)
                plt.pause(0.001)
    return swaps

def shell(nums, sz, graph, plt, GRAPHICS):
    swaps = 0
    # generate gaps of N/2^k
    gaps = [int(sz/ pow(2,k)) for k in range(sz)]
    for gap in gaps:
        for i in range(gap, sz):
            temp = nums[i]

            j = i
            while j >= gap and nums[j-gap] > temp:
                nums[j] = nums[j-gap]
                swaps += 1
                if GRAPHICS:
                    graph.updateGraph(plt, nums, sz)
                    plt.pause(0.001)
                j -= gap
            nums[j] = temp
            swaps += 1
    return swaps

def default_sort(nums, sz, graph, plt, GRAPHICS):   
    for i, e in enumerate(sorted(nums)):
        nums[i] = e 
        if GRAPHICS:
            graph.updateGraph(plt, nums, sz)
            plt.pause(0.001)

'''
FUNCTION merge
recursive merge sort function
@return number of swaps
'''
def merge(nums, sz, graph, plt, GRAPHICS):
    swaps = 0
    if sz > 1:
        mid = sz // 2
        left = nums[:mid]
        right = nums[mid:]
        
        swaps += merge(left, len(left), graph, plt, GRAPHICS)
        swaps += merge(right, len(right), graph, plt, GRAPHICS)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                swaps += 1
                j += 1
                
            k += 1
            
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        
    if GRAPHICS:
        graph.updateGraph(plt, nums, sz)
        plt.pause(0.001)
    
    return swaps
        
'''
FUNCTION inMerge
in-place merge sort function
@return number of swaps
'''
def inMerge(nums, sz, graph, plt, GRAPHICS):
    unit = 1
    swaps = 0
    while unit <= sz:
        h = 0
        for h in range(0, sz, unit * 2):
            l, r = h, min(sz, h + 2 * unit)
            mid = h + unit
            p, q = l, mid
            while p < mid and q < r:
                if nums[p] < nums[q]:
                    p += 1
                else:
                    tmp = nums[q]
                    nums[p + 1: q + 1] = nums[p:q]
                    nums[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1
                    swaps += 1
        unit *= 2
        if GRAPHICS:
            graph.updateGraph(plt, nums, sz)
            plt.pause(1)
            
    return swaps

