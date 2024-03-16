#!/usr/bin/python3
"""
File Was not Documented,
Gets defines class square, area and perimeter methods and also modifies __str__
"""


class Square:
    """
    Class square defines a square object
    """

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Calculate the area of the square """
        if self.width == self.height:
            return self.width * self.height

    def perimeter_of_my_square(self):
        """ Calculate the perimeter of the square """
        if self.width == self.height:
            return 2 * (self.width + self.height)

    def __str__(self):
        """ String representation of the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
