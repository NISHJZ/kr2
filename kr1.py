import csv


class Bullet:
    def __init__(self, calibr, mass):
        self.calibr = calibr
        self.mass = mass
        self.power = round(mass * calibr)

    def __repr__(self):
        return f" Калибр: {self.calibr}," \
               f" Масса: {self.mass}," \
               f" Мощность: {self.power}"


class Clip:
    def __init__(self):
        self.stack = []

    def append_bullet(self, bullet_obj):
        self.stack.insert(0, bullet_obj)

    def remove_bullet(self):
        self.stack.pop(0)

    def show_clip(self):
        return self.stack

    def get_info_about_clip(self):
        with open("info.csv", "a", newline='') as file:
            writer = csv.writer(file, delimiter=';', lineterminator="")
            writer.writerow(self.show_clip())

    def create_info_file(self):
        """Метод создание пустого csv файла"""
        with open("info.csv", "w", ) as file:
            pass


if __name__ == "__main__":
    Magazin = Clip()
    Magazin.create_info_file()
    Pylia_1 = Bullet(7.62, 790)
    Pylia_2 = Bullet(5.62, 70)
    Magazin.append_bullet(Pylia_1)
    Magazin.append_bullet(Pylia_2)
    Magazin.append_bullet(Pylia_1)
    Magazin.append_bullet(Pylia_1)
    print(Magazin.show_clip())
    Magazin.remove_bullet()
    print(Magazin.show_clip())
    Magazin.get_info_about_clip()