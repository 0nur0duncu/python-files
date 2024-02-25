"""
Öğrenci sayısı, öğrencilerin isimleri ve bir sınavdan aldıkları notlar her biri
bir satır olacak şekilde girdi olarak verilmektedir. Sınavda aynı notu alan
öğrenciler bulunmamaktadır(her not farklı). Verilen girdiye göre en düşük ikinci
notu ve en yüksek ikinci notu alan öğrencilerin adlarını alt alta yazdıran
Python kodunu yazınız.

Programın örnek çalışması aşağıda verilmiştir:
Girdi:
7
Ogrenci 1
3
Ogrenci 2
68
Ogrenci 3
86
Ogrenci 4
87
Ogrenci 5
40
Ogrenci 6
76
Ogrenci 7
31
Çıktı:
Ogrenci 7
Ogrenci 3

Not: Derste listeler henüz anlatılmamıştır fakat listeler kullanılmadan da 
ilgili hesaplama yapılabilir.
"""

""" ogrSayisi = int(input(''))
ogr =[]
notu = []

for i in range(ogrSayisi):
    ogr.append(input(''))
    notu.append(int(input('')))

ogrNot = list(zip(ogr,notu))
sirali = sorted(ogrNot, key=lambda x: x[1])
print(sirali[1][0])
print(sirali[-2][0])
print(sirali[1][0])"""




""" sayi = int(input(''))
enyukseknot = None
endusuknot = None
enyuksekikincinot = None
endusukikincinot = None
enyuksekad = None
endusukad = None
enyuksekikinciad = None
endusukikinciad = None

for i in range(sayi):
    adi = input('')
    notu = int(input(''))
    if enyukseknot == None or enyukseknot < notu:
        enyuksekikincinot = enyukseknot
        enyukseknot = notu
        enyuksekikinciad = enyuksekad
        enyuksekad = adi
    if endusuknot == None or endusuknot > notu:
        endusukikincinot = endusuknot
        endusuknot = notu
        endusukikinciad = endusukad
        endusukad = adi

print(endusukikinciad)
print(enyuksekikinciad)
"""


sayi = int(input(''))

enb = None
enbA = None
enb2N = None
enb2A = None

enk = None
enkA = None
enk2N = None
enk2A = None

for i in range(sayi):
    adi = input('')
    notu = int(input(''))
    if enb == None or notu > enb:
        enb2N = enb
        enb = notu
        enb2A = enbA
        enbA = adi
    if enk == None or notu < enk:
        enk2N = enk
        enk = notu
        enk2A = enkA
        enkA = adi

print(enk2A)
print(enb2A)





""" ogrSayisi = int(input(''))
ogrAdNot = ''
for i in range(ogrSayisi):
    ad = input('')
    notu = input('')
    ogrAdNot += (ad + '=' + notu + ',')

text = ''
ograd = ''
ogrnot = 0
enyukseknot = 0
yuksekikincinot = 0
endusuknot = 100
dusukikincinot = 0
dusukikinciad = ''
yuksekikinciad = ''

for j in ogrAdNot:
    if j == '=':
        ograd = text
        text = ''
        pass
    elif j == ',':
        ogrnot = text
        if int(text) > enyukseknot:
            yuksekikincinot = int(text)
            enyukseknot = int(text)
            
        else:
            yuksekikinciad = ograd

        if int(text) < endusuknot:
            dusukikincinot = int(text)
            endusuknot = int(text)
        
        else:
            dusukikinciad = ograd
        text = ''
        pass
    text += j """






""" numStu = int(input(''))
ogrAd = input('')
enyuksek = endusuk = int(input(''))
enyuksekikinci = 0
endusukikinci = 0
endusukikincikisi = ''
enyuksekikincikisi = ''
for i in range(1,numStu):
    ogrAd = input('')
    stuGrade = int(input(''))
    if stuGrade > enyuksek:
        enyuksekikincikisi = 
        enyuksekikinci = enyuksek
        enyuksek = stuGrade
        
    if stuGrade < endusuk:
        endusukikincikisi = 
        endusukikinci = endusuk
        endusuk = stuGrade

print(endusukikincikisi)
print(enyuksekikincikisi) """

