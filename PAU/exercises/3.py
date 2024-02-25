kareler1 = []

for i in range(10):
    kareler1.append(i**2)

print(kareler1)

kareler2 = list(map(lambda x:x**2,range(10)))
print(kareler2)

kareler3 = [x**2 for x in range(10)]
print(kareler3)

import random
random.seed(42)

print([a for a in [random.randint(-5,5) for x in range(10)] if a > 0])
print([a for a in [-8, -4, -2, 0, 2, 4, 8] if a>0])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

asal = [p for p in range(2,100) if all(p%y!=0 for y in range(2,p))]
print(asal)

mukemmel = [p for p in range(2,1000) if sum([d for d in range(1,p) if p%d==0])==p]
print(mukemmel)

print([(x, "2'nin katı" if x%2==0 else "2'nin katı değil") for x in range(20)])
t=(x*2 for x in range(10)) # üreteç nesnesi
print(tuple(t)) # tuple üretme, üretildikten sonra kaybolur

t=(x**2 for x in range(10))
print(list(t)) # liste üretme

def fonk(arg1, *args, **kwargs):
    print(arg1)
    for arg in args:
        print(arg)
    for k in kwargs:
        print(k, ':', kwargs[k])

fonk('deneme', '1. parametre', '2.', 3.14, yaz='python', anahtar='AE12FF')

def fonksiyon(a1, a2='merhaba', a3='dünya!'):
    print('{} {} {}'.format(a1, a2, a3))
fonksiyon('Python')
fonksiyon('Python', 'hello', 'world!')
fonksiyon('Python', a3='programlama')

def fib(n): # fonksiyon tanımı
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b
fib(100) # fonksiyon çağrısı

def fonksiyon(sayi): # tanım
    if sayi<1000:
        return True, 'Sayı 1000\'den küçük'
    else:
        return False, 'Sayı 1000\'den büyük'
sonuc, metin = fonksiyon(150) # fonksiyon çağrısı

(lambda n: print(n))(5) #isimsiz fonksiyon oluşturma ve değer gönderme
(lambda x: print('çift' if x%2==0 else 'tek'))(13) # tek yazar
def cift(x):
    return x%2 == 0

print(list(map(cift, range(20)))) # True ve False'lardan oluşan liste
print(list(filter(cift, range(20)))) # 20'den küçük çift sayı listesi

def fonk(f, sayi):# fonksiyona başka fonksiyonu parametre olarak gönderme
    print(f(sayi))

fonk(cift, 17) # False yazar
fonk(lambda n: 'çift' if n%2==0 else 'tek', 20) # çift yazar

""" while True:
    pass #sonsuz döngü

def bos_metod():
    pass #bir iş yapmaz """


""" #while True print('sonsuz döngü') # yazım hatası
y = 0
x = 1 / y # olağan dışı durum
try:
    x=1 / y
except ZeroDivisionError: # sıfıra bölme hatası oluşursa
    print('Sıfıra bölme hatası') """

""" while True:
    try:
        x = int(input('Bir sayı girin: '))
        break
    except (ValueError, KeyboardInterrupt): #birden fazla hata algılama
        print('Geçerli bir sayı girmediniz')
    except: # diğer tüm hatalar
        print('Beklenmedik hata')
        raise """


random.seed(41)

def isPrime(x):
    return True if all(x % y !=0 for y in range(2,x)) else False

liste = [random.randint(13,91) for x in range(10)]
print(list(map(isPrime,liste)))
print(list(filter(isPrime,liste)))
