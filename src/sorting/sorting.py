# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # Create indexes for all our arrays
    a = 0
    b = 0
    m = 0

    # Keep the while going until the len of the array is greater than our index so we can go through the whole array
    # Create if statements to check for the smaller index and add that to the array, then increase the index to go through the next part of the array.
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[m] = arrA[a]
            a += 1
            m += 1
        else:
            merged_arr[m] = arrB[b]
            b += 1
            m += 1

    # Checks for any remaining indexes in arrays then adds them to the merged array and increases the index
    while a < len(arrA):
        merged_arr[m] = arrA[a]
        a += 1
        m += 1
    while b < len(arrB):
        merged_arr[m] = arrB[b]
        b += 1
        m += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here

    # Check if the array can still be split by checking if it is less than 1
    if len(arr) <= 1:
        return arr

    # Create a middle index that floors
    mid = int(len(arr)//2)

    # Use recursion to split the indexes of the array in the middle, one going left to the lowest index and one going right to the highest index
    arrA = merge_sort(arr[:mid])
    arrB = merge_sort(arr[mid:])

    # The arrays are compared and merged back together up the recursion tree
    return merge(arrA, arrB)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
