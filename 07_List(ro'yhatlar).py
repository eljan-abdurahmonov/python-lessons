# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 07:48:15 2024

@author: eljan
"""

#7-dars.List(ro'yhat)
"""
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
ismlar = [] # bo'sh ro'yxat

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar[0].title())
print("Ikkinchi meva: ", mevalar[1].upper())

narhlar = [12000, 18000, 10900, 22000]
print(narhlar[2] + narhlar[3])

car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 

narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
print(narhlar)

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
print(mevalar)

cars = [] # bo'sh ro'yxat yaratamiz
cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
print(cars)

cars = ['Lacetti', 'Nexia 3', 'Cobalt']
cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
print(cars)

cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
print(cars)

## Elementni o'chirish
#Ro'yxatdan biror elementni olib tashlash uchun uning indeksini yoki qiymatini bilishimiz lozim.

#Inedks yordamida olib tashlash uchun `del` operatoridan foydalanamiz:

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
print(mevalar)

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
print(mevalar)

hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
print(hayvonlar)

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)

#>Agar `.pop()` metodida indeks berilmasa, ro'yxatdan o'xirgi qiymat sug'urib olinadi.

"""
#Amaliyot
'''
#1
ismlar=['abror', 'javlon','urol']
print(ismlar[0].title(), 'bugun ishga chiqdingizni?')
print(ismlar[1].title(), 'bizda ingliz tilidan darsimiz bor')
print(ismlar[2].title(), 'bugun ishga chiqdingizni?')

#2
sonlar=[23, -12, 9, -20.35, -12, 35.5]
sonlar[1]=-11
sonlar.append(10)
sonlar.insert(1, -12)
del sonlar[2]
sonlar.remove(-12)
manfiy=sonlar.pop(2)

print(sonlar[0]+sonlar[-1],'birinchi va oxirgi qiymatlar yigindisi')
print(sonlar[0], 'birinchi qiymat')
print(sonlar[-1],'oxirgi qiymat')
print(sonlar)
print(manfiy, '.pop() metodi orqali listdan sugurib olingan qiymat')

#3
t_shaxslar=["Buxoriy","Farg'oniy", "Ibn Sino"]
z_shaxslar=["Ilon Maks","Robert Kiyosaki","Jeki Chan"]
t_shaxs=t_shaxslar.pop(1)
z_shaxs=z_shaxslar.pop(0)
print("Men tarixiy shaxslardan", t_shaxs,"bilan, zamonaviy shaxslardan esa",z_shaxs,"bilan suhbat qilishni istar edim.")
#4
friends=[]
friends.append('Abror')
friends.append('Azamat')
friends.append('Odilxoja')
friends.append('Islombek')
friends.append('Ibrohim')
friends.remove('Islombek')
print(friends)
friends.append('Nodir')
friends.insert(0, 'Elbek')
friends.insert(3, 'Zokir')
print(friends)
'''
#5
friends=[]
friends.append('Abror')
friends.append('Azamat')
friends.append('Odilxoja')
friends.append('Islombek')
friends.append('Ibrohim')
friends.remove('Islombek')
friends.append('Nodir')
friends.insert(0, 'Elbek')
friends.insert(3, 'Zokir')

mehmonlar=[]
mehmon1=friends.pop(0)
mehmon2=friends.pop(3)
mehmon3=friends.pop(-1)

mehmonlar.append(mehmon1)
mehmonlar.append(mehmon2)
mehmonlar.append(mehmon3)
mehmonlar.append(friends.pop(2))
print(mehmonlar)






