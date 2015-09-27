#!/usr/bin/env python
'''Python implementation of Union-Find for Coursera Algorithm class questions'''

import math

__author__ = "Adam Tetelman"


class Array:

    def __init__(self,num):
        self.tree = {}
        self.tree_size = {}
        self.tree_height = {}
        if isinstance(num, int):
            self.size = num
            for i in range(0,self.size):
                self.tree[i] = i
                self.tree_size[i] = 1
        else:
            tree = num.split(" ")
            self.size = len(tree)
            for i in range(self.size):
                self.tree[i] = int(tree[i])
                self.tree_size[i] = 1 #TODO - Implement size calculations in Array
                self.tree_height[i] = 1 #TODO - Implement height calculations

    def __str__(self):
        return "\n".join(["size:%d" %(self.size), \
            "array:" + ' '.join(str(i) for i in self.tree.values())])
        
    def union(self,a,b):
        val = self.tree[a]
        val2 = self.tree[b]
        self.tree[b] = val2
        for i in range(0,self.size):
            if self.tree[i] == val or self.tree[i] == val2:
                self.tree[i] = val2

    def connected(self,a,b):
        return self.tree[a] == self.tree[b]


class Tree(Array):

    def __str__(self):
        return "\n".join(["size:%d" %(self.size), \
            "array:" + ' '.join(str(i) for i in self.tree.values()), \
            "tree_size:" + ' '.join(str(i) for i in self.tree_size.values())])

    def get_root(self,a,ret_depth=False):
        val = self.tree[a]
        depth = 1
        while a != val:
            depth += 1
            if depth > self.size:
                return depth
            a = val
            val = self.tree[val]
        if ret_depth:
            return depth
        return val
    
    def union(self,a,b):
        a_root = self.get_root(a)
        b_root = self.get_root(b)
        self.tree[a_root] = b_root
        self.tree_size[b_root] = self.tree_size[a_root]
    
    def connected(self,a,b):
        return self.get_root(a) == self.get_root(b)

    def recalculate_size(self):
        for i in range(self.size):
            self.tree_size[i] = 1
        for i in range(self.size):
            val = i
            while val != self.tree[val]:
                val = self.tree[val]
                self.tree_size[val] += 1


class WeightedTree(Tree):

    def union(self,a,b):
        a_root = self.get_root(a)
        b_root = self.get_root(b)
        if a_root == b_root:
            return
        elif self.tree_size[a_root] < self.tree_size[b_root]:
            self.tree[a_root] = b_root
            self.tree_size[b_root] += self.tree_size[a_root]
        else:
            self.tree[b_root] = a_root
            self.tree_size[a_root] += self.tree_size[b_root]


class CompressedWeightedTree(Tree):

    def get_root(self,a,ret_depth=False):
        val = self.tree[a]
        depth = 1
        while a != val:
            depth += 1
            if depth > self.size:
                return depth
            self.tree[a] = self.tree[val]
            self.tree_size[val] -= self.tree_size[a]
            self.tree_size[self.tree[val]] += self.tree_size[a]
            a = val
            val = self.tree[val]
        if ret_depth:
            return depth
        return val


class ValidateWeightedTree(WeightedTree):
    '''Used to valide pre-created possibly invalid WeightedTrees'''

    def test_loops(self):
        for i in range(self.size):
            if self.get_root(i) > self.size:
                print "ERROR: Loop detected in %d" %i
                return False        
        return True
            
    def test_parent_size(self):
        self.recalculate_size()
        for i in range(self.size):
            if self.tree_size[self.tree[i]] <  2 * self.tree_size[i] and i != self.get_root(i):
                print "ERROR: Parent/Child size discrepancy found between %d (%d) and %d (%d)" %(
                        self.tree[i], self.tree_size[self.tree[i]], i,self.tree_size[i])
                return False
        return True

    def test_forest_size(self):
        max = math.log(self.size)
        for i in range(self.size):
            if self.tree_height[i] > max:
                print "ERROR: Tree height in %d (%d) larger than max (%d)" %(i,self.tree_height[i],max)
                return False
        return True #TODO - implement height tracking for this to work

    def validate(self):
        if self.test_loops() and self.test_parent_size() and self.test_forest_size():
            print self
            return True
        else:
            return False
