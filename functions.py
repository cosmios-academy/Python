# def function_name(parameter1, parameter2):

#     variable = parameter2 + parameter1

# ilk fonksiyon
def hello_world():

    print("Hello World")


# i = 0

# while (i < 5):

#     hello_world()

#     i += 1

# def test(num1: int, num2: int, name: str):

#     print(num1, num2, name)

# test(3,"qweqe", 5)

# def toplama(num1, num2):

#     sonuc = num2 + num1

#     return sonuc

# # sayi1 = 5
# # sayi2 = 10

# # islem_sonucu = toplama(sayi1, sayi2)

# # print(islem_sonucu)

# def cikarma(num1, num2):

#     return num2 - num1

# def carpma(num1, num2):

#     return num2 * num1

# def bolme(num1, num2):

#     return num2 / num1

# islem = int(input("Hangi işlemi yapmak istiyorsunuz? \n 1-Toplama \n 2-Çıkarma \n 3-Çarpma \n 4-Bölme \n"))

# sayi1 = int(input("1. Sayı:"))
# sayi2 = int(input("2. Sayı:"))

# if(islem == 1):

#     islem_sonucu = toplama(sayi1, sayi2)

#     print(islem_sonucu)

# elif(islem == 2):

#     islem_sonucu = cikarma(sayi1, sayi2)

#     print(islem_sonucu)

# elif(islem == 3):

#     print(carpma(sayi1, sayi2))

# elif(islem == 4):

#     print("İşlem sonucu", bolme(sayi1, sayi2) )

# else:

#     print("Hatalı tuşlama")

# ##### ---------------#######

# get_names()

# print(name)
# def get_names():

#     print("Ahmet", "Ayşe")


# name = "Fatma"

# def findMax(number_list):

#     x = max(number_list)

#     return x

# def findMin(number_list):

#     y = min(number_list)

#     return y


# def findMinAndMax(number_list):
#     x = max(number_list)

#     y = min(number_list)

#     return x, y

# numbers = [100, 857, 457, 116, 210, 55]

# # max_num = findMax(numbers)
# # min_num = findMin(numbers)

# max_num, min_num = findMinAndMax(numbers)

# print(max_num, min_num)

# import random

# def generate_otp():
    
#     otp = random.randint(100000, 999999)

#     return otp

# new_otp = generate_otp()

# print(new_otp)

# def func(*args):
#     print("test")

def market_list(urun1, urun2):

    print("Almak istediklerim: ", urun1, urun2)

def market_list_args(*urun):

    print("Almak istediklerim: \n")

    for i in urun:
        print(f"Ürün: {i}, Tipi: {type(i)}")

# market_list("süt", "ekmek")

# market_list_args("süt", "ekmek", "portakal", "çikolata", "yoğurt")

market_list_args(500.50, 10, "süt", False)

# def func(**kwargs): -> keyword args
#     print("test")

def ulkeler(**kwargs):

    print("Ulke, Başkent")

    for key, value in kwargs.items():
        print(f"{key}, {value}")

ulkeler(Turkiye="Ankara", Ispanya="Madrid", Fransa="Paris")

# local değişken ve global değişken


def yerel_yemekler(): # local variables

    sehir = "Adana"
    yemek = "Kebap"
    print(sehir)


ulke = "Turkiye" # global variable

def ulke_mutfaklari():
    print(ulke)

yerel_yemekler()

# hata verecekk
#print(sehir)
