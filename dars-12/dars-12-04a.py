# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:05:54 2024

@author: eljan
"""

"""
27/11/2020
Dasturlash asoslari
#12-dars: Xatolar
Muallif: Anvar Narzullaev
Web sahifa: https://python.sariq.dev
"""

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat=[]

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: ").lower())

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")            