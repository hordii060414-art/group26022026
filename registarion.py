import messanges


# ===== 1. ІМ'Я =====
name = input(messanges.MSG_INPUT_NAME)
name = name.strip()

if name.isalpha():
    name = name.title()
    print(messanges.MSG_NAME_OK.format(name=name))
else:
    print(messanges.MSG_NAME_ERROR)


# ===== 2. ВІК =====
age = input(messanges.MSG_INPUT_AGE)
age = age.strip().lstrip("0")

if age.isdigit() and age != "":
    print(messanges.MSG_AGE_OK.format(age=age))
else:
    print(messanges.MSG_AGE_ERROR)


# ===== 3. ТЕЛЕФОН =====
phone = input(messanges.MSG_INPUT_PHONE)
phone = phone.strip()

if phone.isdigit():
    print(messanges.MSG_PHONE_OK.format(phone=phone))
else:
    print(messanges.MSG_PHONE_ERROR)


# ===== ЗАВЕРШЕННЯ =====
print(messanges.MSG_FINISH)