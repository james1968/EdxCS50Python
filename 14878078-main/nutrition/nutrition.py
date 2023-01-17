fruit = input("Item: ")
fruit = fruit.lower()

fruit_cal = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "pear": 100,
    "kiwifruit": 90,
    "orange": 80,
    "sweet cherries": 100
    }

if fruit in fruit_cal:
    print(f"Calories: {fruit_cal[fruit]}")
else:
    quit()

