"""
This module explains the **`__init__`** method (Constructor).
"""

class Employee:
    """
    Demonstrates how to use __init__ to initialize objects with specific data.
    """
    
    def __init__(self, name, age):
        """
        The Constructor Method.
        
        Args:
            name (str): The name to assign to this employee.
            age (int): The age to assign.
            
        Run automatically when `Employee()` is called.
        """
        self.name = name # Assigning argument to instance attribute
        self.age = age

    def enterEmployeeDetails(self):
        """Example method to access attributes."""
        print(self.name, self.age)

    def displayEmployeeDetails(self):
        """Displays the employee properties."""
        print(self.name, self.age)    

# Creating an object triggers __init__ automatically
employeeOne = Employee("Adity", 12) 
employeeOne.displayEmployeeDetails()