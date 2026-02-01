"""
This module implements a Savings Account system using OOP principles.
It builds upon the abstract `Account` class and provides a concrete implementation.

Key Concepts:
- **Inheritance**: `SavingsAccount` inherits from `Account`.
- **Method Implementation**: It defines the logic for all abstract methods.
- **Dictionary for Storage**: Simulates a database using a dictionary `self.savingsAccounts`.
"""

from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
    """
    Abstract Base Class for an Account.
    Defines the contract that all account types must follow.
    """
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayBalance():
        return 0


class SavingsAccount(Account):
    """
    Concrete implementation of a Savings Account.
    """
    def __init__(self):
        """
        Initializes the SavingsAccount system.
        self.savingsAccounts is a dictionary:
        Key: Account Number (int)
        Value: List [Name (str), Balance (int)]
        """
        # [key][0] => name ; [key][1] => balance
        self.savingsAccounts = {}

    def createAccount(self, name, initialDeposit):
        """Creates a new savings account with a unique 5-digit number."""
        print()
        self.accountNumber = randint(10000, 99999)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        print("Account creation has been successful. Your account number is ", self.accountNumber)
        print()

    def authenticate(self, name, accountNumber):
        """
        Authenticates a user based on name and account number.
        Returns True if successful, False otherwise.
        """
        print()
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][0] == name:
                print("Authentication Successful")
                self.accountNumber = accountNumber
                print()
                return True
            else:
                print("Authentication Failed")
                print()
                return False
        else:
            print("Authentication Failed")
            print()
            return False

    def withdraw(self, withdrawalAmount):
        """Withdraws amount if sufficient balance exists."""
        print()
        if withdrawalAmount > self.savingsAccounts[self.accountNumber][1]:
            print("Insufficient balance")
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawalAmount
            print("Withdrawal was successful.")
            self.displayBalance()
        print()

    def deposit(self, depositAmount):
        """Deposits amount into the current account."""
        print()
        self.savingsAccounts[self.accountNumber][1] += depositAmount
        print("Deposit was successful.")
        self.displayBalance()
        print()

    def displayBalance(self):
        """Displays the current balance."""
        print("Avaialble balance: ",self.savingsAccounts[self.accountNumber][1])

savingsAccount = SavingsAccount()
while True:
    print()
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    userChoice = int(input())
    print()
    # FIXED: Replaced 'is' with '==' for value comparison
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
        authenticationStatus = savingsAccount.authenticate(name, accountNumber)
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
                    savingsAccount.withdraw(withdrawalAmount)
                    print()
                elif userChoice == 2:
                    print()
                    print("Enter an amount to be deposited")
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                    print()
                elif userChoice == 3:
                    print()
                    savingsAccount.displayBalance()
                    print()
                elif userChoice == 4:
                    break
    elif userChoice == 3:
        quit()
