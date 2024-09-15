# listeler => array => []

country = ['Turkey', 'Germany', 'New Zeland', 'Poland']
print(country)
print(type(country))

sentence = 'Cosmios Yazılım'

sentence_list = list(sentence)
print(sentence_list)

word_list = [sentence]
print(word_list)

mixed_list = ['Ali', 45, False, 37.5, [1, 2, 3]]
print(mixed_list)

empty_list1 = list()
empty_list2 = []

print("empty list 2", empty_list2)

# .append() --> listenin sonuna ekler
empty_list2.append('Cosmios')
print('empty list 2:', empty_list2)

country.append('India')
print('Country List: ', country)

# .insert(index, eleman) --> istenilen indexe ekler.
country.insert(1, 'China')
print('Country List: ', country)

# .remove() --> belirtilen elemanı siler.
country.remove('New Zeland')
print('Country List: ', country)

# .pop() --> belirtilen indexteki elemanı siler.
country.pop(1)
print('Country List: debug', country)

# belirli indexteki elemanı silme
# eleman = country[1]
country.remove(country[1])
print(country)

# # .sort() --> listeyi sıralar
# country.sort()
# print('Country List: ', country)

# test_int = [5, 15, 2, 54, -5, 0]
# test_int.sort()
# print('Sorted Int List: ', test_int)

# # len() --> listenin uzunluğunu verir
# print('Country List Length: ', len(country))
# print('Length of Int List', len(test_int))

# print('Min number: ', test_int[0])
# print('Forth number: ', test_int[3])

# # liste içerisinde liste --> nested list
# student_list = [['Ali', 'Ayşe', 'Fatma'], [15, 54, 25]]
# print(student_list[1][1])

# print(student_list[0][0], student_list[1][0])

# # Liste dilimleme
# # [:], [5:], [:2], [::2]

# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers = list(range(1, 11))

# print(numbers[:]) # tamamını yazdırır
# print(numbers[2:]) #2. indexten itibaren listenin sonuna kadar
# print(numbers[2:5]) # 2. index ile 5. index arasındakileri yazar.
# print(numbers[:5]) # 5. indexe kadar yazar
# print(numbers[::-1]) # tamamını tersten yazdırır

# # Tuple 
# tuple_ex = ('Cosmios', )
# print(tuple_ex)
# print(type(tuple_ex))

# empty_tuple = tuple()

# my_tuple = (1, 2, 15, 8)
# print(my_tuple)
# print(type(my_tuple))

# tuple_to_list = list(my_tuple)
# tuple_to_list.sort()
# print(tuple_to_list)
# print(type(tuple_to_list))

# print(my_tuple[0])





