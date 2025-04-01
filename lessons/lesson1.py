


# class Person:
#     # Конструктор Класса
#     def __init__(self, name, age, city):
#         # Атрибуты Класса
#         self.name_1 = name
#         self.age_1 = age
#         self.city_1 = city
#
#     # Метод Класса
#     def introduce(self):
#         print(f"Привет меня зовут {self.name_1}")
#
#     def update_age(self, age):
#         self.age_1 = age
#
#
# # Объект Класса Person\Экземпляр класса
# obj1 = Person("Арзыбек", 25, "Bishkek")
# int_test = 1
# str_test = "23"
# list_test = []
#
# str_test.lower()
# list_test.append(1)
# print(obj1.age_1)
# obj1.update_age(26)
# print(obj1.age_1)


# print(type(obj1))
# print()
# print(type("test"))
# print(type([]))
# print(type({}))


# MageHero - для название классов
# mage_hero - для название переменных функций

# Родительский\Супер\Базовый - Класс
class Hero:

    def __init__(self, name, lvl=1, hp=100):
        self.name = name
        self.lvl = lvl
        self.hp = hp


    def introduce(self):
        print(f"Я герой {self.name}, мой уровень {self.lvl}")

    def action(self):
        print(f"{self.name} выполняет базовое действие")


# kirito = Hero(lvl=90, name="Kirito", hp=1000)

# Наследование

# Дочерний\Подкласс
class Warrior(Hero):

    def rest(self):
        self.hp += 10
        print(f"{self.name} отдыхает и востонавливает здоровье ")

hero = Hero("Герой")
kirito = Warrior(lvl=90, name="Kirito", hp=1000)

kirito.introduce()



kirito.rest()





