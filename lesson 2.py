# password = input("Parolni kiriting: ")
# a = "admin"
# while password != a:
#     print("Parol xato, qaytadan kiriting")
#     password = input("Parolni kiriting: ")
# print("Parol to'g'ri, xush kelibsiz!")

# balance = int(input("Hisobingizdagi pul miqdorini kiriting: "))
# x =0
# while balance > 10:
#     product = int(input("Mahsulot narxini kiriting: "))
#     balance -= product
#     x += product
# print("pul oz qoldi")
# print("qoldiq:", balance)
# print("ishlatildi:", x )
# Eng katta sonni topish dasturi
x = int(input("kirit"))
y = 0
while x!=0:
    if x%2 == 1:
        print(x)
        y+=x
    x-=1
print(y)
