"""
This module demonstrates a basic Banking System using Object-Oriented Programming in Python.
It illustrates:
1.  **Abstraction**: Using Abstract Base Classes (ABC) to define an interface (`Account`).
2.  **Encapsulation**: Using a class (`BankAccount`) to bundle data (account details) and methods together.
3.  **State Management**: Using a dictionary to store multiple accounts.
"""

from random import randint
from abc import ABCMeta, abstractclassmethod

class Account(metaclass=ABCMeta):
    """
    Abstract Base Class defining the interface for a bank account.
    Classes inheriting from this MUST implement all abstract methods.
    """
    @abstractclassmethod
    def createAccount(self):
        """Abstract method to create a new account."""
        return 0

    @abstractclassmethod
    def authenticate(self):
        """Abstract method to verify user credentials."""
        return 0

    @abstractclassmethod
    def withdraw(self):
        """Abstract method to withdraw funds."""
        return 0

    @abstractclassmethod
    def deposit(self):
        """Abstract method to deposit funds."""
        return 0

    @abstractclassmethod
    def displayBalance(self):
        """Abstract method to show current balance."""
        return 0

class BankAccount(Account):
    """
    Concrete implementation of a Bank Account.
    Manages multiple accounts using a dictionary.
    """
    def __init__(self):
        """
        Initialize the BankAccount system.
        
        Attributes:
            savingAccount (dict): Stores account data. Key: Account Number, Value: [Name, Balance]
        """
        # FIXED: savingAccount was a local variable, making it inaccessible in other methods.
        # Changed to self.savingAccount to make it an instance attribute.
        self.savingAccount = {}

    def createAccount(self, name, startingDeposit):
        """
        Creates a new account with a random account number.
        
        Args:
            name (str): The name of the account holder.
            startingDeposit (int): The initial amount to deposit.
        """
        self.accountnumber = randint(10000, 99999)
        self.name = name
        self.startingDeposit = startingDeposit
        # FIXED: Accessing self.savingAccount instance attribute
        self.savingAccount[self.accountnumber] = [self.name, self.startingDeposit]

        print("Account created successfully")
        print("Account number is : ", self.accountnumber)
        print("Name is : ", self.name)
        print("Starting deposit is : ", self.startingDeposit)

    def authenticate(self, accountnumber, name):
        """
        Verifies if the account exists and the name matches.
        
        Args:
            accountnumber (int): The account number to verify.
            name (str): The name to match against the account.
            
        Returns:
            bool: True if authentication succeeds, False otherwise.
        """
        # FIXED: Accessing self.savingAccount
        if accountnumber in self.savingAccount.keys():
            if self.savingAccount[accountnumber][0] == name:
                print("Authentication is succesfull")
                return True # Added return for logic flow often used in these systems
            else:
                print("Authentication is failed")
                return False
        else:
            print("Authentication is failed")
            return False

    def withdraw(self, accountnumber, withdrawalAmount):
        """
        Withdraws money from a specific account.
        
        Args:
            accountnumber (int): The account to withdraw from.
            withdrawalAmount (int): The amount to withdraw.
        """
        # FIXED: Accessing self.savingAccount
        if withdrawalAmount > self.savingAccount[accountnumber][1]:
            print("Insufficient balance")
        else:
            self.savingAccount[accountnumber][1] -= withdrawalAmount
            print("Withdrawal was successful.")
            self.displayBalance(accountnumber)

    def deposit(self, accountnumber, depositAmount):
        """
        Deposits money into a specific account.
        
        Args:
            accountnumber (int): The account to deposit into.
            depositAmount (int): The amount to deposit.
        """
        # FIXED: Accessing self.savingAccount
        self.savingAccount[accountnumber][1] += depositAmount
        print("Deposit was successful.")
        self.displayBalance(accountnumber)

    def displayBalance(self, accountnumber):
        """
        Prints the current balance of the specified account.
        
        Args:
            accountnumber (int): The account to check.
        """
        # FIXED: Accessing self.savingAccount
        print("Available balance is : ", self.savingAccount[accountnumber][1])


savingsAccount = BankAccount() # Create instance of the concrete class

print("Enter 1 to create a new account")
print("Enter 2 to access an existing account")
print("Enter 3 to exit")
userChoice = int(input())
print()

# FIXED: Replaced 'is' with '==' for literal comparison (SyntaxWarning fix)
if userChoice == 1:
    print()
    print("Enter your name: ")
    name = input()
    print("Enter the initial deposit: ")
    deposit = int(input())
    savingsAccount.createAccount(name, deposit)
    print()
elif userChoice == 2:
    print()
    print("Enter your name: ")
    name = input()
    print("Enter your account number: ")
    accountNumber = int(input())
    
    # Note: The original code didn't return True/False from authenticate, 
    # but the logic below expects a "True" flow or implied success.
    # We added return values to authenticate() method to support this.
    authenticationStatus = savingsAccount.authenticate(accountNumber, name)
    print()
    
    if authenticationStatus is True:
        while True:
            print()
            print("Enter 1 to withdraw")
            print("Enter 2 to deposit")
            print("Enter 3 to display avialable balance")
            print("Enter 4 to go back to the previous menu")
            userChoice = int(input())
            print()
            # FIXED: Replaced 'is' with '=='
            if userChoice == 1:
                print()
                print("Enter a withdrawal amount")
                withdrawalAmount = int(input())
                savingsAccount.withdraw(accountNumber, withdrawalAmount)
                print()
            elif userChoice == 2:
                print()
                print("Enter an amount to be deposited")
                depositAmount = int(input())
                savingsAccount.deposit(accountNumber, depositAmount)
                print()
            elif userChoice == 3:
                print()
                savingsAccount.displayBalance(accountNumber)
                print()
            elif userChoice == 4:
                break
elif userChoice == 3:
    quit()