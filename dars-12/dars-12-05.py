# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:14:13 2024

@author: eljan
"""

"""
27/11/2020
Dasturlash asoslari
#12-dars: Xatolar
Muallif: Anvar Narzullaev
Web sahifa: https://python.sariq.dev
"""

users = ['alisher1983','aziza','yasina', 'umar']

login = input("Yangi login tanlang:" ).lower()

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")