def binary_search(arr, target):
    """
    Performs a binary search on a sorted array to find the target element.

    Args:
        arr: A sorted list or array of elements.
        target: The element to search for.

    Returns:
        The index of the target element if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Target found at mid index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Target not found in the array

# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
search_target = 11

result = binary_search(my_list, search_target)
