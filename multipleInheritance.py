"""
This module demonstrates **Multiple Inheritance**.

Concept:
- A Child class (`MacBook`) inherits from **multiple** Parent classes (`OP`, `Apple`).
- It has access to attributes and methods of ALL parent classes.
"""

class OP:
    """Parent Class 1: Operating System info"""
    multipleTasking = True

class Apple:
    """Parent Class 2: Brand info"""
    website = "www.Apple.com"

class MacBook(OP, Apple):
    """
    Child Class inheriting from BOTH OP and Apple.
    """
    def __init__(self):
        # Accessing attribute from Parent 1 (OP)
        if self.multipleTasking == True:
            print("MacBook supports multitasking")
        else:
            print("MacBook does not support multitasking")
            
        # Accessing attribute from Parent 2 (Apple)
        print("Website : ", self.website)    

# Execution
myMac = MacBook()