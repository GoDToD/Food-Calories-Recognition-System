# 更新 food_labels 列表中的第二个单词首字母为小写
food_labels = [
    "Apple pie",
    "Baby back ribs",
    "Baklava",
    "Beef carpaccio",
    "Beef tartare",
    "Beet salad",
    "Beignets",
    "Bibimbap",
    "Bread pudding",
    "Breakfast burrito",
    "Bruschetta",
    "Caesar salad",
    "Cannoli",
    "Caprese salad",
    "Carrot cake",
    "Ceviche",
    "Cheesecake",
    "Cheese plate",
    "Chicken curry",
    "Chicken quesadilla",
    "Chicken wings",
    "Chocolate cake",
    "Chocolate mousse",
    "Churros",
    "Clam chowder",
    "Club sandwich",
    "Crab cakes",
    "Creme brulee",
    "Croque madame",
    "Cup cakes",
    "Deviled eggs",
    "Donuts",
    "Dumplings",
    "Edamame",
    "Eggs benedict",
    "Escargots",
    "Falafel",
    "Filet mignon",
    "Fish and chips",
    "Foie gras",
    "French fries",
    "French onion soup",
    "French toast",
    "Fried calamari",
    "Fried rice",
    "Frozen yogurt",
    "Garlic bread",
    "Gnocchi",
    "Greek salad",
    "Grilled cheese sandwich",
    "Grilled salmon",
    "Guacamole",
    "Gyoza",
    "Hamburger",
    "Hot and sour soup",
    "Hot dog",
    "Huevos rancheros",
    "Hummus",
    "Ice cream",
    "Lasagna",
    "Lobster bisque",
    "Lobster roll sandwich",
    "Macaroni and cheese",
    "Macarons",
    "Miso soup",
    "Mussels",
    "Nachos",
    "Omelette",
    "Onion rings",
    "Oysters",
    "Pad thai",
    "Paella",
    "Pancakes",
    "Panna cotta",
    "Peking duck",
    "Pho",
    "Pizza",
    "Pork chop",
    "Poutine",
    "Prime rib",
    "Pulled pork sandwich",
    "Ramen",
    "Ravioli",
    "Red velvet cake",
    "Risotto",
    "Samosa",
    "Sashimi",
    "Scallops",
    "Seaweed salad",
    "Shrimp and grits",
    "Spaghetti bolognese",
    "Spaghetti carbonara",
    "Spring rolls",
    "Steak",
    "Strawberry shortcake",
    "Sushi",
    "Tacos",
    "Takoyaki",
    "Tiramisu",
    "Tuna tartare",
    "Waffles"
]

# 保持 food_calories 字典不变
food_calories = {
    'Apple pie': 237,
    'Baby back ribs': 292,
    'Baklava': 417,
    'Beef carpaccio': 160,
    'Beef tartare': 160,
    'Beet salad': 43,
    'Beignets': 450,
    'Bibimbap': 210,
    'Bread pudding': 275,
    'Breakfast burrito': 290,
    'Bruschetta': 150,
    'Caesar salad': 190,
    'Cannoli': 340,
    'Caprese salad': 250,
    'Carrot cake': 410,
    'Ceviche': 70,
    'Cheesecake': 321,
    'Cheese plate': 400,
    'Chicken curry': 200,
    'Chicken quesadilla': 300,
    'Chicken wings': 290,
    'Chocolate cake': 367,
    'Chocolate mousse': 310,
    'Churros': 450,
    'Clam chowder': 186,
    'Club sandwich': 250,
    'Crab cakes': 400,
    'Creme brulee': 330,
    'Croque madame': 330,
    'Cup cakes': 150,
    'Deviled eggs': 450,
    'Donuts': 220,
    'Dumplings': 122,
    'Edamame': 270,
    'Eggs benedict': 250,
    'Escargots': 333,
    'Falafel': 270,
    'Filet mignon': 595,
    'Fish and chips': 290,
    'Foie gras': 312,
    'French fries': 67,
    'French onion soup': 250,
    'French toast': 110,
    'Fried calamari': 280,
    'Fried rice': 210,
    'Frozen yogurt': 300,
    'Garlic bread': 357,
    'Gnocchi': 160,
    'Greek salad': 350,
    'Grilled cheese sandwich': 177,
    'Grilled salmon': 186,
    'Guacamole': 210,
    'Gyoza': 176,
    'Hamburger': 380,
    'Hot and sour soup': 92,
    'Hot dog': 292,
    'Huevos rancheros': 250,
    'Hummus': 370,
    'Ice cream': 420,
    'Lasagna': 100,
    'Lobster bisque': 58,
    'Lobster roll sandwich': 343,
    'Macaroni and cheese': 190,
    'Macarons': 411,
    'Miso soup': 57,
    'Mussels': 300,
    'Nachos': 200,
    'Omelette': 70,
    'Onion rings': 197,
    'Oysters': 350,
    'Pad thai': 140,
    'Paella': 321,
    'Pancakes': 150,
    'Panna cotta': 385,
    'Peking duck': 330,
    'Pho': 250,
    'Pizza': 400,
    'Pork chop': 360,
    'Poutine': 290,
    'Prime rib': 450,
    'Pulled pork sandwich': 292,
    'Ramen': 220,
    'Ravioli': 160,
    'Red velvet cake': 200,
    'Risotto': 320,
    'Samosa': 174,
    'Sashimi': 330,
    'Scallops': 158,
    'Seaweed salad': 90,
    'Shrimp and grits': 90,
    'Spaghetti bolognese': 395,
    'Spaghetti carbonara': 240,
    'Spring rolls': 350,
    'Steak': 140,
    'Strawberry shortcake': 360,
    'Sushi': 311,
    'Tacos': 250,
    'Takoyaki': 240,
    'Tiramisu': 360,
    'Tuna tartare': 280,
    'Waffles': 170
}

def get_food_calories_and_name(index):
    return food_labels[index], food_calories[food_labels[index]]