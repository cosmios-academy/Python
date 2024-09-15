# kullanıcıdan ülke adı, nüfus, yüz ölçümü, başkent alınacak, listeye eklenecek.

# input() fonk ile kullanıcıdan input alınır.

# name = input("Lütfen adınızı giriniz: ")

# print("Girdiğiniz ad: ", name)

# age = int(input("Yaşınızı giriniz: "))
# print(type(age))

# --- Algorithm

# boş liste oluşturun. (country_detail)

# country değişkeni al 
# population değişkeni int
# area (yüz ölçümü) değişkeni float
# capital değişkeni

# alınan her veri oluşturulan boş listeye eklenecek

# liste print edilecek

# ---zorunlu değil

# kaçıncı elemanı silmek istiyorsunuz -- index alınacak ! trick
# o indexteki veri silinecek
# listenin son hali printlenecek

country_detail = []

country = input("Lütfen bir ülke adı giriniz: ")
population = int(input("Lütfen bir ülkenin nüfusu giriniz: "))
area = float(input("Lütfen ülkenin yüzölçümünü giriniz: "))
capital = input("Lütfen başkenti giriniz: ")

country_detail.append(country)
country_detail.append(population)
country_detail.append(area) 
country_detail.append(capital)

print(country_detail)

selected_eleman = int(input("Kaçıncı elemanı silmek istiyorsunuz? "))

country_detail.pop(selected_eleman)

# country_detail.remove(country_detail[selected_eleman -1 ])

print("Seçtiğiniz eleman listeden silindi.", country_detail)