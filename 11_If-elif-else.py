# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:56:51 2024

@author: eljan
"""

#11-dars. If-elif-else
#Amaliyot

#1
#son=int(input('Juft sonni kiriting:'))
#if son%2:
#    print('Bu juft son emas!')
#else:
#    print("Rahmat!")
   
#2
#yosh=int(input('Yoshingiz nechida?\n>>>'))
#if yosh<=4 or yosh>=60:
#    narx=0
#elif yosh<=18:
#    narx=10000
#else:
#    narx=20000
#print(f"Sizga kirish {narx} so'm")

#3
#a=int(input("Birinchi sonni kiriting:"))   
#b=int(input("Ikkinchi sonni kiriting:"))     
#if a<b:
#    print(f"{a} kichik {b} dan")
#elif a>b:
#    print(f"{b} kichik {a} dan")    
#elif a==b:
#    print(f"{a} teng {b} ga")    
    
#4 
"""  
mahsulotlar=['sut','guruch','qaymoq','non','sabzi','piyoz','turp','lavlagi','qatiq','yogurt']
savat=[]
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qoshing:"))
bor_mahsulotlar=[]
mavjud_emas=[]
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
  print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")  
"""
#5
"""
foydalanuvchilar=['abror', 'ibrohim','anvar','elbek','sardor']    
login=input("Iltimos o'zingizga yangi login toping:")
if login.lower() in foydalanuvchilar:
    print("Login band, iltimos yangi login kiriting:")
else:
    print(f"Xush kelibsiz {login.title()}!")
"""   
    
#6
son=int(input('Biron butun son kiriting:')) 
for n in range(2,11):
    if not (son%n):    
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi.")
    
    
    
    
    
    
    
    