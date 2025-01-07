from math import pi, sqrt

class Figure:
    sides_count = 0
    def __init__(self, color, sides):
        self.__sides = sides
        self.__color = color
        self.filled = True


    def get_color(self):
        return self.__color

    def __is_valid_color(self, *args):
        flag = True
        for i in args:
            if 0 <= i <= 255:
                continue
            else:
                flag = False
        return flag

    def set_color(self, *args):
        if self.__is_valid_color(*args):
            self.__color = args



    def __is_valid_sides(self, *args):
        spis = [i for i in args]
        flag = True
        for i in spis:
            if i < 0:
                flag = False
        if len(spis) == len(self.__sides) and flag == True:
            return True
        else:
            return False

    def get_sides(self):
        if self.sides_count > 1:
            return [self.__sides for i in range(self.sides_count)]
        else:
            return self.__sides

    def __len__(self):
        if isinstance(self.__sides, list):
            return sum(self.__sides)
        else:
            return self.__sides

    def set_sides(self, *new_sides):
        spis = [i for i in new_sides]
        if len(spis) != self.sides_count:
            pass
        else:
            self.__sides = spis


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides

    def get_square(self):
        return pi * self.__radius ** 2



class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = sides

    def get_square(self):
        p = (self.__sides * self.sides_count) / 2
        s = sqrt(p * (p - self.__sides) * (p - self.__sides) * (p - self.__sides))
        return s


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = sides


    def get_volume(self):
        return self.__sides ** 3



