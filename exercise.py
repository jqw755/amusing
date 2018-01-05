#!/usr/bin/env python3

h = input('身高')
w = input('体重')
x = float(w)/float(h)**2
if x<18.5:
	print('过轻')
elif 18.5<x<25:
	print('正常')
else:
	print('过重')