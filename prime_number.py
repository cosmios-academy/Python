# asal sayı kendisinden ve birden başka böleni olmayan.

asal_sayilar = []

# 1 ile 100 arasındaki sayılar
for sayi in range(2, 100):  # sayi = 13

    # Asal sayı gibi tanımlıyorum
    asal_mi = True

    # Bir bölen bulunmuşsa
    for bolen in range(2, sayi - 1):

        if(sayi % bolen == 0):

            # asal_mi değişkeni false çekilir.
            asal_mi = False

            # döngüden çıkılır
            break
    
    if(asal_mi):
        asal_sayilar.append(sayi)

print(asal_sayilar)
