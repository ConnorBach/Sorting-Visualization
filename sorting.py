#contains all sorting algorithms
def bubble(nums, graph, plt):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if(nums[j] > nums[j+1]):
                #swap element
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
            #update graph
            graph.updateGraph(plt, nums)
            plt.pause(0.001)
#TODO: Add more sorting algorithms