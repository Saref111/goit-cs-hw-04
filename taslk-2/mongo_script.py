from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

# Підключення до MongoDB
client = MongoClient('mongodb+srv://root:root@cluster0.rqsgk8e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['cats_database']
collection = db['cats']

# Функція для виведення всіх записів із колекції
def read_all_cats():
    cats = collection.find({})
    for cat in cats:
        print(cat)

# Функція для виведення інформації про кота за ім'ям
def read_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print("Кіт з ім'ям '{}' не знайдено.".format(name))

# Функція для оновлення віку кота за ім'ям
def update_cat_age(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.modified_count > 0:
        print("Вік кота '{}' оновлено до {} років.".format(name, new_age))
    else:
        print("Кіт з ім'ям '{}' не знайдено.".format(name))

# Функція для додавання нової характеристики до списку features кота за ім'ям
def add_feature_to_cat(name, new_feature):
    result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    if result.modified_count > 0:
        print("Нова характеристика '{}' додана до кота '{}'.".format(new_feature, name))
    else:
        print("Кіт з ім'ям '{}' не знайдено.".format(name))

# Функція для видалення запису з колекції за ім'ям тварини
def delete_cat_by_name(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print("Кіт з ім'ям '{}' видалено.".format(name))
    else:
        print("Кіт з ім'ям '{}' не знайдено.".format(name))

# Функція для видалення всіх записів із колекції
def delete_all_cats():
    result = collection.delete_many({})
    print("Усі записи з колекції видалено. Кількість видалених записів: {}".format(result.deleted_count))

if __name__ == "__main__":
    # Додаткові тести
    # Додавання кількох котів у базу даних для тестування
    collection.insert_many([
        {"name": "Barsik", "age": 3, "features": ["ходить в капці", "дає себе гладити", "рудий"]},
        {"name": "Murzik", "age": 5, "features": ["поганенький", "любить їсти"]},
        {"name": "Pushok", "age": 2, "features": ["пухнастий", "грається з м'ячиком"]}
    ])

    # Виведення всіх котів
    print("Усі коти:")
    read_all_cats()
    print("\n")

    # Виведення інформації про кота за ім'ям
    cat_name = "Barsik"
    print("Інформація про кота з ім'ям '{}':".format(cat_name))
    read_cat_by_name(cat_name)
    print("\n")

    # Оновлення віку кота
    cat_name = "Barsik"
    new_age = 4
    print("Оновлення віку кота '{}':".format(cat_name))
    update_cat_age(cat_name, new_age)
    print("\n")

    # Додавання нової характеристики до кота
    cat_name = "Barsik"
    new_feature = "гарний"
    print("Додавання нової характеристики '{}' коту '{}':".format(new_feature, cat_name))
    add_feature_to_cat(cat_name, new_feature)
    print("\n")

    # Видалення кота за ім'ям
    cat_name = "Murzik"
    print("Видалення кота з ім'ям '{}':".format(cat_name))
    delete_cat_by_name(cat_name)
    print("\n")

    # Виведення всіх котів після видалення
    print("Усі коти після видалення:")
    read_all_cats()
    print("\n")

    # Видалення всіх котів
    print("Видалення усіх котів:")
    delete_all_cats()
    print("\n")
