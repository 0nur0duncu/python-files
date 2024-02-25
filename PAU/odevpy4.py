"""
Kullanıcıdan alınan iki kelimede bulunan karakterlerin(harflerin) her iki
kelimede bulunma sayılarını hesaplayan ve ilgili harfin kelimelerin bir 
tanesindeki bulunma sayısı 0 ise bulunma sayılarını toplayan aksi halde
bu sayıları çarpan ve sonucu ekrana yazdıran kodu yazınız. Aşağıda örnek
hesaplamalar verilmiştir:

Örnek 1:
Kelime 1: merhaba
Kelime 2: manyetik
Harfler(alfabetik sırada): ['a','b','e','h','i','k','m','n','r','t','y']

                  abehikmnrty
merhaba sayılar:  21110010100
manyetik sayılar: 10101111011
sonuç(çıktı) :    21111111111

Örnek 2:
Kelime 1: werewolves
Kelime 2: oversee
Harfler(alfabetik sırada): ['e', 'l', 'o', 'r', 's', 'v', 'w']

                    elorsvw
werewolves sayılar: 3111112
oversee sayılar :   3011110
sonuç(çıktı):       9111112

"""

f_word = input()
s_word = input()
chars = []

for i in (f_word+s_word):
    if i not in chars:
        chars.append(i)

chars = sorted(chars)
count_f_word = ""
count_s_word = ""

for j in chars:
    count_f_word += str(f_word.count(j))
    count_s_word += str(s_word.count(j))

new_count = ""
for k in range(len(chars)):
    if count_f_word[k] == "0" or count_s_word[k] == "0":
        new_count += str(int(count_s_word[k]) + int(count_f_word[k]))
    else:
        new_count += str(int(count_s_word[k]) * int(count_f_word[k]))

print(new_count)