"""
This module demonstrates the difference between **Class Attributes** and **Instance Attributes**.

1.  **Class Attribute**: belongs to the Class. Shared by all instances.
2.  **Instance Attribute**: belongs to specific Object. Unique to that instance.
"""

class Employee:
    """
    Employee Class showing attribute lookup order.
    """
    # Class Attribute (Shared)
    numberOfWorkingHours = 40

# 1. Accessing Class Attribute
employeeOne = Employee()
print("Class Attribute (via Object):", employeeOne.numberOfWorkingHours) # Prints 40

# 2. Modifying Class Attribute (affects all future lookups if not overridden)
Employee.numberOfWorkingHours = 45
print("Modified Class Attribute:", employeeOne.numberOfWorkingHours) # Prints 45

# 3. Creating an Instance Attribute
employeeOne.name = "Aditya"
print("Instance Attribute:", employeeOne.name)

# 4. "Overriding" Class Attribute with Instance Attribute
# When we assign to self.attribute or obj.attribute, Python creates a NEW instance attribute
# shadowing the class attribute for THIS object only.
employeeOne.numberOfWorkingHours = 42 # Creates instance attribute
print("Shadowing Class Attribute:", employeeOne.numberOfWorkingHours) # Prints 42 (Instance)

# 5. Other objects still see the Class Attribute
employeeTwo = Employee()
print("Other Object (Class Attribute):", employeeTwo.numberOfWorkingHours) # Prints 45