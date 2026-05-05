while loop bilan ishlash — bu xuddi bir ishni bajarish uchun shart qo'yib, o'sha shart bajarilmaguncha to'xtamaslikka o'xshaydi. Ro'yxatlarni while orqali aylanish uchun bizga "sanoqchi" (counter) kerak bo'ladi.

1. Oddiy tushuntirish

for loop ro'yxatni o'zi avtomatik boshidan oxirigacha aylanib chiqsa, while loopda biz hammasini qo'lda boshqarishimiz kerak:

Qayerdan boshlashni aytamiz (masalan, 0-indeksdan).

Qachon to'xtashni aytamiz (ro'yxat tugaganda).

Har bir qadamda bitta oldinga yurishni aytamiz (indexni oshirish).

2. Hayotiy o'xshatish

Tasavvur qiling, siz zinadan ko'tarilyapsiz.

Siz 0-pog'onada turibsiz (i = 0).

Sizga shart qo'yilgan: "Toki tepaga yetmaguningcha, qadam bosishda davom et" (while i < pogonalar_soni).

Har safar bir qadam bosganingizda, o'zingizga "bitta qadam bosdim" deb hisoblab borasiz (i += 1).

Agar sanashni unutsangiz, bir joyda depsinib turaverasiz (Infinite loop — cheksiz takrorlanish).

list comprehention.
sonlar = [1, 2, 3, 4]

kvadratlar = [x * x for x in sonlar]

print(kvadratlar) # [1, 4, 9, 16]
4. Qanday o'qiladi?
Sintaksisni tushunish uchun uni o'ngdan chapga qarab o'qing:

for x in sonlar — "sonlar ichidagi har bir x uchun..."
x * x — "...uni o'ziga ko'paytir..."
[...] — "...va natijani yangi ro'yxatga yig'."


5. Murakkabroq: Shart (if) qo'shish

List comprehension ichida hatto if (shart) ham ishlatsa bo'ladi. Masalan, faqat juft sonlarni ajratib olmoqchimiz:

Python
sonlar = [1, 2, 3, 4, 5, 6]
juft_sonlar = [x for x in sonlar if x % 2 == 0]

print(juft_sonlar) # [2, 4, 6]


Python-da Set Methods (to'plam metodlari) — bu to'plamlar ustida har xil amallarni bajarish uchun 
ishlatiladigan maxsus buyruqlar. Setlar tartibsiz va takrorlanmas bo'lgani uchun, ularning 
metodlari ham asosan element qo'shish, o'chirish va matematik amallar (birlashma, kesishmalar) ustida ishlaydi.

1. Element qo'shish va o'chirish metodlari

Bu metodlar to'plam tarkibini o'zgartirish uchun ishlatiladi.

add(): To'plamga bitta element qo'shadi. Agar u element allaqachon bo'lsa, hech narsa qo'shmaydi.

update(): To'plamga bir nechta elementlarni (ro'yxat, tuple yoki boshqa set) qo'shadi.

remove(): Ko'rsatilgan elementni o'chiradi. Agar u element topilmasa, xatolik (error) beradi.

discard(): Elementni o'chiradi, lekin u topilmasa xatolik bermaydi. (Xavfsizroq usul).

pop(): To'plamdan tasodifiy (random) bir elementni o'chiradi va o'sha elementni qaytaradi.

clear(): To'plamni butunlay bo'shatadi.

Python
savatcha = {"olma", "banan"}
savatcha.add("anor")      # {"olma", "banan", "anor"}
savatcha.discard("nok")   # Xatolik bermaydi, chunki "nok" yo'q

2. Matematik amallar (To'plamlar o'rtasidagi munosabat)

Setlarning eng kuchli tomoni mana shu metodlarda. Bu xuddi matematika darsidagi Venn diagrammalariga o'xshaydi.

union(): Ikki to'plamni birlashtiradi (ikkala to'plamdagi hamma elementlarni oladi).

intersection(): Faqat ikkala to'plamda ham bor bo'lgan umumiy elementlarni oladi.

difference(): Birinchi to'plamda bor, lekin ikkinchisida yo'q elementlarni oladi.

symmetric_difference(): Ikkala to'plamda ham bor bo'lgan umumiy elementlarni tashlab yuboradi va qolganlarini oladi.