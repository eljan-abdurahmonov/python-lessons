# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:14:13 2024

@author: eljan
"""

#Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
dav_poy={
    "o'zbekiston":"Toshkent",
    "rossiya":"Moskva",
    "xitoy":"Pekin",
    "yapaniya":"Tokyo",
    "angliya":"London",
    "aqsh":"Vashington"
    }
davlat=input("Qaysi davlatning poytaxti nomini bilishni istaysiz?: ").lower()

if davlat in dav_poy.keys():
    print(f"{davlat.upper()} davlatining poytaxti {dav_poy[davlat]} shaxri")
else:
    print("Bizda bunday davlat mavjud emas")