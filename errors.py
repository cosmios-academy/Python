# # Syntax Error

# result = 10 +* 5

# my_list = [1, 2, 3
           
# # Name Error 

# variable = 5

# print(variabl)

# # Value Error

# word = "test"

# number = int(word)

# print(number)

# # Type Error 
# # örn veri ttabanında int kolona string kaydı yapmaya çalıştığımızda alırız.

# number = "123"

# # element = number[0]

# print(number.split())

# # Index Error

# my_list = [1, 2, 3, 4, 5]

# print(my_list[10])


# # File not fouund Error
# file_path = "C:\\Users\\GC\\Desktop\\Cosmios\\1Week\\folder_test\\test2.txt"

# with open(file_path, 'r') as file:

#     content = file.read()


try: 
    print("Yapılması gerekenler")
except:
    print("Bir hata oluştu")
else:
    print("Her şey yolunda gitti")
finally:
    print("Her zaman çalışır")


try:
    cities = {'Adana': '01', 'İstanbul': '34', 'Ankara': '06'}

    print(cities['İzmir'])

except KeyError:
    print("Böyle bir şehir bulunamadı")

except NameError:
    print("Değişken tanımlanmamıştır")


try:
    my_list = [1,2,3]

    print(my_list[5])

except IndexError:
    print("Bir hata oluştu")

except KeyError:
    print("test")



