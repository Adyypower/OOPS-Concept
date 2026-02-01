# OOP Concepts in Python

Welcome to my **OOP Concepts** repository! This project contains clear, executable examples of Object-Oriented Programming (OOP) principles in Python.

## 📂 Project Structure
This repository relies on practical examples to teach concepts:

### 1. Basic Concepts
- **[Class_and_object.py](./Class_and_object.py)**: Introduction to Classes (Blueprints) and Objects (Instances).
- **[Self_understanding.py](./Self_understanding.py)**: Deep dive into the `self` keyword and variable scope (Local vs Instance attributes).
- **[init()Method.py](./init()Method.py)**: Understanding Constructors (`__init__`) for initializing objects.

### 2. Attributes & Methods
- **[classAttribute_instanceAtribute.py](./classAttribute_instanceAtribute.py)**:
    - **Class Attributes**: Shared by all instances.
    - **Instance Attributes**: Unique to each object.
- **[staticMathod_instancemathod.py](./staticMathod_instancemathod.py)**:
    - **Instance Methods**: Can modify object state (`self`).
    - **Static Methods**: Utility functions belonging to the class (`@staticmethod`).

### 3. Inheritance
How classes derive behavior from other classes.
- **[singleInheritance.py](./singleInheritance.py)**: One Child inherits from one Parent.
- **[multipleInheritance.py](./multipleInheritance.py)**: One Child inherits from **multiple** Parents.
- **[multiLevelInheritance.py](./multiLevelInheritance.py)**: Grandparent -> Parent -> Child chain.
- **[daimond.py](./daimond.py)**: The **Diamond Problem** and Method Resolution Order (MRO) in multiple inheritance.

### 4. Polymorphism
"Many Forms" - Methods behaving differently based on context.
- **[overloading.py](./overloading.py)**: **Operator Overloading**. changing how `+` or `-` works for custom objects using magic methods (`__add__`, `__sub__`).
- **[overriding.py](./overriding.py)**: **Method Overriding**. Child class providing a specific implementation of a Parent method.

### 5. Encapsulation & Abstraction
- **[accesSpecifiers.py](./accesSpecifiers.py)**: Public, Protected (`_`), and Private (`__`) members.
- **[Banking.py](./Banking.py) & [BankingSystem.py](./BankingSystem.py)**: A complete **Banking System** demonstrating:
    - **Abstract Base Classes (ABC)**: Enforcing an interface.
    - **Encapsulation**: Hiding implementation details.
    - **Data Persistence**: Using dictionaries to manage account state.

### 6. Projects & Exercises
- **[library.py](./library.py)**: A Library Management System where Customers and Library objects interact.
- **[exercise1.py](./exercise1.py)**: Furniture inheritance example.
- **[exercise2.py](./exercise2.py)**: Square class with power operator overloading.

## 🚀 How to Run
You can run any file directly using Python:
```bash
python Banking.py
python library.py
```

## 📝 Notes
- **Encapsulation** in Python is not strict. "Private" variables are hidden using name mangling but can still be accessed if you try hard enough.
- **Polymorphism** in Python is implicit (Duck Typing) but can be enforced via Inheritance.
- **Self** is explicitly passed as the first argument to instance methods, unlike `this` in Java/C++.

---
*Created by Adyypower*
