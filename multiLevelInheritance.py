"""
This module demonstrates **Multilevel Inheritance**.

Concept:
- Grandparent -> Parent -> Child
- `Guitar` inherits from `StringInstrument`, which inherits from `MusicalInstrument`.
- The Child class has access to attributes from the entire ancestry chain.
"""

class MusicalInstrument:
    """Grandparent Class"""
    numberofMajorkeys = 12

class StringInstrument(MusicalInstrument):
    """Parent Class (Child of MusicalInstrument)"""
    typeOfwood = "teak"    

class Guitar(StringInstrument):
    """
    Child Class (Child of StringInstrument)
    Inherits from both StringInstrument and MusicalInstrument.
    """
    def __init__(self):
        self.numberOfStrings = 6

    def guitarDetails(self):
        print("Number of strings: ", self.numberOfStrings)
        print("Type of wood: ", self.typeOfwood) # From Parent
        print("Number of major keys: ", self.numberofMajorkeys) # From Grandparent

# Execution
myGuitar = Guitar()
myGuitar.guitarDetails()