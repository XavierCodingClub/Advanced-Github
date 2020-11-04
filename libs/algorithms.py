##
# Module to store various algorithms
#
# Author: Luke Sequeira
# Date: November, 2020
#


def bubbleSort(a):
    lst = a.copy()
    lnt = len(lst)
    for i in range(lnt):
        for j in range(lnt - 1):
            if(lst[j] >  lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j] #switch j and j + 1
    return lst


def insertionSort(a):
    lst = a.copy()
    lnt = len(lst)
    for i in range(lnt-1): #loop from 2nd to last element (since list of len 1 is trivially sorted)
        key = lst[i + 1]
        j = i
        while(j >= 0 and key < lst[j]):
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def selectionSort(a):
    lst = a.copy()
    lnt = len(lst) - 1
    for i in range(lnt):
        key = i
        for j in range(i + 1, lnt + 1):
            if(lst[j] < lst[key]):
                key = j
        lst[key], lst[i] = lst[i], lst[key]
    return lst

