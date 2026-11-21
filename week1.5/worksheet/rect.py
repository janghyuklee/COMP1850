# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height
        if not isinstance(width, (int)) or not isinstance(height, (int)):
            raise TypeError("Width and height must be integers.")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    
    def is_square(self):
        """
        Return True if rectangle is square (width = height)
        """
        return self.width == self.height


    def area(self):
        """
        Return area
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Return perimeter
        """
        return 2 * (self.width + self.height)
