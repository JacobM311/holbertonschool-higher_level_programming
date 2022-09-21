#!/usr/bin/python3
"""
Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """smelly"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
