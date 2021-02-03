# double cycle
def bubbleSort(array):
    for i in range(len(array)):
        for j in (i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

# find the smallest number of this array, exchange it with the first element
def selectionSort(array):
    for i in range(len(array)):
        minimum = ip
        for j in range(i+1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
    return array

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

# time: propotional to NlogN
# space(extra): proptional to N


def merge(array):
    if len(array) > 1:
        mid = len(array) // 2
        L = array[:mid]
        M = array[mid:]
        merge(L)
        merge(M)
        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
    return array

