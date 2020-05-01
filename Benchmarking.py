# 6. Benchmarking of sorting algorithms
import time   # will be used to time the sorting algorithms
import random #will be used to generate random arrays of integers
import numpy as np # will use numpy.mean to return the average of an array of ten run times
import pandas as pd # will be used to output the results in a dataframe
import matplotlib.pyplot as plt #will be used to generate a plot of the data
# import the files containing the sorting algorithms
import Bubble
import Merge
import Counting
import Insertion
import Selection

def main(): #main function 
    print("Benchmarking process has begun, Please wait approximately 30 minutes for results")
    # create a function to generate random array of integers
    # sourced from sample given in the project specification
    # Python random module: https://docs.python.org/3/library/random.html
    def random_array(n):
        array = []
        for i in range(0, n, 1): # low, high, size 
            array.append(random.randint(0, 100))  # randomly generated arrays will contain integers in range 100
        return array

    #testing_arrays= [100, 250, 500, 750, 1000] # shorter list for testing
    testing_arrays = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 7500, 8750, 10000]
    
    average_bubble = [] #Create a list to hold the average time of ten runs
    average_merge = [] #I will calculate the average of the ten run times for each input size
    average_counting = [] #I will append the average for each input size to this list
    average_insertion = [] #Python append to a list: https://www.w3schools.com/python/ref_list_append.asp
    average_selection = []
    
    # for loop will loop through input size array & each input size will be used as input to the random array function
    for array in testing_arrays:
        benchmark_array = random_array(array) 
            # I will generate just one array for each input size and pass a copy of the array to the sorting algorithms
            # https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
            # this will be necessary to avoid passing an already sorted array to an algorithm on runs 2 through 10
        
        bubble_time = []  #create a list to hold running times for ten runs of each algorithm
        merge_time = [] # time for each run will be appended to this list
        counting_time = [] #I will then calculate the average time of the ten runs using numpy.mean
        insertion_time = []
        selection_time = []

        # for loop to loop through each input size ten times for the purpose of timing the algorithm ten times
        for runs in range (10):        
            #the first sorting algorithm will be timed using the Python time module 
            start_time = time.time()  #current time in seconds 
            Bubble.bubbleSort(list(benchmark_array)) #copied array passed into Bubble Sort algorithm
            finish_time = time.time()  #current time in seconds 
            time_elapsed = finish_time - start_time #time elapsed will be the difference between the start & finish times
            #print(time_elapsed) testing purposes, comment out
            bubble_time.append(time_elapsed)  #append the time to the container set up to hold the run times
        
            #repeat same procedure for the remaining 4 sorting algorithms:
        
            #Merge Sort time
            start_time = time.time()
            Merge.mergeSort(list(benchmark_array))
            finish_time = time.time()
            time_elapsed = finish_time - start_time
            #print(time_elapsed)
            merge_time.append(time_elapsed)
            
            #Counting sort time
            start_time = time.time()
            Counting.counting_sort(list(benchmark_array))
            finish_time = time.time()
            time_elapsed = finish_time - start_time
            #print(time_elapsed)
            counting_time.append(time_elapsed)
            
            #Insertion sort time
            start_time = time.time()
            Insertion.insertionSort(list(benchmark_array))
            finish_time = time.time()
            time_elapsed = finish_time - start_time
            #print(time_elapsed)
            insertion_time.append(time_elapsed)
            
            #Selection sort time
            start_time = time.time()
            Selection.selection_sort(list(benchmark_array))
            finish_time = time.time()
            time_elapsed = finish_time - start_time
            #print(time_elapsed)
            selection_time.append(time_elapsed)
    
        #print for testing purposes, comment out 
        #print(bubble_time)
        #print(merge_time)
        #print(counting_time)
        #print(insertion_time)
        #print(selection_time)
    
        # I will use numpy.mean to return the average time of the list holding the 10 run times for eacj input size
        # numpy.mean: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.mean.html
        #mutiply by 1000 to convert seconds to milliseconds 
        average_time_bubble_sort = np.mean(bubble_time)*1000
        average_bubble.append(average_time_bubble_sort)  #append the average time for each input size to the average time list
        #print(f"Average time for Bubble Sort on Input Size {array} : {average_time_bubble_sort}") 
        # print for testing purposes, comment out later
    
        average_time_merge_sort = np.mean(merge_time)*1000
        average_merge.append(average_time_merge_sort)
        #print(f"Average time for Merge Sort on Input Size {array} : {average_time_merge_sort}")
        
        average_time_counting_sort = np.mean(counting_time)*1000
        average_counting.append(average_time_counting_sort)
        #print(f"Average time for Counting Sort on Input Size {array} : {average_time_counting_sort}")
        
        average_time_insertion_sort = np.mean(insertion_time)*1000
        average_insertion.append(average_time_insertion_sort)
        #print(f"Average time for Insertion Sort on Input Size {array} : {average_time_insertion_sort}")
        
        average_time_selection_sort = np.mean(selection_time)*1000
        average_selection.append(average_time_selection_sort)
        #print(f"Average time for Selection Sort on Input Size {array} : {average_time_selection_sort}")
        
    #print out the array containing the average run for all input sizes, cross check against pandas dataframe for testing   
    #print(f"Average time Bubble {average_bubble}")
    #print(f"Average time Merge {average_merge}")
    #print(f"Average time Counting{average_counting}")
    #print(f"Average time Insertion {average_insertion}")
    #print(f"Average time Selection {average_selection}")

    #Next step to create pandas dataframe

    #pandas.DataFrame: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
    df_average_times = pd.DataFrame() #create a pandas dataframe
    #add columns to the pandas dataframe
    df_average_times['Input Size'] = testing_arrays #the array of input szes will be the first column
    df_average_times['Bubble Sort'] = average_bubble #the average run times for all sorting algorithms will be next columns 
    df_average_times['Merge Sort'] = average_merge
    df_average_times['Counting Sort'] = average_counting
    df_average_times['Insertion Sort'] = average_insertion
    df_average_times['Selection Sort'] = average_selection
    #pandas.DataFrame.set_index: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html
    df_average_times.set_index('Input Size', inplace=True) #set the index as the input size 
    #df_average_times.round(3) show dataframe for testing, comment out
    #display the dataframe & round to 3 decimal places: https://www.geeksforgeeks.org/python-pandas-dataframe-round/
    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.round.html

    #transpose() dataframe can be accessed with the property T
    print(df_average_times.round(3).T)
    # transpose dataframe: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transpose.html
    # https://www.geeksforgeeks.org/python-pandas-dataframe-transpose/
    #round dataframe output to 3 decimal places: https://www.geeksforgeeks.org/python-pandas-dataframe-round/

    df_average_times.round(3).T.to_csv('Benchmark_Results.csv') 
    #send data from dataframe to a csv file: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
    
    #Plot the average run times from the pandas dataframe
    #matplotlib pyplot documentation: https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.html
    # rc params to customize plot appearance: https://matplotlib.org/tutorials/introductory/customizing.html
    plt.rcParams['figure.figsize'] = (20, 10)
    plt.rcParams['lines.linewidth'] = 2.5
    plt.rcParams['font.size'] = 15.0
    plt.rcParams['font.weight'] = 'bold'

    # add the columns of data to the plot from the pandas dataframe 
    #pyplot;plot: https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
    plt.plot(df_average_times['Bubble Sort'], marker='o', markersize=10)  #add marker to show each input size on the lines
    plt.plot(df_average_times['Merge Sort'], marker='o', markersize=10)
    plt.plot(df_average_times['Counting Sort'], marker='o', markersize=10)
    plt.plot(df_average_times['Insertion Sort'], marker='o', markersize=10)
    plt.plot(df_average_times['Selection Sort'], marker='o', markersize=10)

    # add a title to the plot: https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title
    plt.title('Average run time of sorting algorithms over ten runs of varying Input Sizes n')

    # add labels to x and y axis : https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel
    plt.xlabel('Input Size n')
    plt.ylabel('Average of ten runs in millseconds')

    # add a grid: https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid
    plt.grid()
    # add a legend: https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend
    plt.legend()
    # pyplot.show to display the plot: https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show
    #plt.show()
    plt.savefig('Benchmark_Plot.png') # save the figure: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.savefig.html

if __name__ == "__main__":
    main()    #script will be ran if called as main