# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 07:04:43 2024

@author: eljan
"""

# 5 - dars. String
'''
matn = "Men yangi 📱 oldim"
print(matn)

ism = 'Ahmad'
print("Mening ismim " + ism)

ism = 'Ahad'
familiya = 'Qayum'
print(ism + familiya)

ism = 'Ahad'
familiya = 'Qayum'
print(ism + ' ' + familiya) # ikki o'zgaruvchi orasiga bo'sh joy qo'shamiz

ism = "Ahad"
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

ism = "James"
familiya = 'Bond'
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")
'''
#maxsus belgilar
'''
print('Hello World!')
print('Hello \tWorld!')
print('Hello \nWorld!')
'''
#string metodlari
'''
ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())
print(ism_sharif.lower())
print(ism_sharif.title())
print(ism_sharif.capitalize())
print('james bond'.upper())

meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")
print("Men " + meva + " yaxshi ko'raman")
'''
#input
'''
ism = input("Ismingiz nima?")
print("Assalom alaykum, " + ism)

ism = input("Ismingiz nima?\n>>>") # Foydalanuvchi ismini yangi qatordan kiritadi
print("Assalom alaykum, " + ism.title())
'''
#Amaliyot
'''
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
'''
'''
kocha=input("Ko'changiz nomi: ")
mahalla=input("Mahallangiz nomi: ")
tuman=input("Tumaningiz nomi: ")
viloyat=input("Viloyatingiz nomi: ")
#print(f"{kocha.title()} ko'chasi, {mahalla.title()} mahallasi, {tuman.title()} tumani, {viloyat.title()} viloyati")
print(f"{kocha.title()} ko'chasi, \n{mahalla.title()} mahallasi, \n{tuman.title()} tumani, \n{viloyat.title()} viloyati")
'''
kocha=input("Ko'changiz nomi: ")
mahalla=input("Mahallangiz nomi: ")
tuman=input("Tumaningiz nomi: ")
viloyat=input("Viloyatingiz nomi: ")
manzil=f"{kocha.capitalize()} ko'chasi, {mahalla.capitalize()} mahallasi, {tuman.capitalize()} tumani, {viloyat.capitalize()} viloyati"
print(manzil)














