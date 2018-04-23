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
        graph.updateGraph(plt, nums, sz)
        plt.pause(0.001)
        swaps += _quicksort(nums, begin, pvt-1, swaps)
        swaps += _quicksort(nums, pvt+1, end, swaps)
        return swaps

    swaps = _quicksort(nums, begin, end, swaps)
    return swaps
