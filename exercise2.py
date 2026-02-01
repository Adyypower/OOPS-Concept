"""
This module demonstrates **Operator Overloading**.

Concepts Covered:
- **Magic Methods (Dunder Methods)**: Specifically `__pow__`.
- **Operator Overloading**: Changing the behavior of the `**` operator for custom objects.
"""

class Square:
    """
    Class to mimic a number that can be squared.
    """
    def __init__(self, side):
        """
        Initialize with a side length.
        
        Args:
            side (int/float): The value of the side.
        """
        self.side = side

    def __pow__(self, other):
        """
        Overloads the power operator (**).
        Allows syntax like: square1 ** square2
        
        Args:
            other (Square): The exponent object.
            
        Returns:
            The result of self.side raised to the power of other.side.
        """
        return self.side ** other.side

# Execution
square1 = Square(2)
square2 = Square(3)
print("Power of both square: ", square1 ** square2) # 2 ** 3 = 8
