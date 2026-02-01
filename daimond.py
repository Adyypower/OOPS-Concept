"""
This module demonstrates the **Diamond Problem** (Method Resolution Order - MRO).

Concept:
- Happens in Multiple Inheritance when two parent classes inherit from the same base class.
- Python solves this using C3 Linearization (MRO).
- Structure: D -> (B, C) -> A
"""

class A:
    def method(self):
        print("This method belongs to class A")

class B(A):
    def method(self):
        print("This method belongs to class B")

class C(A):
    def method(self):
        print("This method belongs to class C")

class D(C, B):
    """
    Inherits from C and B.
    Both B and C inherit from A.
    """
    pass    

# Execution
d = D()
d.method()

# Explanation:
# Since D inherits from (C, B), python looks for 'method' in:
# 1. D (Not found)
# 2. C (Found! - prints "class C")
# 3. B
# 4. A
# Output will be "This method belongs to class C"