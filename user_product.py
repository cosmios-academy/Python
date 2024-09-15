from product_object import Customer

print("Lütfen ad soyad giriniz:")

name = input("Ad")
surname = input("Soyad")

Customer(name, surname)

for c in Customer.all_customers:
    print(c.name, c.surname)



