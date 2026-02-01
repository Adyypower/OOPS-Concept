"""
This module demonstrates **Inheritance** and **Encapsulation** in Python.

Concepts Covered:
1.  **Inheritance**: `Chair` inherits from `Furniture`.
2.  **Super()**: Using `super().__init__` to call the parent class constructor.
3.  **Encapsulation**: Using private members (double underscore `__legs`) to hide data.
"""

class Furniture:
    """
    Base class representing general Furniture.
    """
    def __init__(self, wood_type="teak Wood"):
        """
        Constructor to initialize the wood type.
        
        Args:
            wood_type (str): The type of wood used. Defaults to "teak Wood".
        """
        self.wood_type = wood_type    

    def DisplayWoodType(self):
        """Prints the type of wood."""
        print("Type of wood : ", self.wood_type)

class Chair(Furniture):
    """
    Derived class representing a Chair, which is a type of Furniture.
    Inherits attributes and methods from Furniture.
    """
    def __init__(self, wood_type="teak Wood"):
        """
        Constructor for Chair. calls the parent constructor and sets private attribute __legs.
        """
        super().__init__(wood_type) # Call parent constructor
        self.__legs = 4 # Private attribute (Encapsulation)

    def SetWoodType(self, wood):
        """
        Setter method to update the wood type.
        
        Args:
            wood (str): New wood type.
        """
        self.wood_type = wood    

    def ChairProperty(self):
        """Displays properties specific to the Chair."""
        print("chair details:  ")
        print("Wood type: ", self.wood_type)
        print("Number of legs: ", self.__legs)

# --- Execution Logic ---
furniture = Furniture()
furniture.DisplayWoodType()

choice = input("IS you want to change wood type for chair (yes/no)")
if choice.lower() == "yes":
    wood = input("Enter the wood type: ")
    chair = Chair(wood) 
else:
    chair = Chair()

chair.ChairProperty()    
chair.DisplayWoodType()
# furniture.DisplayWoodType() # Optional redundant call