#!/usr/bin/env python3
# -*- coding:utf-8 -*-
a=float(input('please input a number:'))
b=float(input('please input another number:'))
def ABC(a,b):
	c=(a**2+b**2)**0.5
	return c
D=ABC(a,b)
print('The triangle third side\'s length is %.2f' %D)
