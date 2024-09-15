# file_path = "C:\\Users\\GC\\Desktop\\Cosmios\\1Week\\names.txt"

# with open(file_path, 'a', encoding="utf-8") as file:


#     while(True):


#         name = input("Çıkış yapmak için q'ya basınız. \n İsim giriniz: ")

#         if(name == 'q'):
#             break

#         line_name = name + '\n'

#         file.write(name)

# #     # dosyayı okur
# # with open(file_path, 'r') as file:

# #     lines = file.readlines()

# #     print(lines)

# # for line in lines:
# #     print(line)

# file.close()

# column -> sütunlar
# row -> satırlar

import os
import csv

folder_path = "C:\\Users\\GC\\Desktop\\Cosmios\\1Week\\folder_test"
file_name = "stock.csv"

file_path = os.path.join(folder_path, file_name)

if not (os.path.exists(file_path)):

    with open(file_path, 'w', newline= "") as file:

        writer = csv.writer(file)
        writer.writerow(["Product", "Count"])
        writer.writerow(["Hats", 352])
        writer.writerow(["Shoes", 254])
        writer.writerow(["Glasses", 257])

        print("File created successfully")

else:
    with open(file_path, 'r') as file:

        reader = csv.DictReader(file)

        for row in reader:
            product = row["Product"]
            count = row["Count"]
            print(f"{product} Ürününden {count} adet bulunmaktadır.")

        # reader = csv.reader(file)

        # for row in reader:
        #     print(row)

        # dict_reader = csv.DictReader(file)

        # for r in dict_reader:
        #     print(r)






