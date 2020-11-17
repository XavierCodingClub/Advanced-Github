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

def mergeSort(a):
    if(len(a) > 1): #non trivially-sorted list
        mdle = len(a)//2 #find the mid-point of the list
        L = a[:mdle] #left half of array
        R = a[mdle:] #right half of array

        #Call merge sort on the 2 halfs
        mergeSort(L)
        mergeSort(R)

        #merge the 2 sorted halfs
        i = 0
        j = 0
        k = 0
        while(i < len(L) and j < len(R)): #this loop runs len(a) times
            if(L[i] < R[j]):
                a[k] = L[i]
                i += 1
                k+=1
            else:
                a[k] = R[j]
                j += 1
                k+=1
        # Checking if any element was left
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1
    return a