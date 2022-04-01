import csv
import datetime


class Character:
    def __init__(self, name, midname, age, sex):
        self.name = name
        self.midname = midname
        self.age = age
        self.sex = sex

    def __repr__(self):
        return f'Имя: {self.name},' \
               f'Фамилия: {self.midname},' \
               f'Возраст: {self.age},' \
               f'Пол: {self.sex}'


class Food:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __repr__(self):
        return f'Что: {self.name},' \
               f'Сколько {self.count}'


class Functions:
    def __init__(self, file_path, columns):
        self.file_path = file_path
        self.columns = columns

    def create_info_file(self):
        """Метод создание пустого csv файла"""
        with open("info_2file.csv", "w", ) as file:
            pass

    def eat_food(self, character_obj, food_obj):
        with open("info_2file.csv", "a") as file:
            human = character_obj
            food = food_obj
            text = str("Съел(а)")
            data = datetime.datetime.now()
            writer = csv.writer(file, delimiter=";", lineterminator="")
            writer.writerow(
                (
                    human, text, food, data
                )
            )
            writer.writerow("\n")

    def give_all_food_info(self):
        """Отображает все сообщения"""
        with open("info_2file.csv", "r") as message_file:
            reader = csv.reader(message_file)
            Name = set(row[0] for row in reader)
        with open("info_2file.csv", "r") as message_file:
            reader = csv.reader(message_file)
            Food = set(row[0] for row in reader)
        with open("info_2file.csv", "r") as message_file:
            reader = csv.reader(message_file)
            When = set(row[3] for row in reader)
        return f'{Name}\n Что ел: {Food}\n Когда: {When}'


if __name__ == "__main__":
    data_characters = Functions("info_2file.csv", ["name", "midname", "age", "sex", "food", "time"])
    c1 = Character("Ангелина", "Баратрума", 18, "Женский")
    c2 = Character("Ашот", "Ваковский", 20, "Мужской")
    f1 = Food("Дыня", 2)
    f2 = Food("Малина", 1)
    data_characters.eat_food(c1, f1)
    data_characters.eat_food(c2, f2)
    # print(data_characters.give_all_food_info())