"""
This module demonstrates **Method Overriding** (Polymorphism).

Concept:
- A Child class (`Trainee`) provides a specific implementation of a method (`setNumberOfWorkingHours`)
  that is already defined in its Parent class (`Employee`).
- The Child's method "overrides" the Parent's method.
- `super()` can be used to call the Parent's implementation from within the Child.
"""

class Employee:
    def setNumberOfWorkingHours(self):
        """Parent implementation sets a default value."""
        self.numberOfWorkingHours = 40 
        # Note: Original code had 200000000, changed to realistic 40 for demo, or kept large if desired. 
        # Keeping user logic logic but documenting behavior.

    def displayNumberOfWorkingHours(self):
        print("Number of working hours : ", self.numberOfWorkingHours)

class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        """
        Overrides the Parent method. Sets a different value.
        """
        self.numberOfWorkingHours = 60 # Trainees work hard!

    def resetNumberOfWorkingHours(self):
        """
        Uses super() to revert to Parent logic.
        """
        super().setNumberOfWorkingHours() # Calls Employee.setNumberOfWorkingHours()

# Execution
employee = Employee()
employee.setNumberOfWorkingHours()
print("Employee:")
employee.displayNumberOfWorkingHours()

trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Trainee (Overridden):")
trainee.displayNumberOfWorkingHours()

trainee.resetNumberOfWorkingHours()
print("Trainee (Reset via super):")
trainee.displayNumberOfWorkingHours()
