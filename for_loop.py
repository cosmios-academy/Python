# ##### BREAK ######

# count = 150

# i = 1

# limit = int(input("Sınırlandırmak istediğiniz sayıyı giriniz: "))

# while(i < count):

#     if( i == limit):
#         print(i)
#         print("Döngü kırıldı.")
#         break

#     print(i)

#     i += 1

# ##### SAYI TAHMİN OYUNU ########
# import random

# # 0 ile 100 arasında random sayı oluşturulur.
# number = random.randint(0, 100)

# print("Sayı tahin oyununa hoşgeldiniz!")

# while True:

#     # kullanıcıdan bir tahmin alınır.
#     tahmin = int(input("1 ile 100 arasında bir tahmin giriniz: "))

#     # tahmin sayıdan küçükse daha büyük bir sayıı girilmeli
#     if (tahmin < number):
#         print("Yanlış Tahmin! Daha büyük bir sayı giriniz!")

#         # tahmin sayıdan büyükse daha küçük bir sayı girilmeli.
#     elif(tahmin > number):
#         print("Yanlış Tahmin! Daha küçük bir sayı giriniz!")
    
#     # sayı doğru tahmin edildiyse döngü kırılır.
#     elif(tahmin == number):
#         print("BRAVO!!")
#         break

#     else:
#         print("Bir hata oluştu")
#         break

# ####### FOR DÖNGÜSÜ #######

# # for eleman in list:
# #     islemler

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in numbers:
#     print(number)

# mevsimler = ['Sonbahar', 'Kış', 'İlkbahar', 'Yaz']

# for mevsim in mevsimler:
#     print(mevsim)

# mixed_list = [3.20, mevsimler, numbers]

# for i in mixed_list:
#     print(i)

# ilkbahar = mevsimler[2]

# for harf in ilkbahar:
#     print(harf)
#     print("5")

# times = int(input("Kaç kere bu mesajı göndermek istiyorsunuz: "))

# for i in range(times):
#     print(f"{i} İYİ HAFTALAR")

# colors = ["kırmızı", 'Mor', 'Mavi', 'Sarı', 'Yeşil', 'Beyaz'] 

# for index, color in enumerate(colors):
#     print(f"{index + 1}. elemandaki renk: {color}")


# for i in range(1, 6): 
#     for j in range(i): 
#         print("*", end="")
    
#     print("")


# sayilar = [ [1, 2, 3 ], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17] ]

# print("i j   ")
# for i, sayi in enumerate(sayilar):
#     for j, s in enumerate(sayi):
#         print(f"{i} {j}   ", s)

sales = [250, 300, 150, 400, 500, 600, 450]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

total_sales = 0

for sale in sales:
    total_sales += sale

print("Haftanın toplan satışı: ", total_sales)

max_sale = 0
max_day = ''

for i, s in enumerate(sales):

    if(s > max_sale):
        max_sale = s
        max_day = days[i]

print(f"En fazla satış {max_sale} ile {max_day} günü yapılmıştır.")
