# and, or, not   ---> ve, veya, değil

# AND 
# T AND T -> T

# 25-35 yaş aralığındaki evli erkeklere reklam gösterilecek.

# 30, bekar, erkek
age = True
married = True
gender = True

# reklam = age and married and gender
# reklam = age and married and gender
# print(reklam)

# OR 
# 25-35 yaş aralığında veya evlilere ve erkek.
second_age = False
second_married = False
gender = True

reklam = second_age or second_married and gender # 0 and 1

# print(reklam)



a = True
b = False
c = True

# d = a and (b or c) # True and (False or True)
# print(d)

# e = c or (b and (a or c)) # True or (False and (False or True))
# print(e)

# NOT 
discount = True

new_dis = not discount

print(new_dis)


age = True # 36
married = True # evli 
gender = True # kadın

# 35 yaşından büyük evli kadın 

w_age = not age
print(w_age)

w_married = not married
print(w_married)

woman = (not age and married and not gender)
print(woman)

x = (not age or married and gender)
print("x:", x)


# iki öğrenci 
student1 = 'Ali'
student2 = 'Fatma'

ali_gr = 80
fatma_gr = 70

# <= , <, >=, >, ==, !=

print("Alinin notu Fatmanın notundan düşük veya eşit mi?", ali_gr <= fatma_gr) # küçük eşit mi
print("Alinin notu Fatmanın notundan düşük mü?", ali_gr < fatma_gr) # küçük mü
print('Alinin notu Fatmanın notundan büyük veya eşit mi?', ali_gr >= fatma_gr) # büyük veya eşit mi
print('Alinin notu Fatmanın notundan büyük mü?', ali_gr > fatma_gr) # büyük mü
print('Alinin notu Fatmanın notuna eşit mi?', ali_gr == fatma_gr) # eşit mi
print('Alinin notu Fatmanın notuna farklı mı?', ali_gr != fatma_gr) # farklı