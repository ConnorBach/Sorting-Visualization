#contains all sorting algorithms

'''
FUNCTION bubble
@param nums - list of numbers to sort
@param sz - size of list
@param graph - module for graphing
@param plt - matplotlib plt
@return number of swaps
'''
def bubble(nums, sz, graph, plt):
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
            graph.updateGraph(plt, nums, sz)
            plt.pause(0.001)
    return swaps
#TODO: Add more sorting algorithms

'''
FUNCTION partion
Quick sort helper function
'''
def partition(nums, begin, end, swaps):
    pvt = begin
    for i in range(begin+1 , end+1):
        if(nums[i] <= nums[begin]):
            pvt += 1
            nums[i], nums[pvt] = nums[pvt], nums[i]
            swaps += 1
            print(swaps)
    nums[pvt], nums[begin] = nums[begin], nums[pvt]
    swaps += 1
    return [pvt, swaps]

'''
FUNCTION quick
quick sort function
@return number of swaps
'''
def quick(nums, sz, graph, plt):
    begin = 0
    end = (sz-1)
    swaps = 0

    def _quicksort(nums, begin, end, swaps):
        if begin >= end:
            return 0 
        val = partition(nums, begin, end, swaps)
        pvt = val[0]
        swaps = val[1]
        print('above ', swaps)
        graph.updateGraph(plt, nums, sz)
        plt.pause(0.001)
        _quicksort(nums, begin, pvt-1, swaps)
        print('first ', swaps)
        _quicksort(nums, pvt+1, end, swaps)
        print('second ', swaps)

    swaps = _quicksort(nums, begin, end, swaps)
    return swaps

def insertion(nums, sz, graph, plt):
    swaps = 0
    print('in insertion')
    for i in range(1, sz):
        val = nums[i]
        pos = i
        while pos > 0 and nums[pos-1] > val:
            nums[pos] = nums[pos-1]
            pos -= 1
            swaps += 1
            graph.updateGraph(plt, nums, sz)
            plt.pause(0.001)
        nums[pos] = val
    return swaps