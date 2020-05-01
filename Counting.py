# 3. Counting Sort
#Code sourced from: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php
# Added my own comments
# I found it hard to find good examples of this sorting algorithm online 
# I had to change the function to only take an array as input as I wont be entering a max val when benchmarking 

# In the source code the function accepts:
#def counting_sort(array1, max_val):
    #m = max_val + 1
def counting_sort(array1):
# I changed the sourced code to have a set max val of 100 
# I chose this as I am generating random integers up to 100 in the benchmarking
    m = 100 + 1   # array created of size of range of input plus one 
    count = [0] * m                
    
    for a in array1:
    # for loop loops through input array and counts number of occurrences 
    # the count is stored used a counter
        count[a] += 1             
    i = 0
    for a in range(m):       #loop to iterate every element in array     
        for c in range(count[a]):  #inner loops to iterate over each occurrence of a key
            array1[i] = a #the sorted array is being built and stored in array1 
            i += 1  
    #sorted array is returned 
    return array1