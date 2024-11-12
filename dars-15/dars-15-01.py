# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:54:49 2024

@author: eljan
"""

#Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
pyton_dict={'boolean':'Mantiqiy qiymat',
            'strig':'Mantli ma\'lumot turi',
            'integer':'Butun son',
            'float':"O'nlik son",
            'for':'Tsikl, takrorlash operatori',
            'if':"Shart operatori",
            'print':'Ekranga natijani chiqarish',
            'list':'Ro\'yhat',
            'tuple':'O\'zgarmas qiymat',
            'set':'Tartibsiz va bir xil qiymatsiz ma\'lumot turi'
            }
for key, value in sorted(pyton_dict.items()):
    print(f"{key.title()}-{value}.")
