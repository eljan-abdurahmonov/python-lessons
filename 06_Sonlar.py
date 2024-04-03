# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 07:39:07 2024

@author: eljan
"""

#06-dars. Sonlar
# INTEGERS — BUTUN SONLAR
#Butun sonlarni ham o'zgaruvchida saqlash, ularning ustida qo'shish (`+`), ayirish (`-`), ko'paytirish(`*`), bo'lish (`/`) kabi [arifmetik amalarni](https://python.sariq.dev/ilk-qadamlar/03-print#arifmetik-amallar) bajarish mumkin:

# FLOATS — O'NLIK SONLAR
#Pythonda o'nlik sonlar **floating point numbers** yoki qisqa qilib **floats** deyiladi. "Floating point numbers" atamasini o'zbek tiliga "suzuvchi nuqtali sonlar" deb tarjima qilish mumkin. Ingliz tilida o'nlik sonlarni yozishda vergul (`,`) emas nuqta (`.`) belgisi ishlatiladi, va bu nuqta sonning katta kichikligiga qarab joyi o'zgargani uchun "floating" (suzuvchi) deyiladi.   
  
#Amaliyot
'''
son=int(input("istalgan sonni kiriting:\n>>>"))
print(son," ning kvadrati ", son**2, " ga teng")
print(son, " ning kubi ", son**3, " ga teng")    
  
yosh=int(input("Yoshingiz nechida?\n>>>"))
t_yil=2024-yosh
print("Siz",t_yil,"da tug'ilgansiz")
'''
a=float(input("Birinchi sonni kiriting: "))  
b=float(input("Ikkinchi sonni kiriting: "))    
print(a,"+",b,"=",a+b)   
print(a,"-",b,"=",a-b)  
print(a,"*",b,"=",a*b) 
print(a,"/",b,"=",a/b)
# Foydalanuvchidan ikki son kiritshni so'rab, 
# kiritilgan sonlarning yig'indisi, ayirmasi, 
# ko'paytmasi va bo'linmasini chiqaruvchi dastur
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
print(f"{a}+{b}=", a+b)
print(f"{a}-{b}=", a-b)
print(f"{a}x{b}=", a*b)
print(f"{a}/{b}=", a/b)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    