"""
This module explains **Access Specifiers** in Python: Public, Protected, and Private.

Rules:
1.  **Public** (`name`): Accessible from anywhere (inside/outside class).
2.  **Protected** (`_name`): Intended for internal use and subclasses. Python does not enforce this strictly (convention only).
3.  **Private** (`__name`): Accessible ONLY inside the class definition. Python uses "Name Mangling" to hide it.
"""

class Car:
    # Public Attribute
    numberOfWheels = 4
    
    # Protected Attribute (Prefix with single underscore)
    _color = "black"
    
    # Private Attribute (Prefix with double underscore)
    __yearOfManufacture = 2022

class BMW(Car):
    def __init__(self):
        # Accessing Protected attribute (Allowed in subclass)
        print("protected attribute color : ", self._color)
        
        # Accessing Private attribute (Direct access FAILS in subclass)
        # print("private attribute year of manufacture : ", self.__yearOfManufacture) # AttributeError
        
        # To access private member of Parent, one would need Name Mangling or public getter methods.

car = Car()
print("public attribute number of wheels: ", car.numberOfWheels)

# Accessing Private Member using Name Mangling
# Python renames __yearOfManufacture to _Car__yearOfManufacture
print("Accessing private member via Name Mangling:", car._Car__yearOfManufacture)
