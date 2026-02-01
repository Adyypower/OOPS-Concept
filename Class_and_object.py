"""
This module introduces the fundamental concepts of **Classes and Objects**.
"""

class Employee:
    """
    A Class is a blueprint (template) for creating objects.
    
    It encapsulates:
    - **Attributes** (Data/Variables): e.g., name, designation.
    - **Methods** (Behavior/Functions): e.g., hasAchievedTarget.
    """
    
    # Class Attributes (Shared by all instances if not overridden)
    name = "Aditya"
    designation = "Sales Executive"
    SalesMadethisWeek = 6
    
    def hasAchievedTarget(self):
        """
        A Method is a function defined inside a class that describes the object's behavior.
        The 'self' parameter refers to the specific object calling this method.
        """
        if self.SalesMadethisWeek >= 5:
            print("Target Achieved")
        else:
            print("Target Not Achieved")

# Object Creation
employeeOne = Employee() # Creating an instance of Employee
print(employeeOne.name) # Accessing attribute
employeeOne.hasAchievedTarget() # Calling method

employeeTwo = Employee() # Creating another instance
