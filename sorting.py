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