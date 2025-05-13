#6-5-25
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1        # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  

    # Place pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partition index
        quick_sort(arr, low, pi - 1)    # Sort left part
        quick_sort(arr, pi + 1, high)   # Sort right part

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)
