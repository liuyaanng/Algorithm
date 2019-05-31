#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :19-5-28 上午9:20
# @Author  : liuyaanng
# @FileName: useful_algorithm.py
# @Software: PyCharm Community Edition


def swap(M, N):
		"""
		swap two numbers
		:param M: 
		:param N: 
		:return: N,M 
		"""
		return N,M

def Bubble_sort(sort,order = 'ascending'):

	"""
	sort a list with ascending or descending, default order is ascending 
	:param sort: 
	:return: sorted
	"""
	swaped = False
	for i in range(len(sort)-1):
		for j in range(len(sort)-1-i):
			if sort[j] > sort[j+1]:
				sort[j],sort[j+1] = swap(sort[j],sort[j+1])
				swaped = True

		if not swaped:
			break
	return sort

def Insertion_sort(sort):
	"""
	sort
	:param sort: 
	:return:sorted 
	"""
	count = len(sort)
	for loop_index in range(1,count):
		insertion_index = loop_index
		while insertion_index > 0 and sort[insertion_index - 1] > sort[insertion_index]:
			sort[insertion_index-1],sort[insertion_index] = sort[insertion_index],sort[insertion_index-1]
			insertion_index -= 1
	return sort


def Select_sort(sort):
	"""
	
	:param sort: 
	:return:sorted 
	"""
	count = len(sort)
	for i in range(count):
		least = i
		for j in range(i+1,count):
			if sort[j] < sort[least]:
				least = j
		sort[least],sort[i] = sort[i],sort[least]

	return sort