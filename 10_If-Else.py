# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 06:36:16 2024

@author: eljan
"""

#10-dars. IF-ELSE

#avtolar = ['audi','bmw','volvo','kia','hyundai']
#for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#    else: # aks holda ... 
#        print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.
# QIYMATLARNING TENG EMASLIGINI TEKSHIRISH
#Agar ikki qiymatning teng emasligini tekshirish talab qilinsa, `!=` operatoridan foydalanilamiz. 

#ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
#if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
#    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
#else:
#    print("Salom, Ali")

# SONLARNI SOLISHTIRISH

#Sonlarni solishtirishda yuqoridagi teng (`==`) va teng emas (`!=`) shartlariga qo'shimcha ravishda quyidagi mantiqiy shartlar ham qo'shiladi:

#- Kichik: `a<b`
#- Kichik yoki teng: `a<=b`
#- Katta: `a>b`
#- Katta yoki teng: `a>=b`

#javob = float(input("12x6 nechiga teng?>>>"))
#if javob!=72:
#    print("Javob xato!")

#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
#    print('Xush kelibsiz!')
#else: # ask holda
#    print('Kirish mumkin emas!')

#login = input("Yangi login tanlang:")
#if len(login)<=5: # login uzunligini tekshiramiz
#    print("Login 5 harfdan ko'proq bo'lishi shart!")

#yil = int(input("Tug'ilgan yilingizni kiriting:"))
#if 2020-yil<18: # foydalanuvchining yoshini hisoblaymiz
#    print(f"Yoshingiz {2020-yil}da ekan.")
#    print("Kirish mumkin emas!")
#else:
#    print("Xush kelibsiz!")

# BIR QATOR if/else
#Qisqa kodlar uchun shart va uning badanini 1 qatorga jamlab yozishimiz ham mumkin:

#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

#x, y = 25, 50 # x=25 va y=50
#print("x>y") if x>y else print("x<y")

# AMALIYOT
"""
- Yangi `cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']` degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. `GM` uchun ikkala harfni katta qiling.
- Yuqoridagi mashqni teng emas (`!=`) operatori yordamida bajaring. 
- Foydalanuvchi login ismini so'rang. Agar login `admin` bo'lsa, `"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?"` xabarini konsolga chiqaring. Aks holda, `"Xush kelibsiz, {foydalanuvchi_ismi}!"`  matnini konsolga chiqaring.
- Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, `"Sonlar teng"` ekan degan yozuvni konsolga chiqaring.
- Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga `"Manfiy son"`, agar musbat bo'lsa `"Musbat son"` degan xabarni chiqaring. 
- Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, `"Musbat son kiriting"` degan xabarni chiqaring. 

#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting:"))
if x==y: print(f"Sonlar teng: {x}={y}")

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
son = float(input("Istalgan son kiriting:"))
print("Son manfiy") if son<0 else print("Son musbat")

#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
son = float(input('Istalgan son kiriting: '))
 print(son**(1/2)) if son>0 else print('Musbat son kiriting')

"""
#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car=='gm':
#        print(car.upper())
#    else:
#        print(car.title())
                
#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car!='gm':
#        print(car.title())
#    else:
#        print(car.upper())

#login_ism=input('Login ismingizni nima?\n>>>')
#if login_ism.lower()=='admin':
#    print('Xush kelibsiz , Admin!')
#else:
#    print(f"Xush kelibsiz, {login_ism.title()}!")

#son1=int(input('Birinchi sonni kiriting:'))
#son2=int(input('Ikkinchi sonni kiriting:'))
#if son1==son2:
#    print("Sonlar teng!")
#else:
#    print('Sonlar teng emas')

#son=float(input("Istalgan sonni kiriting: "))
#if son<0:
#    print('Manfiy son!')
#else:
#    print("Musbat son!")

son=float(input("Biror sonni kiriting: "))
if son>=0:
    print(son**(1/2))
else:
    print("Musbat sonni kiriting!")    