def binary_search(data: list[int], key: int, low: int, high: int) -> int:
        mid: int = (low + high) // 2
        
        if low > high:          # Base Case 1
            return -1
        elif key == data[mid]:    # Base Case 2
            return mid
        if key < data[mid]:     # Recursive Case 1
            return binary_search(data, key, low, mid - 1)
        else:
            return binary_search(data, key, mid + 1, high)
    