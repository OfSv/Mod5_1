# Атрибуты и методы объекта
# Задача "Developer - не только разработчик"

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to_(self, new_floor):
        if type(new_floor) != int or new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i+1)


House_1 = House('ЖК Эльбрус', 30)
House_2 = House('ЖК Лесное', 5)
House_3 = House('Реконструкция', 3)
House_1.go_to_(5)
House_2.go_to_(4.2)
House_3.go_to_(-1)
