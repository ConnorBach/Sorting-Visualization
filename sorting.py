import graph

def insertion_sort(curve,nums, start=0, end=None):
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

        curve.setData(nums)
        yield

    return swaps

def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]

def quicksort(curve, nums, start=0, end=None):
    # Default Parameter Correction
    if end is None:
        end = len(nums)
    # Smaller Sorts --> insertion_sort
    # Larger Sorts --> quicksort
    # Without using insertion, would need an if making sure length > 1
    if end-start <= 10:
        yield from insertion_sort(curve,nums, start, end)
    else:
        p = partition(nums, start, end)
        yield from quicksort(curve, nums, start, p)
        yield from quicksort(curve, nums, p+1, end)

def partition(nums, start, end):
    # Initialization
    current = start
    # Sorting by pivot
    for i in range(start, end):
        if nums[i] < nums[end-1]:
            swap(nums, current, i)
            current+=1
    # Move pivot between sorted sections
    swap(nums, current, end-1)
    return current
