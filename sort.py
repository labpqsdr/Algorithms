# Bubble Sort
# feature: double cycle
def bubbleSort(array):
    for i in range(len(array)):
        for j in (i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

# Selection Sort
# find the smallest number of this array, exchange it with the first element
def selectionSort(array):
    for i in range(len(array)):
        minimum = ip
        for j in range(i+1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
    return array

# Insertion Sort
# always make the front part ordered, like playing cards
# example: i=1, array[1] only has one element, which is ordered
# the thing we need to do is put another element in this ordered array, and check the element we put has the right order
# cycle this process, we can have an ordered array
def insertionSort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
    return array

# Shell Sort
# make the elements with any interval in the dispersion are ordered
def shellSort(array):
    N = len(array)
    gap = N // 2
    while gap > 0:
        for i in range(gap, N):
            for j in range(i, 0, -gap):
                if array[j] < array[j-gap]:
                    array[j-gap], array[j] = array[j], array[j-gap]
        gap = gap // 2
    return array

# Merge Sort
# time: propotional to NlogN
# space(extra): proptional to N
def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array

# Quick Sort
# the most useful sort algorithms
def quickSort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)
    return array

def partition(array, low, high):
    i = low-1
    v = array[high]

    for j in range(low, high):
        if array[j] <= v:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

# Quick sort(alt)
# 1. use insertion sort when short array
def quickSort_alt_1(array, low, high):
    if (high <= low+5):
        return insertionSort(array)
    else:
        return quickSort(array, low, high)
