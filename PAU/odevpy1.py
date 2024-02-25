"""
Bir 100 metre koşucusu farklı günlerde yaptığı sürelerin kaydını tutmaktadır.
Kullanıcıdan süre sayısını ve süreleri alan; en küçük, en büyük ve ortalama 
süreleri ekrana yazdıran Python kodunu yazınız.
Örnek girdi ve çıktı aşağıda verilmiştir:
Girdi:
5
9.97
10.53
11.23
11.28
10.18
Çıktı:
9.97
11.28
10.638

Not: Lütfen kullanıcıdan değer alırken ekrana herhangi bir şey yazdırmayın,
ekrana herhangi bir şey yazdırmak çıktıyı bozacağı için hesaplamanız doğru
olsa bile sistem doğru kabul etmeyecektir. Kullanıcıdan bir değer alırken,
giriş fonksiyonunu input('') biçiminde kullanmalısınız.

Kodlarınızı aşağıya yazabilirsiniz.
"""
""" time = int(input(''))
time_records = []
for i in range(time):
    time_records.append(float(input('')))
print(min(time_records))
print(max(time_records))
print(sum(time_records)/time) """

sure = int(input(''))
enb = None
enk = None
sureToplam = 0

for i in range(sure):
    deger = float(input(''))
    sureToplam += deger
    if enk == None or enk > deger:
        enk = deger
    if enb == None or enb < deger:
        enb = deger

print(enk)
print(enb)
print(sureToplam/sure)