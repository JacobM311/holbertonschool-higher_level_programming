#!/usr/bin/python3
"""
Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """stinky"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """informal string representation of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)
