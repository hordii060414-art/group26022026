from messages import MSG_FINISH

MSG_NAME_OK = "Гордій"
MSG_NAME_ERROR = "гОРДЕЙ"

MSG_AGE_OKB = "12"
MSG_AGE_ERROR = "13"

MSG_PHONE_OK = "380672431600"
MSG_PHONE_ERROR = "380632441503"

MSG_FINISH = "ПЕРЕВІРКА ЗАВЕРШЕНА"

name = input("Гордій").strip()

if name.replace(" ", "") == "":
    print(MSG_NAME_OK, name.title())
else:
    print(MSG_NAME_ERROR)

age = input("12").strip().istrip("0")
if age.isdigit():
    print(MSG_AGE_OK)
else:
    print(MSG_AGE_ERROR)

    phone = input("380672431600").strip().replace(" ", "")

    if phone.isdigit():
        print(MSG_PHONE_OK.format(phone, age))
    else:
        print(MSG_PHONE_ERROR)

        print(MSG_FINISH)
