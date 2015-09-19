#!/usr/bin/env python
'''Python implementation of Union-Find for Coursera Algorithm class questions'''

import math
import time

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
		
	def union(self,a,b):
		val = self.tree[a]
		val2 = self.tree[b]
		self.tree[b] = val2
		for i in range(0,self.size):
			if self.tree[i] == val or self.tree[i] == val2:
				self.tree[i] = val2

	def connected(self,a,b):
		return self.tree[a] == self.tree[b]

	def printme(self):
		print "size:%d" %(self.size)
		print "array:" + ' '.join(str(i) for i in self.tree.values())


class Tree(Array):

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

	def printme(self):
		print "size:%d" %(self.size)
		print "tree:" + ' '.join(str(i) for i in self.tree.values())
		print "tree_size:" + ' '.join(str(i) for i in self.tree_size.values())


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
			self.printme()
			return True
		else:
			return False

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
			test.printme()
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

test2.printme()

print 'solution'
test.printme()
test2.printme()

print 'validations'
print test3.validate()
print test4.validate()
print test5.validate()
print test6.validate()
print test7.validate()

exit()
