#!/usr/bin/env python
'''Python implementation of Shell Sort, Insertion Sort, Select Sort, Shuffle for Coursera Algorithm class questions'''

from random import random, randint

import union_find

__author__ = "Adam Tetelman"


def shellsort(array, N, printme=False):
    '''Takes an array of integers and value N and sorts it using the N-Shell Sort algorithm'''
    for i in range(N - 1, len(array), N):
        for j in range(i, 0, -1):
            if array[j] >= array[j - 1]:
                break
            swap = array[j - 1]
            array[j - 1] = array[j]
            array[j] = swap
            if printme:
                print "Shell sort iteration %d:%d resulted in" %(i, j), array
    return array


def k_shellsort(array, k, printme=False):
    '''Takes a list of values and iterates through shellsort with those gap sizes'''
    for N in k:
        if printme:
            print "Running shellsort with %d" %(N)
        shellsort(array, N, printme)
    return array


def insertsort(array, printme=False):
    '''Takes an array of integers and sorts it using the Insert Sort algorithm'''
    return shellsort(array, 1, printme)


def selectsort(array, printme=False):
    '''Takes an array of integers and sorts it using the Select Sort algorithm'''
    for i in range(len(array)):
        if printme:
            print array    
        min = i
        for j in range(i, len(array)):
            if array[j] < array[min]:
                min = j
        if printme and i == min:
            print "No Exchange"
        elif printme:
            print "Exchanged %d:%d for %d:%d" % (i, array[i], min, array[min])
        min_value = array[min]
        array[min] = array[i]
        array[i] = min_value
    return array


def issorted(array):
    for i in range(len(array) -1):
        if array[i] > array[i + 1]:
            return False
        return True


def slowshuffle(array):
    rnd_dist = {}
    for i in range(len(array)):
        rnd_dist[i] = random()    

    for i in range(len(array)):
        for j in range(i, 0, -1):
            if rnd_dist[j] >= rnd_dist[j - 1]:
                break
            swap = rnd_dist[j - 1]
            swap_array = array[j - 1]
            rnd_dist[j - 1] = rnd_dist[j]
            array[j - 1] = array[j]
            rnd_dist[j] = swap
            array[j] = swap_array
    return array


def shuffle(array):
    for i in range(len(array)):
        rnd = randint(0, i)
        swap = array[i]
        array[i] = array[rnd]
        array[rnd] = swap
    return array
