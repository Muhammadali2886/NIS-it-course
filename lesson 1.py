# ball = int(input("Ballingizni kiriting: "))
# if 1 <= ball <= 1000:
#     print("Sizning darajangiz: Boshlovchi ")
# elif 1000 < ball <= 5000:
#     print("Sizning darajangiz: O‘rta daraja ")
# elif 5000 < ball <= 10000:
#     print("Sizning darajangiz: Usta ")
# else:
#     print("Noto‘g‘ri ball kiritildi yoki siz 10000 dan oshdingiz ")

gradus = int(input("Haroratni kiriting : "))
if gradus < 0:
    print("Tashqarida muzdek, qor yogmoqda ")
elif 0 <= gradus < 10:
    print("Sovuq tumanli havo ")
elif 10 <= gradus < 20:
    print("Salqin, ehtimol yomg‘ir yogmoqda ")
elif 20 <= gradus < 30:
    print("Iliq va yoqimli havo ")
elif 30 <= gradus < 40:
    print("Issiq, quyosh charaqlab turibdi ")
else:
    print("Juda issiq! Chol darajasidagi havo ")