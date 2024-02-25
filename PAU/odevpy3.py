"""
Bir film puanlama sitesindeki filmlere verilen oy sayısı, filmlerin adları 
ve verilen puanları(1-10) satırlar halinde kullanıcıdan alan ve ortalaması
en iyi ve en kötü filmin adlarını ekrana yazdıran Python programını yazınız.
Programın örnek çalışması aşağıda verilmiştir:

Girdi:
6
The Shawshank Redemption
8
The Dark Knight
5
The Good, the Bad and the Ugly
4
The Shawshank Redemption
9
The Dark Knight
6
The Dark Knight
8
Çıktı:
The Shawshank Redemption
The Good, the Bad and the Ugly

İpucu: Filmlere verilen oyları sözlüklerde saklayarak ortalama puanı sözlüğü
oluşturduktan sonra hesaplayabilirsiniz.
Not: bilmoodle üzerinde verilen oy sayısı 50 ile 70 arasında değişecektir.
"""

""" numberOfMovie = int(input(''))
nameScore = {}

for i in range(numberOfMovie):
    movieName = input('')
    movieScore = int(input(''))
    nameScore[movieName] = movieScore

maxName = None
maxScore = None
minName = None
minScore = None

for key,value in nameScore.items():
    if maxScore == None or value > maxScore :
        maxScore = value
        maxName = key
        continue
    
    if minScore == None or value < minScore:
        minScore = value
        minName = key
    

print(maxName)
print(minName) """



""" numberOfMovie = int(input(''))
nameScore = {}

maxName = None
maxScore = None
minName = None
minScore = None

for i in range(numberOfMovie):
    movieName = input('')
    movieScore = int(input(''))
    nameScore[movieName] = movieScore

orderedList = sorted(nameScore.items(), key=lambda x: x[0])
orderedList = sorted(orderedList, key=lambda x: x[1])
print(orderedList[len(orderedList)-1][0])
print(orderedList[0][0]) """




""" numberOfMovie = int(input(''))

maxName = None
maxScore = None
minName = None
minScore = None

for i in range(numberOfMovie):
    movieName = input('')
    movieScore = int(input(''))
    if maxScore == None or movieScore >= maxScore:
        maxScore = movieScore
        maxName = movieName
        continue
    if minScore == None or movieScore <= minScore:
        minScore = movieScore
        minName = movieName
        continue

print(maxName)
print(minName) """

numberOfMovie = int(input(''))
movieNameList = []
movieScoreList = []
new_nameScore = {}

for i in range(numberOfMovie):
    movieName = input('')
    movieNameList.append(movieName)

    movieScore = int(input(''))
    movieScoreList.append(movieScore)
    
nameScoreList = list(zip(movieNameList,movieScoreList))

for key in set(movieNameList):
    itemList = [value for key2, value in nameScoreList if key == key2]
    new_nameScore[key] = sum(itemList) / len(itemList)

orderedList = sorted(new_nameScore.items(), key=lambda x: x[1])
print(orderedList[len(orderedList)-1][0])
print(orderedList[0][0])

""" maxName = None
maxScore = 1
minName = None
minScore = 10

for key,value in nameScore.items():

    if movieScore > maxScore:
        maxScore = movieScore
        maxName = movieName

    if movieScore < minScore:
        minScore = movieScore
        minName = movieName

print(maxName)
print(minName) """