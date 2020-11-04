##
# Program to accept and sort numbers in a list, aswell as measure how long it took
#
# Author: XCC
# Date: 10/25/2020

from libs import algorithms
import timeit

# Initialize list variable
numList = []


done = False
# Loop until user is satisfied
while(not done):

    numInput = input(
        "Enter a number to add to the list, if you wish to stop adding numbers enter 'q': \n")
    # Quit out of loop when user says to
    if numInput == 'q':
        done = True
        break

    # Try except to catch ValueError when converting string input to int
    try:
        numList.append(int(numInput))
    except:
        print("Please enter a single number")

### Output the list sorted with various algoritms ###

# To compare, output the unsorted list
print("Unsorted list:" + str(numList))

## Bubble sort ##

# Output sorted
foo = numList
print("Sorted with bubble sort" + str(algorithms.bubbleSort(foo)))

# Time the sorting with timeit.timeit
time = timeit.timeit('algorithms.bubbleSort(foo)',
                     'from __main__ import algorithms, foo')

# Output the time it took in micro seconds
print("Time: " + str(time) + " micro sec")


## Insertion sort ##

# Output sorted
foo = numList
print("Sorted with insertion sort" + str(algorithms.insertionSort(foo)))

# Time the sorting with timeit.timeit
time = timeit.timeit('algorithms.insertionSort(foo)',
                     'from __main__ import algorithms, foo')

# Output the time it took in micro seconds
print("Time: " + str(time) + " micro sec")

## Selection sort ##

# Output sorted
foo = numList
print("Sorted with selection sort" + str(algorithms.selectionSort(foo)))

# Time the sorting with timeit.timeit
time = timeit.timeit('algorithms.selectionSort(foo)',
                     'from __main__ import algorithms, foo')

# Output the time it took in micro seconds
print("Time: " + str(time) + " micro sec")
