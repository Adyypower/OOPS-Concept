"""
This module implements a **Library Management System**.

Demonstrates:
- **Encapsulation**: Classes (`Library`, `Customer`) managing their own data.
- **Interaction**: Objects interacting with each other (Customer requests book, Library lends it).
"""

class Library:
    """
    Manages the collection of books.
    """
    def __init__(self, ListBook):
        self.availableBooks = ListBook

    def displayAvailableBooks(self):
        """Lists all books currently in the library."""
        print("\nAvailable Books:")
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        """
        Lends a book if available, removing it from the list.
        """
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available in our library.")

    def addBook(self, returnedBook):
        """
        Accepts a returned book and adds it back to the list.
        """
        self.availableBooks.append(returnedBook)
        print("You have successfully returned the book.")

class Customer:
    """
    Represents a user of the library.
    """
    def requestBook(self):
        """Prompts user for a book name to borrow."""
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        """Prompts user for a book name to return."""
        self.book = input("Enter the name of the book you want to return: ")
        return self.book        

# Execution Logic
library = Library(["The Alchemist", "The Secret", "The Monk Who Sold His Ferrari"])
customer = Customer()

while True:
    print("\n1. Display available books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        library.displayAvailableBooks()
    elif choice == 2:
        library.lendBook(customer.requestBook())
    elif choice == 3:
        library.addBook(customer.returnBook())
    elif choice == 4:
        break
    else:
        print("Invalid choice!")