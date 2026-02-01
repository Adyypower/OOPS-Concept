"""
This module explains the concept of **`self`** and **Variable Scope** in Python OOP.
"""

class Employee:
    """
    Demonstrates the difference between Instance Attributes and Local Variables.
    """
    def employeeDetails(self):
        """
        Explains 'self' and instance attributes.
        """
        # 'self' refers to the current object instance.
        
        # Instance Attribute: Attached to 'self'. Accessible throughout the class.
        self.name = "Aditya"  
        print("Name : ", self.name)
        
        # Local Variable: Created only for this function execution. Inaccessible outside.
        age = 12  
        print("Age : ", age)

    def printDetailsUnique(self):
        """
        Demonstrates accessing instance attributes.
        """
        # We can access self.name because it was saved to the object in previous method calls.
        print("Accessing self.name from another method:", self.name)
        
        # We CANNOT access 'age' here because it was local to employeeDetails()
        # print(age) # This raises NameError

employeeOne = Employee()
employeeOne.employeeDetails()
employeeOne.printDetailsUnique()

"""
KEY TAKEAWAYS:
1. **`self`**: Always the first argument in instance methods. Python passes the object itself automatically.
2. **Instance Scope**: Variables like `self.name` live as long as the object lives.
3. **Local Scope**: Variables like `age` are destroyed when the method finishes.
"""
