from abc import abstractmethod, ABC
from symtable import Class


class Person:
    population = 0  # Атрибут класса

    def __init__(self, name):
        self.name = name # Атрибут объекта класса
        Person.population += 1


    @classmethod
    def get_population(cls):
        return cls.population

# person1 = Person("Ardager")
# person2 = Person("Ardager2")
# person3 = Person("Ardager3")

# print(Person.get_population())




class Circle:

    def __init__(self, radius):
        self._radius = radius  # Атрибут объекта класса

    @property
    def radius(self):
        return "property"

    def radius_2(self):
        return  "Just method"



# circle = Circle(5)
# print(circle.radius)
# print(circle.radius_2())




# Пример простого декоратора

# 3     step   def hello():
def my_decorator(func):

    #4
    def wrapper():
        # 5
        print("Перед выполнением функции")
        func()
        print("После выполнения функции")

    return wrapper

# 2
@my_decorator
def hello():
    print("Привет!!!")
# 1
# hello()



# Декораторы с аргументами


def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator


# amount = int(input("Введите число"))


# @repeat(amount)
# def greet():
#     print("Привет!!")


# greet()


                 #MyClass
def class_decorator(cls):
                #MyClass
    class NewClass(cls):

        def new_method(self):
            return "Новый метод!!!"

    return NewClass


@class_decorator
class MyClass:

    def old_method(self):
        return "Старый метод!!!"


# obj = MyClass()
#
# print(obj.old_method())
# print(obj.new_method())
