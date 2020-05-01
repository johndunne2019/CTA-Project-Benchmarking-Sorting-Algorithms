# 5. Selection Sort
#sourced from: https://stackabuse.com/sorting-algorithms-in-python/#selectionsort
#Added my own comments 

def selection_sort(nums):
    # Selection sort uses the left part of the unsorted list to store the sorted sub-list which grows at every iteration
    # This value of i increases with each iteration and the unsorted sub-list becomes smaller
    for i in range(len(nums)):
        # Selection sort assumes the first element is the smallest 
        lowest_value_index = i
        # For loops iterates over all the elements from index 1 to the end of the collection
        for j in range(i + 1, len(nums)):
            # if the an element is found that is smaller than the element at index 0
            if nums[j] < nums[lowest_value_index]:
                # that element is then set as the lowest value in the collection
                lowest_value_index = j
        # The exchange is made:
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]