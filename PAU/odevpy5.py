"""
Parametre olarak verilen iki listedeki ortak elemanları tekrarsız ve sıralı
olarak geri döndüren ortak fonksiyonunu yazınız.
Fonksiyonun örnek çalışması aşağıda verilmiştir:
>>> ortak([4, 2, 1, 2, 2, 1, 2, 4, 5, 1], [2, 4, 1, 3, 5, 2, 1, 3, 1, 1])
[1, 2, 4, 5]
"""

def ortak(liste1, liste2):
    return sorted(list(set([i for i in liste1 if i in liste2])))

print(ortak([4, 2, 1, 2, 2, 1, 2, 4, 5, 1], [2, 4, 1, 3, 5, 2, 1, 3, 1, 1]))
