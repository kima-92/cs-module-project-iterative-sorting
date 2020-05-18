

def linear_search(arr, target):
    # For each index in the array
    for i in range(0, len(arr)):
        # If the element at this index
        # matches the target
        if arr[i] == target:
            # return the index in which 
            # this elements is stored
            return i
        
    
    # If it never returns True
    # Return -1
    return -1



# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Set taget_found bool, to store whether you found the taget or not
    target_found = False

    # Set low to 0
    low = 0
    # Set hight to the last index in arr
    high = len(arr) - 1

    # While target_found is false
    # and the lenght of arr is not 0
    while target_found == False and len(arr) != 0:

        # Set the midpoint of arr
        midpoint = (low + high) // 2

        # If the midpoint is the target
        if arr[midpoint] == target:

            # Set target_found to true
            target_found = True
            # return the index in which the target is at
            return midpoint

        # If the midpoint is greater than target
        if arr[midpoint] > target:
            # We have to focus on the left_side, and
            # discard the entire right_side

            # Set high to be the midpoint
            high = midpoint

        # If the midpoint is less than target
        if arr[midpoint] < target:
            # We have to focus on the right_side, and
            # discard the entire left_side

            # Set low as the midpoint
            low = midpoint

    # If it was not found, return -1
    return -1  # not found
