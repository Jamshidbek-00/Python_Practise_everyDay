## day04
Operator ustuvorligi  yani qaysi biri birinchi bajarilishi kerakligi jadvali
Python-da bir nechta operator birgalikda kelganda, ularning qaysi 
biri birinchi bo'lib bajarilishi 
Operator Precedence (Operatorlar ustuvorligi) qoidasiga asoslanadi.
Tartib,Operator,Tavsif

1,(),Qavslar (Eng yuqori ustuvorlik)
2,**,Darajaga ko'tarish
3,"+x, -x, ~x","Unar plyus, minus va bitli NOT"
4,"*, /, //, %","Ko'paytirish, bo'lish, butun bo'lish va qoldiq"
5,"+, -",Qo'shish va ayirish
6,"<<, >>",Bitli surishlar
7,&,Bitli AND
8,^,Bitli XOR
9,|,Bitli OR
10,"==, !=, >, >=, <, <=, is, in",Taqqoslash va a'zolik operatorlari
11,not,Mantiqiy NOT
12,and,Mantiqiy AND
13,or,Mantiqiy OR
14,"=, +=, -=, ...",O'zlashtirish operatorlari (Eng past ustuvorlik)


## Python Lists

* Python'da List (Ro'yxat) — bu bir nechta elementlarni bitta o'zgaruvchida 
saqlashga imkon beruvchi eng ko'p qo'llaniladigan ma'lumotlar turidir.

1. List yaratish va uning xususiyatlari

Ro'yxatlar kvadrat qavslar [] yordamida yaratiladi va elementlar 
vergul bilan ajratiladi.

Tartiblangan (Ordered): Elementlar ma'lum bir tartibda turadi.

O'zgartirsa bo'ladi (Mutable): Ro'yxat yaratilgandan keyin unga 
element qo'shish, o'chirish yoki qiymatini o'zgartirish mumkin.

Dublikatlarga ruxsat beradi: Bir xil qiymatli elementlar bir necha bor 
kelishi mumkin.


mevalar = ["olma", "banan", "olcha", "banan"] 
sonlar = [1, 2, 3, 10.5]
aralash = ["salom", 100, True] # Har xil turdagi ma'lumotlar bo'lishi mumkin


1. Metod,Vazifasi,Misol
2. .append(x),Ro'yxat oxiriga element qo'shadi,"mevalar.append(""uzum"")"
3. ".insert(i, x)",Ko'rsatilgan indeksga element qo'shadi,"mevalar.insert(1, ""nok"")"
4. .remove(x),Ko'rsatilgan qiymatli elementni o'chiradi,"mevalar.remove(""banan"")"
5. .pop(i),Ko'rsatilgan indeksdagi elementni sug'urib oladi,mevalar.pop(0)
6. .sort(),Ro'yxatni tartiblaydi,sonlar.sort()
7. len(),Ro'yxat uzunligini qaytaradi,len(mevalar)