# 1. Bubble Sort
# Code sourced from: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBubbleSort.html
# Added my own comments
# Bubble Sort has the capability to stop running when the list becomes sorted

# Bubble sort function is created taking one input
def bubbleSort(alist):
    # A variable called exchanges is created and set to true 
    exchanges = True
    # the variable passnum is set to the size of the input array minus 1 
    passnum = len(alist)-1
    # while loop executes while there is more than one element in the array and there are exchanges to be made
    while passnum > 0 and exchanges:
        # exchanges set to false at beginning of the loop
        exchanges = False
        # An inner for loop traverses each element in passnum array
        for i in range(passnum):
            # if the element on the left is greater than the element on the right then we must swap positions and set exchanges to boolean true
            if alist[i]>alist[i+1]:
                exchanges = True
                # the element on the left is stored in a temporary variable
                temp = alist[i]
                # element on the left set equal to the element on its right
                alist[i] = alist[i+1]
                # the element that was originally on the left is moved from temp storage to the right position
                alist[i+1] = temp
                # Without the temp storage the left would be overwritten 
        # the new value od passnum is the previous array length minus 1 as we one less element to sort
        passnum = passnum-1