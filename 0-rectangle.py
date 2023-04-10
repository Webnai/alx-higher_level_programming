#!/usr/bin/python3
class Rectangle:
    """A class that represents a rectangle."""

    def __init__(self, width, height):
        """
        Initialize a new rectangle with the given width and height.

        Args:
            width (int or float): The width of the rectangle.
            height (int or float): The height of the rectangle.

        Raises:
            ValueError: If either width or height is negative or zero.
        """
        if width <= 0:
            raise ValueError("Width must be positive.")
        if height <= 0:
            raise ValueError("Height must be positive.")
        
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

