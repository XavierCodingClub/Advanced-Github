##
# Module to store various algorithms
#
# Author: XCC
# Date: 10/25/2020
#


def bubbleSort(ls):
    is_sorted = False
    while not is_sorted:
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i+1], ls[i] = int(ls[i]), int(ls[i+1])
        for i in range(len(ls) - 1):
            if ls[i] < ls[i+1]:
                is_sorted = True
            else:
                is_sorted = False
                break
    return ls.copy()

def insertionSort(ls):
    return ls


def selectionSort(ls):
    return ls
