a = int(input("Bitta son kiriting: "))
x = 0
y = 0
z = 0
h = 0
for i in range(1,a+1):
    if i % 2 == 0:
        x += i
        z += 1
    else:
        y += i
        h += 1
print("juft sonlar yig'indisi:", x)
print("toq sonlar yig'indisi:", y)
print("juft sonlar soni:", z)
print("toq sonlar soni:", h)

# h
# 1-masala: Yugurish masofasi
jami = 0

while True:
    masofa = int(input("Bugun nechta metr yugurdingiz? (0 - tugatish): "))
    if masofa == 0:
        break
    jami += masofa

print("Umumiy yugurilgan masofa:", jami, "metr")

# 2-masala: Do‘kondagi xarid
umumiy = 0

while True:
    narx = int(input("Mahsulot narxini kiriting (manfiy son - tugatish): "))

    if narx < 0:
        break
    if narx == 0:
        continue  # 0 bo‘lsa o‘tkazib yuboriladi

    umumiy += narx

print("Umumiy xarid summasi:", umumiy, "so'm")

# 3-masala: Juft raqamlar sonini sanash
n = int(input("n sonini kiriting: "))

soni = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        soni += 1

print("1 dan", n, "gacha bo‘lgan juft sonlar soni:", soni)


# 4-masala: Avtobusga kirish
umumiy = 0

while True:
    yo_lovchi = int(input("Necha yo‘lovchi kirdi? (-1 - tugatish): "))

    if yo_lovchi == -1:
        break

    umumiy += yo_lovchi

    if umumiy >= 50:
        print("Avtobus to‘ldi!")
        break

print("Umumiy yo‘lovchilar soni:", umumiy)


# 5-masala: Teskari tartibda chiqarish
son = int(input("Son kiriting: "))

for i in range(son, 0, -1):
    if i == 3:
        continue  # 3 soni o‘tkazib yuboriladi
    print(i)

    