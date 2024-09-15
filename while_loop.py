# while(kosul):
#     işlemler


# ###### ------ 1 'DEN 10A KADAR SAYILAR ---------
# number = 1

# # sayı 10dan küçük olduğu sürece
# while (number < 10):

#     print(number)

#     # number = number + 1 ile aynı şey
#     number += 1


# # ------- LİSTEDEKİ ELEMANLARI YAZDIRMA -------
# my_list = ['C', 'O', 'S', 'M', 'I', 'O', 'S']

# i = 0

# while( i < len(my_list)): 

#     print(my_list[i])    

#     i += 1

# ------------ ATM -------------

bakiye = float(50000.50)

secenek = int(input("İşlemler: \n 1-Bakiye Sorgula \n 2-Para Çekme \n 3-Para Yatırma \n 4-Çıkış \n Seçiniz: "))

while(secenek != 4):

    # Bakiiye sorgula
    if(secenek == 1):
        print("Bakiyeniz: ", bakiye)

        secenek = int(input("İşlemler: \n 1-Bakiye Sorgula \n 2-Para Çekme \n 3-Para Yatırma \n 4-Çıkış \n Seçiniz: "))
    
    # para çek
    elif(secenek == 2):

        para_cek = int(input(f"Toplam bakiyeniz {bakiye}.\n Çekmek istediğiniz miktarı giriniz: "))

        if (para_cek > bakiye):

            print("Yeterli bakiye yok")
        
        else:
            bakiye -= para_cek

            print(f"Kalan bakiyeniz: {bakiye}")

        secenek = int(input("İşlemler: \n 1-Bakiye Sorgula \n 2-Para Çekme \n 3-Para Yatırma \n 4-Çıkış \n Seçiniz: "))
    
    # para yatırma
    elif(secenek == 3):

        para_yatir = int(input("Yatırmak istediğiniz miktarı giriniz: "))

        bakiye += para_yatir

        print(f"Toplam bakiyeniz: ", {bakiye})

        secenek = int(input("İşlemler: \n 1-Bakiye Sorgula \n 2-Para Çekme \n 3-Para Yatırma \n 4-Çıkış \n Seçiniz: "))
    
    elif(secenek == 5):
        print("Yanlış tuşlama yaptınız.")
        secenek = int(input("İşlemler: \n 1-Bakiye Sorgula \n 2-Para Çekme \n 3-Para Yatırma \n 4-Çıkış \n Seçiniz: "))

    else:
        print("Yanlış tuşlama yaptınız.")
        secenek = 5


