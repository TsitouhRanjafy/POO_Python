
class Rectangle:
    positions = {2, 6} # attribut de class

    def __init__(self,length,width,color="red"):
        self.width = width # attribut d'instance
        self.color = color
        self.length = length


    def calculate_area(self):
        return self.width * self.length

    @classmethod
    def get_postions(cls):
        return cls.positions

    @staticmethod
    def get_definition():
        """Donner la définition d'un rectangle"""
        return (
            "C'est un ..."
        )

rectangle = Rectangle(2,3)

print(f"{Rectangle(1,2).calculate_area()}")
print(f"{Rectangle.get_definition()}")
print(f"{Rectangle.get_postions()}")