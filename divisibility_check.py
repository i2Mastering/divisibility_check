"""
Module for checking divisibility between two positive integers.

This script prompts the user to input two positive integers and determines whether the first number is evenly divisible by the second. 

Classes:
    - Main: A class that contains methods for user input and divisibility checking.

Methods:
    - user_prompt(): Collects two positive integers from the user.
    - division(): Checks whether the first integer is evenly divisible by the second.

Example Usage:
    $ python divisibility_check.py
    We are going to divide two positive numbers into each other...
    Please enter a positive integer for your first number: 10
    Please enter a positive integer for your second number: 5
    True

Author: Ike Iloegbu
License: MIT
"""

class Main:
    """
    A class to prompt user input and check divisibility between two integers.
    """
    
    def user_prompt(self):
        """
        Prompts the user to enter two positive integers.
        Ensures input validation for positive integers only.
        """
        print("We are going to divide two positive numbers into each other. Would they divide evenly, or will they not? That is the question!!")
        
        while True:
            try:
                self.a = int(input("Please enter a positive integer for your first number: "))
                if self.a > 0:
                    break
                else:
                    print("Incorrect value. Please enter a positive integer.")
            except ValueError:
                print("Oops! Wrong value.")

        while True:
            try:
                self.b = int(input("Please enter a positive integer for your second number: "))
                if self.b > 0:
                    break
                else:
                    print("Incorrect value. Please enter a positive integer.")
            except ValueError:
                print("Oops! Wrong value.")

    def division(self):
        """
        Determines whether the first number is evenly divisible by the second.
        
        Prints:
            True if evenly divisible, False otherwise.
        """
        print(self.a % self.b == 0)

if __name__ == "__main__":
    results = Main()
    results.user_prompt()
    results.division()
