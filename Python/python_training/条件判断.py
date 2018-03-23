#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
a=input('Please input your hight:')
hight=float(a)
if hight<20 or hight >230:
	print('your input Error!\nPlease input again!')
b=input('Please input your weigh:')
weigh=float(b)
result=weigh/hight/hight
if result <18.5:
	print('Too Light')
elif result <25:
	print('Normal')
elif result <28:
	print('Fat')
else:   
	print('Too Fat')
print('Test End!')