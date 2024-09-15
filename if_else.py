# # if condition :
# #     komutlar
# # elif condition:
# #     komutlar
# # else 
# #     komutlar

# # ---------- IF ELSE BLOĞU -----------
# if False:
#     print("Hello World")
# else:
#     print("Good By World")

# # ---------- SAYI ÖRNEĞİ -----------

# # kullanıcıdan bir sayı al
# number = int(input("Bir sayı giriniz: "))

# # sayı 20 den büyük mü kontrolü
# if(number > 20): # 20 > 20

#     print("Sayı 20 den büyüktür")

# elif(number == 20):
#     print("Sayı 20 ye eşittir")

# else:
    
#     print("Sayı 20 den küçüktür")

# # ---------- HARF NOTU ÖRNEĞİ -----------
# grade = int(input("Sınavdan aldığınız not: "))


# if(grade > 100):
#     print("Geçersiz not girdiniz")
    
# else: 
#     four_grade = float(grade / 25)
    
#     print(f"Dörtlük sistemdeki nootunuz: {four_grade}")
    
#     # 3.5 ile 4 arası AA
#     if (3.5 < four_grade <= 4 ):
    
#         print("AA")
    
#     # 3 ile 3.5 arasında BA
#     elif(3 < four_grade <= 3.5):
    
#         print("BA")
    
#     # 2.5 ile 3 arasında BB
#     elif(2.5 < four_grade <= 3):
    
#         print("BB")
    
#     # 2 ile 2.5 arasında CC
#     elif(2 < four_grade and four_grade < 2.5):
    
#         print("CB")
    
#     else:
    
#         print("Kaldınız")

# ---------- HESAP MAKİNASI ---------
# 1- Toplama
# 2- Çıkarma
# 3- Çarpma
# 4- Bölme

islem = int(input("1-Toplama \n 2-Çıkarma \n 3-Çarpma \n 4-Bölme \n Yapmak istediğiniz işlemi seçiniz: \n"))

first_number = int(input("Birinci sayı: "))
second_number = int(input("İkinci sayı: "))

if(islem == 1):

    print(f"{first_number} + {second_number} = ", first_number + second_number)

elif(islem == 2):

    print(first_number - second_number)

elif(islem == 3):

    print(first_number * second_number)

elif(islem == 4):

    print(first_number / second_number)

else:
    print("Geçersiz işlem")