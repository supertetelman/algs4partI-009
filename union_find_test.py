#!/usr/bin/env python
'''Python Test of Union-Find for Coursera Algorithm class questions'''

import math
import time

from union_find import *

__author__ = "Adam Tetelman"


def iterate_string(test,string,printme,f):
    '''Return a list of tuples'''
    res = []
    for tuple in string.split(" "):
        set = tuple.split("-")
        if f == "union":
            test.union(int(set[0]),int(set[1]))
        if f == "connected":
            res.append(test.connected(int(set[0]),int(set[1])))
        if printme:
            print tuple
            print test
    return res


def do_unions(test,string, printme=False):
    '''Take input in format of "1-4 2-3 1-4" and do unions'''
    return iterate_string(test,string,printme,"union")


def do_connecteds(test,string,printme=False):
    '''Take input in format of "1-4 2-3 1-4" and return a list of True/False '''
    return iterate_string(test,string,printme,"connected")


def test_alg(tree, unions):
    start_union = time.time()
    input(tree,unions)
    stop_union = time.time()
    start_connected = time.time()
    input(tree,unions)
    print test.connected(1,2)
    print test.connected(4,9)
    stop_connected = time.time()
    val1 = stop_union - start_union
    val2 = stop_connected - start_connected
    print "Took %d seconds for all unions" % val1
    print "Took %d seconds for all connection tests" % val1


u1 = "9-0 3-5 1-8 9-1 5-7 1-3"
u2 = "6-5 9-6 5-1 2-7 3-4 0-9 4-7 0-3 6-8"
t1 = "2 9 1 1 1 2 1 1 1 9"
t2 = "6 8 6 6 6 8 6 6 6 5"
t3 = "5 5 9 5 2 4 9 5 5 5"
t4 = "2 4 5 5 3 5 3 4 0 4"
t5 = "0 1 1 3 4 1 6 7 9 9"

test = Array(10)
test2 = WeightedTree(10)
test3 = ValidateWeightedTree(t1)
test4 = ValidateWeightedTree(t2)
test5 = ValidateWeightedTree(t3)
test6 = ValidateWeightedTree(t4)
test7 = ValidateWeightedTree(t5)

do_unions(test,u1)
do_unions(test2,u2)

print test2

print "\n".join(['solution', str(test), str(test2)])

print "\n".join(['validations', str(test3), str(test4), \
    str(test5), str(test6), str(test7)])

exit()
