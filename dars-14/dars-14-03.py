# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:25:51 2024

@author: eljan
"""

#Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
dictionary={
    'print':'chop etish',
    'integer':'butun son',
    'float':'o\'nli son',
    'string':'mantli o\'zgaruvchi turi',
    'del':'o\'chirish funksiyasi',
    'if':'agar',
    'else':'ask holda',
    'for':'uchun',
    'list':'ro\'yhat',
    'tuple':'o\'zgarmas ro\'yhat',
    'dictionary':'lug\'at'
    }

#Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

key_word=input("Kalit so'z kiriting: ").lower()
izohi=dictionary.get(key_word, "Bunday so'z mavjud emas!")
print(izohi)























