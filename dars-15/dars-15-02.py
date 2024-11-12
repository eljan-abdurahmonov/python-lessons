# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:01:31 2024

@author: eljan
"""

#Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
dav_poy={
    "O\'zbekiston":"Toshkent",
    "Rossiya":"Moskva",
    "Xitoy":"Pekin",
    "Yapanoiya":"Tokyo",
    "Angliya":"London",
    "America":"Vashington"
    }
print("Dunyo davlatlari:")
for key in sorted(dav_poy.keys()):
    print(key)
print("Davlatlarning poytaxtlari:")   
for value in sorted(dav_poy.values()):
    print(value)