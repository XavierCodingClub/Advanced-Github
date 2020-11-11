##
# Module to store various algorithms
#
# Author: XCC
# Date: 10/25/2020
#


def bubbleSort(list):
    list = list.copy()
    for i in range(len(list)):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i+1], list[i]
    return list


def insertionSort(list):
    list = list.copy()
    for i in range(1, len(list)):
        j = 0
        while list[i] > list[j]:
            j += 1
        num = list[i]
        list.pop(i)
        list.insert(j, num)
    return list


def selectionSort(list):
    list = list.copy()
    for i in range(len(list)):
        num = i
        for j in range(i + 1, len(list)):
            if list[num] > list[j]:
                num = j
        list[i], list[num] = list[num], list[i]
    return list
