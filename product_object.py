#Name, Size, Price, Stock -> Product

class Customer:

    all_customers = []

    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

        Customer.all_customers.append(self)


# attribute -> column
class Product:

    discount = 0.5

    all_products = []

    def __init__(self, name: str, size: int, price, stock) -> None:

        assert price > 0, f"Gelen fiyat bilgisi 0 dan küçük olamaz. Girdiğiniz fiyat{price}"

        self.name = name
        self.size = size
        self.price = price
        self.stock = stock

        Product.all_products.append(self)

    
    def calculate_total_price(self):
        return self.price * self.stock
    
    def calculate_discounted_price(self):
        return self.price * self.stock * Product.discount


product1 = Product("Shoes", 38, 854.75, 100)

product2 = Product("Hat", "M", 152.50, 250)

# print(type(product1))
# print(product1.name)
# print(product1.size)
# print(product2.name, product2.size)

total_price = product1.calculate_total_price()
print(total_price)

products = Product.all_products

for p in products:
    print(p.name, p.size, p.price, p.stock)

print(product1.calculate_discounted_price())



