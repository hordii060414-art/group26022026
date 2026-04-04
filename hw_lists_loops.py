# Завдання 1
print("=" * 40)
print("Завдання 1")
print("=" * 40)

numbers = [1, 5, 2, 8, 3, 7]

# Знаходимо найбільше число
max_number = max(numbers)
print(f"Список чисел: {numbers}")
print(f"Найбільше число: {max_number}")

# Знаходимо найменше число
min_number = min(numbers)
print(f"Найменше число: {min_number}")

# Знаходимо суму всіх чисел
sum_numbers = sum(numbers)
print(f"Сума всіх чисел: {sum_numbers}")

print("\n" + "=" * 40)
print("Завдання 2")
print("=" * 40)

# Завдання 2
grades = [10, 8, 12, 7, 9]
print(f"Список оцінок: {grades}")

# Знаходимо середній бал
average_grade = sum(grades) / len(grades)
print(f"Середній бал: {average_grade:.2f}")

# Виводимо всі оцінки вище середнього
above_average = [grade for grade in grades if grade > average_grade]
print(f"Оцінки вище середнього ({average_grade:.2f}): {above_average}")

# Альтернативний варіант з циклом for (якщо спискові вирази ще не проходили)
print("\n--- Альтернативний варіант з циклом for ---")
print("Оцінки вище середнього: ", end="")
for grade in grades:
    if grade > average_grade:
        print(grade, end=" ")
print()

print("\n" + "=" * 40)
print("Робота завершена!")
print("=" * 40)