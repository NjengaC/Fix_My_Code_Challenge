#!/usr/bin/python3
"""
File Was not Documented,
Gets defines class square, area and perometer methods and also modifies __str__
"""


class square():
    """
    Class square defines a square object
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
