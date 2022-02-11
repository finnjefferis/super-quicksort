# SUPER QUICKSORT

import numpy as np
import termplotlib as tpl


# print values to console
print("""███████╗██╗   ██╗██████╗ ███████╗██████╗      ██████╗ ██╗   ██╗██╗ ██████╗██╗  ██╗███████╗ ██████╗ ██████╗ ████████╗
██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗    ██╔═══██╗██║   ██║██║██╔════╝██║ ██╔╝██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝
███████╗██║   ██║██████╔╝█████╗  ██████╔╝    ██║   ██║██║   ██║██║██║     █████╔╝ ███████╗██║   ██║██████╔╝   ██║   
╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗    ██║▄▄ ██║██║   ██║██║██║     ██╔═██╗ ╚════██║██║   ██║██╔══██╗   ██║   
███████║╚██████╔╝██║     ███████╗██║  ██║    ╚██████╔╝╚██████╔╝██║╚██████╗██║  ██╗███████║╚██████╔╝██║  ██║   ██║   
╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝     ╚══▀▀═╝  ╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════
═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                                                                                    """)

# initialise array of randomised integers
randnums = np.random.randint(1, 12, 12)

# declare start and end values
start = randnums[0]
end = randnums[11]

# declare pivot
pivot = start
print("Pivot is " + str(pivot))
print("Unsorted values graph")
fig = tpl.figure()
fig.barh(randnums, force_ascii=False)
fig.show()


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # Compare pivot to subarray
 
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
    




array = randnums

sorted = quick_sort(array, 0, len(array) - 1)
print("Sorted values graph")
fig = tpl.figure()
fig.barh(array, force_ascii=False)
fig.show()
