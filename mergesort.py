#29-April-2025
def merge(arr, left, mid, right):
    leftArr = arr[left:mid + 1]
    rightArr = arr[mid + 1:right + 1]
    
    i = 0
    j = 0
    k = left

    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1
    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1

    while j < len(rightArr):
        arr[k] = rightArr[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Driver code
arr = [12, 45, 66, 90, 67]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted Array is:", arr)
