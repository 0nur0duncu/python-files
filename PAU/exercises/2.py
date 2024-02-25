print('merhaba') # merhaba
print("dünya") # dünya
print('Bana "merhaba" dedi!') # Bana "merhaba" dedi!
print("Bana \"merhaba\" dedi!") # Bana "merhaba" dedi!
print(r"c:\users\pau") # c:\users\pau
print('Çok\nsatırlı\nmetin') # 3 satır içerir
print("""Çok
satırlı
metin""")
print(3*'ab'+'cd') # abababcd yazdırır. * tekrarlar,
print('merhaba ' 'dünya') # yan yana stringler birleştirilir
s='Merhaba dünya!' # s metnini tanımlar
print(s[2]) # r yazar
print(s[3:7]) # haba yazar
print(s[-1])
print(s[5:]) # ba dünya! yazar
print(s[:]) # Merhaba dünya! yazar
s='Türkçe karakter uyuşmazlığı'
print(s.upper()) # TÜRKÇE KARAKTER UYUŞMAZLIĞI
print(s.upper().lower()) # türkçe karakter uyuşmazliği
print(s.startswith('Türkçe')) # True
print(s.replace('karakter', 'harf')) # Türkçe harf uyuşmazlığı
l=s.split(' ') # ['Türkçe', 'karakter', 'uyuşmazlığı']
print('- . -'.join(l)) # Türkçe- . -karakter- . -uyuşmazlığı
print(s.count('a')) # 3
print(len(s)) # 27 (uzunluğu verir)
l = ['kırmızı', 'yeşil', 'mavi', 'sarı']
print(l) # ['kırmızı', 'yeşil', 'mavi', 'sarı']
print(l[0]) # kırmızı
print(l[1:3]) # ['yeşil', 'mavi']
print(len(l)) # 4
l2 = l # yeni liste oluşturulmaz, her ikisi de aynı listeyi gösterir
bos_liste = [] # boş liste oluşturur
bos_liste = list() # boş liste oluşturur
l3 = ['siyah', 'mor']
print(l[2:] + l3) # ['mavi', 'sarı', 'siyah', 'mor']
renkler = ['kırmızı', 'yeşil', 'mavi']
for renk in renkler:
    print(renk)
print('yeşil' in renkler) # True
print('sarı' in renkler) # False
liste = ['Ali', 'Ahmet', 'Mehmet']
liste.append('Burak') # sona Burak eklenir
liste.insert(0, 'Hasan') # başa Hasan eklenir
liste.extend(['Ayse', 'Fatma']) # listenin sonuna Ayse ve Fatma eklenir.
print(liste) # ['Hasan', 'Ali', 'Ahmet', 'Mehmet', 'Burak', 'Ayse', 'Fatma']
print(liste.index('Ahmet')) # 2
liste.remove('Burak')
liste.pop(1) # Ali silinir
print(sorted(liste)) # ['Ahmet', 'Ayse', 'Fatma', 'Hasan', 'Mehmet']
print(liste) # ['Hasan', 'Ahmet', 'Mehmet', 'Ayse', 'Fatma']
liste.sort() # Liste sıralanmış hali ile değişir
cu = (1, 3.14, 'merhaba')
for el in cu: # Tüm elemanları yazar
    print(el)
print(cu[1]) # 3.14
cu[2] = 0 # Hata: tuple değiştirilemez
sozluk ={'a': 'alpha', 'o':'omega', 'g':'gamma'}
print(sozluk) # {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
sozluk=dict()
sozluk['a']='alpha'
sozluk['o']='omega'
sozluk['g']='gamma'
print(sozluk) # {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
# for döngüsü varsayılan olarak anahtarlarda dolaşır
for anahtar in sozluk:
    print(anahtar + ':' + sozluk[anahtar])
# Aşağıdakiler listeye dönüştürülebilir.
print(sozluk.keys()) # dict_keys(['a', 'o', 'g'])
print(sozluk.values()) # dict_values(['alpha', 'omega', 'gamma'])
# anahtar değer çiftleri üzerinde dolaşma
for anahtar, deger in sozluk.items():
    print(anahtar,deger)
del sozluk['a'] # silmek için kullanılır
