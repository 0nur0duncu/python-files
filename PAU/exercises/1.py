import random as rnd
rnd.seed(42)

liste = list()
for i in range(3):
    liste.append(rnd.randint(20,40))

for i in liste:
    print(int(i),end= " ")
    count = 1
    while i != 1:
        if i % 2 == 0:
            i = i/2
            print(int(i),end=" ")
            count += 1
        else:
            i = 3 * i + 1
            print(int(i) , end= " ")
            count +=1
    print()
    print(count)


for i in liste:
    total = 0
    for j in range(1,i):
        if i % j == 0:
            total+= j
    if total == i:
        print("evet")
    else:
        print("hayir")
