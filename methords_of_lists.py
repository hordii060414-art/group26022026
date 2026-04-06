numbers = [1, 3 , 4]
names = ['Anna', "Ivan"]
mixed = [
    1,
    90.901,
    True,
    False,
    "some text",
    ['123', 1232],
]

first_element = mixed[0]
print(first_element)

third_element = mixed[2]
print(third_element)

last_element = mixed[-1]
print(last_element)

last_element_in_last_element = last_element[-1]
print(last_element_in_last_element)

#some_element = mixed[7895645987]

#
string = 123
print(id(string))
string = string + 1
print(id(string))

numbers = [1, 3, 4]
print(id(string))
numbers[0] = 200
print(numbers)
print(id(string))

# add values
numbers.append(3000)
numbers.append(3000)
print(numbers)
print(id(string))

numbers.insert(1, 22)
print(numbers)
print(id(string))

# remove data
numbers.remove(3)
print(numbers)
numbers.pop()
print(id(string))
numbers.pop(0)
print(numbers)

is_33_presented_in_numbers = 33 in numbers
print(is_33_presented_in_numbers)
if is_33_presented_in_numbers:
    numbers.remove(33)
print(numbers)

# length of list
elements_in_numbers_count = len(numbers)
print(elements_in_numbers_count)

# slices
numbers2 = [1,7,2,3]
print(numbers2)
numbers2.sort(reverse=True)
print(numbers2)
print(numbers2)

numbers3 = sorted(numbers2)
print(numbers3, 'sorted')
print(numbers2)
print(id(numbers3))
print(id(numbers2))

# slices
#          age, weight, salsry, name, surname, hobbies
person_data = [22,          85,     56000,"Alex", "Bush",['soccer', "tennis"]]
hobbies = person_data[-1]
print(hobbies)
name_surname = person_data[3:4+1]
print(name_surname)
print(id(person_data))
copy_of_person_data = person_data[:]
print(copy_of_person_data)
print(id(copy_of_person_data))

reversed_data = person_data[::]
print(reversed_data)

copy_of_person_data2 = person_data.copy()
print(copy_of_person_data2)

# mult and summa

words = ["apple", "banana", "cherry"]
words2 = ["pans", "caps"]
many_words = words * 200
print(many_words)

#words.append(words2)
#words = words + words2
words.extend(words2)
words.extend('yghegheighighighuej')
print(words)

reversed_data = person_data[::3]
print(reversed_data)

copy_of_person_data2 = person_data.copy()
print(copy_of_person_data2)

# slices with strings
text = 'I love Kremenchuh'
city = text[7:]
print(city)

fifth_letter = text[4]
#text[4] = 'g'
print(fifth_letter)

for letter in text:
    print(letter)

is_odessa_in_text = "odesa" in text.lower()
print(is_odessa_in_text)

# mult and summa
#table_power_3 = []
#table_power_2 = []
#power_list = [0, 1, 2, 3, 4]*100000000

#for power in power_list:
    #table_power_2.append(2 ** power)
   # table_power_3.append(3 ** power)
#print(table_power_3)
#print(table_power_2)

#  NEVER DO THIS AGAIN
some_list = [0, 1, 2, 3, 4]
for item in some_list:
    print(item)
    some_list.append(item*2)

    if item > 1000:
        break
print(some_list)































