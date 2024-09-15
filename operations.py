# toplama

print(3 + 5)

x = 5
y = 10
z = x + y
print(z)
print(x + y)
print(10 + 5.2)

# çıkarma
print(10 - 2)

# bölme /
print(50 / 5)

a = 50
print(a / 4)

print((3 + 5) / 8)

# çarpma * 
print(3 * 4)

# üs alma **
print(3 ** 2)

print(64 ** 0.5)

# % mod alma (bir sayının bir sayıya bölümünden kalan)
print(15 % 2)

# yerinde işlem yapma
x = 10

x += 5 # x = x +5
print("x: ", x)

# string işlemleri
fruit = "Apple"
print("Word: ", fruit)
print("İlk harf: ", fruit[0])
print("İkinci harf: ", fruit[1])

print("İlk harf dışındakiler:", fruit[1:])

print("1. ve 3. harf arası:", fruit[0:3])

print("Son harf: ", fruit[-1])

test = "cosmiso_iletisim"

print(test[-4:])

print(test[::-1])

print(test[1::3])

first_color = 'red'
second_color = 'blue'

print(first_color + ' ' + second_color)

# length ==> len() olarak kullanılır.

print("İlk rengin uzunluğu: ", len(second_color))

print(3 * first_color)

# strip fonksiyonu boşlukları kaldırır
space_str = "      listen spotify       "
print(space_str.strip())

# starts and ends fonksiyonları
mail = 'TeST@gmail.com'

print(mail.endswith('hotmail'))
print(mail.startswith('test'))

print(mail.upper())
print(mail.lower())

new_mail = mail.replace('gmail', 'hotmail')
print(new_mail)