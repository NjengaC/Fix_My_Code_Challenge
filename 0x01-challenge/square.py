#!/usr/bin/python3
"""
File Was not Documented,
Gets defines class square, area and perometer methods and also modifies __str__
"""


class Square():
    """
    Class square defines a square object
    """
    height = 0
    width = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        if self.width == self.height:
            return self.width * self.height
        else:
            return 0

    def perimeter_of_my_square(self):
        """ Calculate the perimeter of square """
        if self.width == self.height:
            return (self.width * 2) + (self.height * 2)
        else:
            return 0

    def __str__(self):
        """ String representation of the square """
        if self.width == self.height:
            return "{}/{}".format(self.width, self.height)
        else:
            return "0/0"

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
