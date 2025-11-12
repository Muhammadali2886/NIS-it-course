# while True:
#         a =input("kirit")
#         if a == "chapga":
#             print("Robot chapga burildi")
#         elif a== "o'nga":
#             print("Robot o'nga burildi")
#         elif a == "orqaga":
#             print("Robot orqaga burildi")
#         elif a == "0":
#             print("Dastur tugadi.")
#             break
#         else:
#             print("Noma'lum buyruq:", a)

# parol = "ucell"
# while True:
#     a = input("parol kirit")
#     if parol !=a:
#         print("parol xato")
#         continue
#     sum = int(input("qancha mb kerak kirit"))
#     if sum <=0:
#         print("0dan katta bo'lsin")
#         continue
# while True:
#     day = input("Hafta kunini kiriting : ").strip().lower()
#     if day == "dushanba":
#         print("Dushanba: 8:00 - 12:00 dars, 14:00 - loyiha ustida ishlash")
#     elif day == "seshanba":
#         print("Seshanba: 9:00 - laboratoriya, 17:00 - sport zali")
#     elif day == "chorshanba":
#         print("Chorshanba: 10:00 - konsultatsiya, 15:00 - kitob o'qish")
#     elif day == "payshanba":
#         print("Payshanba: 9:30 - mashg'ulot, 19:00 - do'stlar bilan uchrashuv")
#     elif day == "juma":
#         print("Juma: 8:00 - yakuniy imtihonlar, 20:00 - dam olish")
#     elif day == "shanba":
#         print("Shanba: 10:00 - bozor, 14:00 - oilaviy tadbir")
#     elif day == "yakshanba":
#         print("Yakshanba: Dam olish, haftani rejalashtirish")
#     else:
#         print("Noma'lum kun. Iltimos, dushanba, seshanba, chorshanba, payshanba, juma, shanba yoki yakshanba kiriting.")




# while True:
#     buyruq = input("Robotga buyruq bering (oldinga/orqaga/chap/ong): ").lower()

#     if buyruq == "oldinga":
#         print("Robot 1 qadam oldinga yurdi ■")
#     elif buyruq == "orqaga":
#         print("Robot 1 qadam orqaga yurdi ■")
#     elif buyruq == "chap":
#         print("Robot chapga burildi ■")
#     elif buyruq == "ong":
#         print("Robot o‘ngga burildi ■")
#     else:
#         print("Noto‘g‘ri buyruq!")


while True:
    son = int(input("Son kiriting: "))

    if son % 3 == 0 and son % 5 == 0:
        print("FizzBuzz")
    elif son % 3 == 0:
        print("Fizz")
    elif son % 5 == 0:
        print("Buzz")
    else:
        print(son)


import random
tasodifiy_son = random.randint(1, 10)

while True:
    taxmin = int(input("1 dan 10 gacha sonni toping: "))

    if taxmin == tasodifiy_son:
        print("To‘g‘ri topdingiz ■")
        break
    else:
        print("Xato! Qayta urinib ko‘r.")


ball = 0

while True:
    buyruq = input("Buyruq kiriting (+, -, stop): ")

    if buyruq == "+":
        ball += 1
        print("Ball:", ball)
    elif buyruq == "-":
        ball -= 1
        print("Ball:", ball)
    elif buyruq == "stop":
        print("O‘yin tugadi. Yakuniy ball:", ball)
        break
    else:
        print("Noto‘g‘ri buyruq!")
