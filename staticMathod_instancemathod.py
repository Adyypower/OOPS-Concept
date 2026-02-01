"""
This module explains **Instance Methods** and **Static Methods**.
"""

class Employee:

    def employeedetails(self):
        """
        **Instance Method**:
        - Inherently receives the object instance as the first argument (`self`).
        - Can modify object state (create/change instance attributes).
        """
        self.name = "Aditya"
        self.age = 12
        print(f"Instance Method: Name={self.name}, Age={self.age}")

    @staticmethod
    def employeeStaticMethod():
        """
        **Static Method**:
        - Decorated with `@staticmethod`.
        - Does NOT receive `self` or `cls`.
        - Behaves like a normal function but belongs to the class namespace.
        - Cannot modify object state directly.
        """
        print("This is a static method (no self access)")

employeeOne = Employee()
employeeOne.employeedetails()      # Calls with self
employeeOne.employeeStaticMethod() # Calls without self (works on instance too)
Employee.employeeStaticMethod()    # Can also call directly on Class