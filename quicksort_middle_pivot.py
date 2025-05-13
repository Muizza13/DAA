def quickalgo(array):
    quicksort(array, 0, len(array) - 1)

def quicksort(array, s, e):
    if s < e:
        mid = (s + e) // 2
        pivot = array[mid]        #middle element pivot
        index = partition(array, s, e, pivot)
        quicksort(array, s, index - 1)
        quicksort(array, index, e)

def partition(array, l, r, pivot):
    while l <= r:
        while array[l] < pivot:
            l += 1
        while array[r] > pivot:
            r -= 1
        if l <= r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1
    return l

numbers = [2, 9, 5, 8, 0, 1]
print("Before sort: ", numbers)
quickalgo(numbers)
print("After sort: ", numbers)
