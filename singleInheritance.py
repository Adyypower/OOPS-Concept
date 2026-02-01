"""
This module demonstrates **Single Inheritance**.

Concept:
- A Child class (`Mac`) inherits properties and behaviors from a **single** Parent class (`Apple`).
"""

class Apple:
    """
    Parent Class (Base Class)
    """
    manufacturer = "Apple"
    contactWebsite = "www.Apple.com"

    def contactDetails(self):
        print("To contact, log on to:", self.contactWebsite)

class Mac(Apple):
    """
    Child Class (Derived Class)
    Inherits from Apple.
    """
    def __init__(self):
        self.yearOfManufacturer = 2017
        
    def manufactureDetails(self):
        """
        Prints details including inherited attribute 'manufacturer'.
        """
        print("Manufacturer: ", self.manufacturer) # Inherited from Apple
        print("Year of Manufacture: ", self.yearOfManufacturer)    

# Execution
myMac = Mac()
myMac.manufactureDetails()
myMac.contactDetails() # Calling inherited method