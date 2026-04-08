numbers = [3, 7, 2, 9, 4, 6, 1, 8]

# парні числа
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# множимо на 2
doubled_even = []
for num in even_numbers:
    doubled_even.append(num * 2)

# перевірка і видалення 8
if 8 in doubled_even:
    doubled_even.remove(8)

print(doubled_even)

words = ["apple", "banana", "kiwi", "pear", "banana", "plum"]

# унікальні слова
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)

# слова довші 4 символів
long_words = []
for word in unique_words:
    if len(word) > 4:
        long_words.append(word)

# у верхній регістр
upper_words = []
for word in long_words:
    upper_words.append(word.upper())

# перевірка
if "BANANA" in upper_words:
    print("BANANA є у списку")

print(upper_words)