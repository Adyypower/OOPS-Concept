"""
This module demonstrates **Polymorphism** via **Operator Overloading**.

Concept:
- We define how standard operators (`+`, `-`) behave for our custom objects (`Square`).
- This is done by implementing "magic methods" like `__add__` and `__sub__`.
"""

class Square:
    def __init__(self, side):
        self.side = side

    def __add__(self, other):
        """
        Overloads the `+` operator.
        Logic: Sum of perimeters (4 * side).
        """
        return ((4 * self.side) + (4 * other.side))

    def __sub__(self, other):
        """
        Overloads the `-` operator.
        Logic: Difference of perimeters.
        """
        return ((4 * self.side) - (4 * other.side))

square1 = Square(10)
square2 = Square(20)

print("Sum of both square (Perimeters): ", square1 + square2)
print("Difference of both square (Perimeters): ", square1 - square2)