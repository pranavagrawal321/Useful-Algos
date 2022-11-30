def binary_search(arr, element):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return -1
