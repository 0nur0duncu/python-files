"""
Kullanıcıdan alınan, aralarında virgül bulunan elemanlardan sadece pozitif
tamsayıları toplayan ve toplamı ekrana yazdıran bir Python programı yazınız.
Programın örnek çalışması aşağıda verilmiştir:
Girdi:
15,3.14,False,-22,10,dasds,1,-123
Çıktı:
26
"""
intTotal = 0
strInput = input('')
text = ''
for i in strInput.split(','):
    try:
        if '.' not in i and int(i) > 0:
            intTotal += int(i)
    except:
        pass

print(intTotal)