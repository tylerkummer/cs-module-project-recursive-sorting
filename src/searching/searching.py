# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # Make sure the start of the array is not bigger than the end of the array for the binary search tree
    if start <= end:
        # Create a middle index based on the start and end where we floor the division
        mid = (start + end) // 2

        # If the target element is in the middle of the array then return it
        if arr[mid] == target:
            return mid

        # Checks if the target is smalled than mid, and places it in the left subtree.
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        # Target must be bigger than middle index so it goes in the right subtree
        else:
            return binary_search(arr, target, mid + 1, end)

    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
