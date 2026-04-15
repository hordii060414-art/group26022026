car = {
    "model": "Toyota RAV4 Hybrid",
    "price_uah": 1587375,
    "engine_volume_l": 2.5,
    "gross_weight_kg": 2135,
    "max_speed_kmh": 180,
    "fuel_consumption_l_per_100km": 4.9,
    "interior_features": [
        "Мультимедійна система з сенсорним екраном",
        "Клімат-контроль",
        "Підігрів сидінь",
        "Цифрова панель приладів"
    ],
    "trunk": {
        "volume_l": 580,
        "volume_folded_l": 1690
    }
}

car["max_trailer_weight_braked_kg"] = 800
print("Назва:", car["model"])
print("Ціна:", car["price_uah"])
print("Перша опція інтер'єру:", car["interior_features"][0])
print("Багажник (складені сидіння):", car["trunk"]["volume_folded_l"])

insurance_rate = 0.005
insurance_payment = car["price_uah"] * insurance_rate
car["insurance_payment_uah"] = insurance_payment
print("Страховий платіж:", insurance_payment)

distance_km = 200
fuel_price_uah_per_l = 93
trip_cost = (
    car["fuel_consumption_l_per_100km"] * distance_km / 100
) * fuel_price_uah_per_l
print("Вартість поїздки:", trip_cost)