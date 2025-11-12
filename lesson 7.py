# import random
# x = random.randint(1, 10)
# while True:
#     y = int(input("raqam kirit"))
#     if x == y :
#         print("yutding")
#         print(x)
#     else:
#         print("hato qayta urunib ko'r")

import random
a = random.randint(0,1)
while True:
    x = input("tanga yoki gerb tanlang: ")
    if x == "tanga":
        if a == 0:
            print("yutdingiz")
            break
        else:
            print("yutqazdingiz")
    elif x == "gerb":
        if a == 1:
            print("yutdingiz")
            break
        else:
            print("yutqazdingiz")
    else:
        print("noto'g'ri tanlov")