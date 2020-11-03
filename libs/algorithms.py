##
# Module to store various algorithms
#
# Author: Luke Sequeira
# Date: November, 2020
#


def bubbleSort(lst):
    lnt = len(lst)
    for i in range(lnt):
        for j in range(lnt - 1):
            if(lst[j] >  lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j] #switch j and j + 1
    
    return lst


def insertionSort(lst2):
    return lst2


def selectionSort(lst3):
    return lst3
