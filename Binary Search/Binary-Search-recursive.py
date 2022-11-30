def binary_search(arr, element):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == element:
            return True
        else:
            if element < arr[mid]:
                return binary_search(arr[:mid], element)
            else:
                return binary_search(arr[mid + 1:], element)
