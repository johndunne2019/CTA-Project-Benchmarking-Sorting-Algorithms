# 4. Insertion Sort
# Code sourced from: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html
#Added my own comments

# Create an insertion sort function
def insertionSort(alist):
    # for loop to iterate over the list from index 1 to the end of the list
    # we need n-1 passes to sort an input size n 
   for index in range(1,len(alist)):
    # the position of the current item in the list is stored as currentvalue
     currentvalue = alist[index]
     position = index
    # while loop checks the index of the element is greater than index zero
    # The current element is compared to the element to its left
    # if the position to its left is less than a shift operation will be made
     while position>0 and alist[position-1]>currentvalue:
         # this is the shift operation that moves the element back at each iteration of the while loop
         # an element on the right that is less than an element on the left when compared is shifted to the left
         alist[position]=alist[position-1]
         # Note the variable position holds the new value of the sorted sub list
         # This is not a complete exchange
         position = position-1
    # The sorted sublist is held in the variable position and this is now set equal to alist
     alist[position]=currentvalue