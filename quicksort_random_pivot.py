def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = 1
    pivot = arr[pivot_index]
    rest = arr[:pivot_index] + arr[pivot_index+1:]

    less = [x for x in rest if x <= pivot]
    greater = [x for x in rest if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

arr = [2, 9, 7, 8, 5, 4]
arr2 = quick_sort(arr)
print(arr2)