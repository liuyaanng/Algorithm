#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :19-5-28 上午9:21
# @Author  : liuyaanng
# @FileName: test.py
# @Software: PyCharm Community Edition
from useful_algorithm import *

sort = [3,3,3,2,4,5,6,7,34,4,523,4,23,24,23,52,35235,32,5,9]
sorted_b = Bubble_sort(sort)
sorted_i = Insertion_sort(sort)
sorted_s = Select_sort(sort)
print(sorted_b)
print(sorted_i)
print(sorted_s)