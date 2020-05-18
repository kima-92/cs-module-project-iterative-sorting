# TO-DO: Complete the selection_sort() function below

def selection_sort(arr):
    # loop through n-1 elements

    # For each element in the array
    for i in range(0, len(arr)):
        #print(f"i: {i}")

        # Save the current_index of this element
        cur_index = i
        # Set smallest_index as current_index
        smallest_index = cur_index

        # For each element exept current_index ( y )
        for y in range(i + 1, len(arr)):
            #print(f"y {y}")

            # Compare the value in current_index 
            # to the value in smallest_index

            # If the value of smallest_index is 
            # bigger than the value in index y
            if arr[smallest_index] > arr[y]:
                # Set smaller_index to y
                smallest_index = y
        
        # If current_index is not smallest_index
        if cur_index != smallest_index:
            # Swap the values of current_index and smalest_index
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
            
    # Return the sorted array
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Set did_swap bool, to store whether 
    # we did a swp or not
    did_swap = True

    # while did_swap is true
    while did_swap == True:
        # set did_swap to false
        did_swap = False

        # Grab the element to the left
        for left_index in range(0, len(arr)):
            # Grab the element to the right
            for right_index in range(left_index + 1, len(arr)):

                # If left is greater than right
                if arr[left_index] > arr[right_index]:
                    # Swap
                    arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
                    # set did_swap to true
                    did_swap = True
                
    # Return the sorted array
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
