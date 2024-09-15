my_dict = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3'
}

country_capitals = {
    'Türkiye': 'Ankara',
    'Almanya': 'Berlin',
    'Fransa': 'Paris',
}


print(country_capitals['Türkiye'])

country_capitals['Fransa'] = 'Marsilya'
print(country_capitals)

country_capitals['İspanya'] = 'Madrid'
print(country_capitals)

car = {
    'uretici': 'Citroen',
    'model': 'C5',
    'yil': 2018,
    'stoktaMi': True
}

print(car)

coffee = {
    'Name' : 'Iced Americano',
    'Description': 'Sade soğuk americano',
    'Price': 100.50
}

coffee['Milk'] = False

print(type(coffee['Price']))

# .keys(), .values() 
print(coffee.keys())
print(coffee.values())

# .items() 
print(coffee.items())

# in ---> Bir dictionary içerisinde aranan key var mı kontrolü yapılır.
# not in

print('Name' in coffee)

del coffee['Milk']
print(coffee)

# set() ----> {}

empty_set = set()

color_set = {'mor', 'mavi', 'kırmızı'}

# print(type(empty_set))
# print(type(color_set))

# .add()
color_set.add('siyah')

# print(color_set)

# remove
color_set.remove('siyah')

print(color_set)

# union
name_set = {'Ali', 'Ayşe'}

print(color_set.union(name_set))


