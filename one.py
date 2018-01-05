#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
注释
'''

s1 = input('请输入上一次的成绩:')
s2 = input('请输入本次的成绩:')
r = (float(s2)-float(s1))/float(s1)*100
if r > 0:
	print('你的成绩较上次提升了%.2f%%' % r)
else:
	print('你的成绩较上次下降了%.2f%%' % r)
