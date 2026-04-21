from letter import LETTER_TEMPLATE

# Ввід даних
name = input("Введіть ім’я та прізвище: ")
date = input("Введіть дату поїздки: ")
persons = int(input("Введіть кількість осіб: "))

# Фіксована ціна
price_per_person = 15000

# Розрахунок загальної вартості
total_price = price_per_person * persons

# Логіка знижки
if persons > 5:
    discount = total_price * 0.05
else:
    discount = 0

# Фінальна сума
final_price = total_price - discount

# Формування листа
letter = LETTER_TEMPLATE.format(
    name=name,
    date=date,
    persons=persons,
    price_per_person=price_per_person,
    total_price=int(total_price),
    discount=int(discount),
    final_price=int(final_price)
)

# ЄДИНИЙ print
print(letter)