#8-dars.Ro'yhat bilan ishlash
# AMALIYOT

#- O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar=["O'zbekiston","Qozog'iston", "Tojikistan", "Qirg'iziston","Turkmanistan","Afg'onistan"]
print(davlatlar)

#- Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

#- `sorted()` funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))

#- `sorted()` yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar,reverse=True))

#- Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)

#- `reverse()` metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

#- `sort()` metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)



#- 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar=list(range(120,1200,2))
#- Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
yigindi=sum(sonlar)
print(yigindi)
#- Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
max_min_ayirmasi=max(sonlar)-min(sonlar)
print(max_min_ayirmasi)
#- Ro'yxatdagi elementlar sonini hisoblang
elenentlar_soni=len(sonlar)
print(elenentlar_soni)
#- Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(sonlar[:20], sonlar[260:280],sonlar[-20:])



#- `taomlar` degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar=['Ovsyanka','Shorva','Tuxum','Sut','Non']
#- `nonushta` degan yangi ro'yxatga `taomlar`dan nusxa oling
nonushta=taomlar[:]
#- Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('Shorva')
nonushta.append('qaymoq')
nonushta.append('asal')
#- Ikkala ro'yxatni ham (`taomlar` va `nonushta`) konsolga chiqaring
print(taomlar)
print(nonushta)
#- Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va `nonushta[0] = "qaymoq va non"` deb qiymat berib ko'ring.
nonushta=tuple()
print(type(nonushta))









