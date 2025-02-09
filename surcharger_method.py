from abc import ABC   # permet de définir des classes de base, Abstract Base Class



class Shape(ABC):
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return length * length
