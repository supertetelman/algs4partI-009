#!/usr/bin/env python
'''Python Test of Shell Sort, Insertion Sort, Select Sort, and Shuffle for Coursera Algorithm class questions'''

from time import time
from random import random, randint

from simple_sort import *

__author__ = "Adam Tetelman"


def test_shuffle(N, printme = False):
    start = time()
    a = shuffle(range(N))
    if printme:
        print a
    shuffle_time = time() - start
    print "Shuffle took %d seconds for %d values" % (shuffle_time, N)
    start_slow = time()
    a = slowshuffle(range(N))
    if printme:
        print a
    a = slow_time = time() - start_slow
    print "Slow shuffle took %d seconds for %d values" % (slow_time, N)


def test_sort(test, k, printme = False):
    N = len(test)
    test1 = test[:]
    test2 = test[:]
    test3 = test[:]

    if printme:
        print "Starting test with these shuffles values", test
        print "\n".join(str(l) for l in [test1, test2, test3])

    start = time()
    k_shellsort(test1, k, printme)
    res = time() - start
    print "Shell Sort took %d seconds for %d values and these iterations:" %(res, N), k 
    if not issorted(test1):
        print "Something went wrong sorting the list - Insert Sort"
        print test1
        return -1

    start = time()
    insertsort(test2, printme)
    res = time() - start
    print "Insert Sort took %d seconds for %d values" %(res, N) 
    if not issorted(test2):
        print "Something went wrong sorting the list - Insert Sort"
        return -1

    start = time()
    selectsort(test3, printme)
    res = time() - start
    print "Select Sort took %d seconds for %d values" %(res, N) 
    if not issorted(test3):
        print "Something went wrong sorting the list - Select Sort"

    if printme:
        print "\n".join(str(l) for l in [test1, test2, test3])
        return -1


def create_semi_sorted(N, j=10, k=2, printme=False):
    rand_lists = []
    test = range(N)

    for lists in range(k):
        rand_lists.append([int(N * random()) for i in range(j)])

    for l in range(k):
        rnd = randint(0, N)
        test = test[0:rnd] + rand_lists[l] + test[rnd+1:]
        
    if printme:
        print "Semi Sorted test set will look like this", test
    return test


N = 10000
k = [11, 7, 5, 3, 1]

test = range(N)
test2 = create_semi_sorted(N)
shuffle(test)

test_shuffle(N)
test_sort(test,k)
test_sort(test2,k)
