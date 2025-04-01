# # Родительский класс
# class Hero:
#
#     def __init__(self, name="John Doe", lvl=1, hp=100):
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
#
#     def action(self):
#         return f"base action"
#
#
# class Tank(Hero):
#
#     def __init__(self, name, lvl, hp, deff=100):
#         super().__init__(name, lvl, hp)
#         self.deff = deff
#
#
#     def rest(self):
#         self.hp += 5
#         return f"Rest and + 5 HP"
#
#     def action(self):
#         return f"{self.name}----Делает один шаг в перед"
#
#
# # naofumi = Tank("",1,100)
# nao_fumi = Tank(hp=1000 ,lvl=100 ,name="Nao Fumi", deff=50,)
#
#
# print(nao_fumi.action())



# Инкапсуляция: предполагает объединение данных и методов, работающих с этими данными, в единое целое — объект.
#   Это позволяет скрыть внутреннее устройство объекта и защитить данные от прямого доступа и изменений извне.

class BankAccount:

    def __init__(self, name, balance, password):
        self.name = name             # Открытый
        self._balance = balance       # Защишенный
        self.__password = password     # Приватный


    def top_up_balance(self, amount):
        if amount > 0:
            self._balance += amount
            return "Баланс пополнен"
        else:
            return "Сумма должна быть положительной"

    def reset_password(self):
        self.__password = 123456
        return 'reset accept'



ardager = BankAccount("Ardager", 100, 123)


# print(ardager._balance)
# print(ardager.reset_password())
# print(dir(ardager))