import requests

url = "https://dummyjson.com/recipes?limit=0"
data = requests.get(url).json()

recipes = data["recipes"]

# 1. список рецептов пиццы
pizza_recipes = [r for r in recipes if "pizza" in r["name"].lower()]

# 2. сколько итальянских блюд
italian_count = sum(1 for r in recipes if r["cuisine"] == "Italian")

# 3. самая калорийная страва
max_calorie_recipe = max(recipes, key=lambda r: r["caloriesPerServing"])

# 4. блюда при 190°C
recipes_190 = [
    r for r in recipes
    if "190" in r["instructions"][0]
]

# 5. сумма всех reviewCount
total_reviews = sum(r["reviewCount"] for r in recipes)

# вывод
print("Пиццы:", [r["name"] for r in pizza_recipes])
print("Итальянских блюд:", italian_count)
print("Самая калорийная:", max_calorie_recipe["name"])
print("При 190°C:", [r["name"] for r in recipes_190])
print("Всего отзывов:", total_reviews)