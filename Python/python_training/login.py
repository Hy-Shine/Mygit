#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
def account_login():
	password=str(input('Please input your password:'))
	if password == '12345':
		print('Login Success!')
	else:
		print('Password Error!\nPlease try again!')
account_login()