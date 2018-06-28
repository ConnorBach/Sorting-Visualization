import graph

def insertion_sort(plt, nums, start=0, end=None):
    swaps = 0
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
        nums[j+1] = x
        graph.draw_barchart(plt, nums)

    return swaps
