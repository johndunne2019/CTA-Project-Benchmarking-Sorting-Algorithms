# 2. Merge Sort
# Code sourced from: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
# Added my own comments

# Merge sort function created taking a list as input
# First half of the code concerned with splitting the lists into sub-lists
def mergeSort(alist):
    # print statement prints out the result of splitting the list into sub-lists, will comment out later
    #print("Splitting ",alist)
    # if statement will execute on lists with more than one element
    if len(alist)>1:
        # mid point of the list found 
        mid = len(alist)//2
        # list sliced into left and right halves or sub-lists
        # left half contains from start of list to mid point and right half from mid point to the end of list
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        # mergeSort function is called on both halves to sort the lists
        mergeSort(lefthalf)
        mergeSort(righthalf)
        # The sub-lists are now sorted

        # From here on the code is concerned with merging the smaller sorted lists into a final sorted list
        i=0
        j=0
        k=0
        # While loops executes as long as both sub-lists contain at least one element
        while i < len(lefthalf) and j < len(righthalf):
            # if the element in the left half is less or equal to than the element in the right half it is stored in alist k
            # this ensures the algorithm is stable as for elements with equal sort keys the element for the left half is places on the left
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            # else statement executes if element on left half is not less than or equal to element in right half
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
            # the values of i, j and k are incremented after the execution of the relevant section of code
        # The above while loop will execute as long as both sub-lits contain at least one element
        # In the case of uneven numbers then one sub-list may have an element left and the other wll be empty
        # Two additional while loops are added to deal with these cases

        # This while loop will execute as long as there is an element present in the left half sub-list
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        # This while loop will execute as long as there is an element present in the right half of the sub-list
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    # print statement that shows the merging process in progress, will comment out later
   # print("Merging ",alist)
