# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 07:18:14 2024

@author: eljan
"""
#9-dars.For takrorlash operatori
# AMALIYOT
#1
ismlar=['Anvar','Ibrohim','Shahriyor','Nurmuhammad','Elbek']
for ism in ismlar:
    print(f"{ism}, bugun universiterga borasizmi?")
#2
print(f"Kod {len(ismlar)} marta takrorlandi.")
#3
toq_sonlar=list(range(11,100,2))
for toq_son in toq_sonlar:
    print(f"{toq_son} ning kubi {toq_son**3} ga teng!")
#4
kinolar=[]
print('5 ta eng sevimli kinolaringiz nomi nima?')
for n in range(5):
    kinolar.append(input(f"{n+1}-kinoning nomi:"))
print(kinolar)
#5
uchrashuv_soni=int(input("Bugun nechta odam bilan uchrachdingiz?\n>>"))
odam_ismlari=[]
for n in range(uchrashuv_soni):
    odam_ismlari.append(input(f"{n+1}- uchrashgan odamingiz ismi:"))
print(odam_ismlari)
#- Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
#- Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
#- 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
#- Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
#- Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
"""
# for QANDAY ISHLAYDI
#01
Keling yana bir misol ko'raylik.
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi")

#02
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(mehmon)
    
print(mehmonlar)

# for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH

#01
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
    
#02
sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
for son in sonlar:  # sonlar dagi har bir son uchun
    sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz

print(sonlar)
print(sonlar_kvadrati)
#for and input
dostlar = [] # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)

"""