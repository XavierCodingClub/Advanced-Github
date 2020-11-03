##
# Module to store various algorithms
#
# Author: XCC
# Date: 11/03/2020
# Edited by: Ayaan D.


def bubbleSort(ls):
    lengthOfList = len(numList)
    for i in range(lengthOfList):
        for j in range(0, lengthOfList - i - 1):
            if numList[j] > numList[j+1]:
                numList[j], numList[j+1] = numList[j+1], numList[j]
    return ls


def insertionSort(ls):
    lengthOfList = len(numList)
    for i in range(1, lengthOfList):
        position = numList[i]
        j = i-1
        while j >= 0 and position < numList[j]:
            numList[j+1] = numList[j]
            j -= 1
        numList[j+1] = position
    
    return ls


def selectionSort(ls):
    lengthOfList = len(numList)
    for i in range(lengthOfList):
        indexOfMinimum = i
        for j in range(i+1, lengthOfList):
            if numList[indexOfMinimum] > numList[j]:
                indexOfMinimum = j
        numList[i], numList[indexOfMinimum] = numList[indexOfMinimum], numList[i]
    
    return ls
