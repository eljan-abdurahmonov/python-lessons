# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:33:52 2024

@author: eljan
"""

#Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
taom_narx={
    'sho\'rva':25000,
    'osh':20000,
    'shashlik':10000,
    'somsa':6000,
    'lag\'mon':22000,
    'beshbarmoq':80000,
    'beshteks': 24000,
    'tort':35000,
    'salad':15000,
    'non':5000
    }
buyurtmalar=[]
print("3ta taomga buyurtma bering")
for n in list(range(3)):
    buyurtmalar.append(input(f"{n+1} - taom: ").lower())

for buyurtma in buyurtmalar:
    if buyurtma in taom_narx.keys():
        print(f"{buyurtma.title()} {taom_narx[buyurtma]} so'm.")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q!")













