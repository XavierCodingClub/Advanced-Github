##
# Module to store various algorithms
#
# Author: XCC
# Date: 10/25/2020
#


def bubbleSort(ls):
    is_sorted = False
    while not is_sorted:
        for i in range(len(ls)):
            next_element = None
            try:
                next_element = ls[i+1]
            except IndexError:
                break
            if ls[i] > next_element:
                temp_i = int(ls[i+1])
                ls[i+1] = int(ls[i])
                ls[i] = temp_i
        for i in range(len(ls)):
            next_element = None
            try:
                next_element = ls[i+1]
            except IndexError:
                break
            if ls[i] < ls[i+1]:
                is_sorted = True
            else:
                is_sorted = False
                break
    return ls

def insertionSort(ls):
    return ls


def selectionSort(ls):
    return ls
