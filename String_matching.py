#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :19-5-27 下午12:44
# @Author  : liuyaanng
# @FileName: String_matching.py
# @Software: PyCharm Community Edition

#problem:给定一个长度为 M 的文本和一个长度为 N 的模式串，在文本中找到一个和该模式相符的子字符串，并返回该字字符串在文本中的位置。


class String_matching(object):
	# 暴力搜索
	def force_search(self, M, N):
		if M is None or N is None:
			return -1
		M_l = list(M)
		N_l = list(N)
		for i in range(len(M) - len(N)+1):
			for j in range(len(N)):
				if M_l[i+j] != N_l[j]:
					break
			else:
				return i
		return -1



M = 'abcdfed'
N = 'e'

p = String_matching.force_search(String_matching,M,N)
print(p)

