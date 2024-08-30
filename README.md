# Bank Account Management System Documentation
---

## Table of Contents
1. [Overview](#overview)
2. [Main Module](#main-module)
   - [Function: `main()`](#function-main)
     - [Exit (case 0)](#function-main)
     - [Login (case 1)](#function-main)
       - [Exit (case 0)](#function-main)
       - [Deposit (case 1)](#function-main)
       - [Withdraw (case 2)](#function-main)
       - [Change Password (case 3)](#function-main)
       - [Change Owner (case 4)](#function-main)
       - [Log out (case 5)](#function-main)
     - [Create Account (case 2)](#function-main)
     - [View Accounts (case 3)](#function-main)
3. [Getters Module](#getters-module)
   - [Function: `get_main()`](#function-get_main)
   - [Function: `get_name()`](#function-get_namepart-str---str)
   - [Function: `get_age()`](#function-get_age---str)
   - [Function: `get_password()`](#function-get_password---str)
   - [Function: `get_balance()`](#function-get_balance---str)
   - [Function: `get_withdraw_deposit()`](#function-get_withdraw_depositstring-str---str)
   - [Function: `validate()`](#function-validatedut-str-mode-str---bool)
   - [Function: `validate_num()`](#function-validate_numn-str-number10000---bool)
   - [Function: `validate_user()`](#function-validate_userusername-str-user_password-str-users-listaccount---int)
   - [Function: `get_inner()`](#function-get_inner---int)
4. [Classes Module](#classes-module)
   - [Class: `Account`](#class-account)
   - [Method: `__init__`](#method-__init__self-first-str-last-str-age-str-password-str-balance-str---none)
   - [Property: `name`](#property-name)
   - [Property: `age`](#property-age)
   - [Property: `password`](#property-password)
   - [Property: `balance`](#property-balance)
   - [Method: `deposit()`](#method-depositself-n-str---none)
   - [Method: `withdraw()`](#method-withdrawself-n-str---none)
   - [Static Method: `get_accounts()`](#static-method-get_accountsfilename-str---listaccount)
   - [Static Method: `set_accounts()`](#static-method-set_accountsfilename-str-users-listaccount---none)
   - [Static Method: `print_accounts()`](#static-method-print_accountsaccounts-listaccount---none)
   - [Method: `__str__`](#method-__str__self---str)
5. [Summary](#summary)

---

## Overview

This documentation provides a detailed description of a simple bank account management system implemented in Python. The system allows users to create accounts, log in, deposit/withdraw funds, and manage account information. The project is divided into three main modules: `main`, `getters`, and `classes`.

## Main Module

The `main` module is the entry point of the application and contains the primary logic that manages user interaction and account operations.

### Function: `main()`
```python
def main():
    # init accounts
    new_account: list[int | str] = ["" for _ in range(5)]
    filename: str = "Accounts.csv"
    accounts: list["Account"] = Account.get_accounts(filename)
    user_index: int
    is_logged_in: bool
    entry: str
    amount: str
    user_name: str
    user_age: str
    entry_inner: int = 0

    # endless loop
    while True:
        entry: int = int(get_main())
        match entry:
            # Exit
            case 0:
                Account.set_accounts(filename, accounts)
                exit()

            # Login
            case 1:
                print("Entry the details to your account.")
                user_name = get_name("first") + " " + get_name("last")
                if user_index := validate_user(user_name, get_password(), accounts):
                    is_logged_in = True
                    print("Logged in successfully")
                else:
                    print("The entered user was not found in the database.")
                    is_logged_in = False
                if is_logged_in:
                    while entry_inner != 5:
                        entry_inner = get_inner()
                        match entry_inner:
                            # Exit
                            case 0:
                                Account.set_accounts(filename, accounts)
                                exit()

                            # Deposit
                            case 1:
                                amount = get_withdraw_deposit("deposit")
                                accounts[user_index].deposit(amount)
                                print(f"New account balance: {accounts[user_index].balance}")
                                print("Deposit was successful")

                            # Withdraw
                            case 2:
                                amount = get_withdraw_deposit("withdraw")
                                accounts[user_index].withdraw(amount)
                                print(f"New account balance: {accounts[user_index].balance}")
                                print("Withdraw was successful")

                            # Change password
                            case 3:
                                print("Make sure to enter the password correctly!")
                                accounts[user_index].password = get_password()
                                print("Password was set.")

                            # Change owner - no U18
                            case 4:
                                print("Fill out the questions with information about the future owner.")
                                user_name = get_name("first").capitalize() + " " + get_name("last").capitalize()
                                user_age = get_age()
                                if int(user_age) >= 18:
                                    accounts[user_index].age = user_age
                                    accounts[user_index].name = user_name
                                    print("New owner is set.")
                                else:
                                    print("The future owner is not yet 18 years old.")

                            # Log out
                            case 5:
                                is_logged_in = False

                            case _:
                                print("Invalid entry")

            # New account
            case 2:
                new_account[0] = get_name("first")
                new_account[1] = get_name("last")
                new_account[2] = get_age()
                new_account[3] = get_password()
                new_account[4] = get_balance()
                accounts.append(Account(new_account[0], new_account[1], new_account[2], new_account[3], new_account[4]))
                Account.set_accounts(filename, accounts)
                print("New account added.")

            # Print a list of all accounts
            case 3:
                Account.print_accounts(accounts)

            case _:
                print("Invalid entry")


if __name__ == "__main__":
    main()
```

- **Purpose**: Manages the main flow of the application, including user authentication, account creation, and account management.
- **Details**:
  - Initializes variables and loads existing account data from a CSV file.
  - Provides an infinite loop for continuous user interaction.
  - Handles user input through a menu-driven interface using a `match` statement.
  - Allows users to:
    - **Exit (case 0)**: Save account data and exit the program.
    - **Login (case 1)**: 
      - Log in to an existing account.
      - Once logged in, users can:
        - **Exit (case 0)**: Save account data and exit the program.
        - **Deposit (case 1)**: Deposit an amount into the account.
        - **Withdraw (case 2)**: Withdraw an amount from the account.
        - **Change Password (case 3)**: Update the account's password.
        - **Change Owner (case 4)**: Update the account's owner details if the new owner is over 18.
        - **Log out (case 5)**: Log out from the current account.
    - **Create Account (case 2)**: Create a new account and save it to the CSV file.
    - **View Accounts (case 3)**: Display a list of all existing accounts.

## Getters Module

The `getters` module contains various functions for gathering user input and validating that input.

### Function: `get_main()`
```python
def get_main() -> str:
    entry: str = ""
    values: set[str] = {"0", "1", "2", "3"}

    while entry not in values:
        print("0: Exit")
        print("1: Log in")
        print("2: Create account")
        print("3: View accounts")
        entry = input("Which action would you like to do? ")

    return entry
```
- **Purpose**: Displays the main menu and returns the user's choice.
- **Returns**: `str`: The user's menu choice.

### Function: `get_name(part: str) -> str`
```python
def get_name(part: str) -> str:
    while True:
        name: str = input(f"Enter your {part} name: ")
        if validate(name, "n"):
            return name.strip().lower().capitalize()
```
- **Purpose**: Prompts the user to enter either their first or last name.
- **Parameters**:
  - `part` (`str`): Specifies whether to ask for the "first" or "last" name.
- **Returns**: `str`: The validated and formatted name.

### Function: `get_age() -> str`
```python
def get_age() -> str:
    while True:
        age = input("Enter your age: ")
        if validate(age, "a"):
            return age
        print("Entered age was not a number or smaller 0 or greater 120.")
```
- **Purpose**: Prompts the user to enter their age and validates the input.
- **Returns**: `

str`: The validated age.

### Function: `get_password() -> str`
```python
def get_password() -> str:
    while True:
        password: str = input("Enter your password: ")
        if validate(password, "p"):
            return password
        print("Entered password did not contain lower, upper, numeric and special characters.")
        print("Entered password was not longer than 8 characters.")
```
- **Purpose**: Prompts the user to enter their password and validates the input.
- **Returns**: `str`: The validated password.

### Function: `get_balance() -> str`
```python
def get_balance() -> str:
    while True:
        balance: str = input("Enter the initial balance: ")
        if validate(balance, "b"):
            return balance
        print("Entered balance was not a number or smaller 0 or greater 10000.")
```
- **Purpose**: Prompts the user to enter the initial balance for their account and validates the input.
- **Returns**: `str`: The validated balance.

### Function: `get_withdraw_deposit(string: str) -> str`
```python
def get_withdraw_deposit(string: str) -> str:
    while True:
        amount = input(f"Enter the amount to {string}: ")
        if validate(amount, string[0]):
            return amount
```
- **Purpose**: Prompts the user to enter an amount to deposit or withdraw and validates the input.
- **Parameters**:
  - `string` (`str`): Specifies the operation, either "deposit" or "withdraw".
- **Returns**: `str`: The validated amount.

### Function: `validate(dut: str, mode: str) -> bool`
```python
def validate(dut: str, mode: str) -> bool:
    mode.lower()
    dut_int: int = 0
    values = {"n", "a", "p", "b", "d", "w"}

    if mode not in values:
        return False

    match mode:
        case "n":
            dut.strip()
            if dut and len(dut) < 100:
                return True

        case "a":
            try:
                dut_int = int(dut)
            except ValueError:
                return False
            if 0 <= dut_int <= 120:
                return True

        case "p":
            results: list[bool] = [False for _ in range(4)]
            for char in dut:
                if char.islower():
                    results[0] = True
                elif char.isupper():
                    results[1] = True
                elif char.isnumeric():
                    results[2] = True
                else:
                    results[3] = True

            for result in results:
                if result:
                    dut_int += 1
                if dut_int == 4 and len(dut) >= 8:
                    return True

        case "b":
            if validate_num(dut):
                return True

        case "d":
            if validate_num(dut):
                return True

        case "w":
            if validate_num(dut):
                return True

        case _:
            return False

    return False
```
- **Purpose**: Validates different types of user input based on the mode provided.
- **Parameters**:
  - `dut` (`str`): The input to validate.
  - `mode` (`str`): The type of input to validate (e.g., name, age, password).
- **Returns**: `bool`: Whether the input is valid.

### Function: `validate_num(n: str, number=10000) -> bool`
```python
def validate_num(n: str, number=10000) -> bool:
    try:
        num: int = int(n)
    except ValueError:
        return False
    if 0 <= num <= number:
        return True
    else:
        return False
```
- **Purpose**: Validates if a string is a number within a specified range.
- **Parameters**:
  - `n` (`str`): The string to validate as a number.
  - `number` (`int`, optional): The maximum value allowed. Defaults to 10,000.
- **Returns**: `bool`: Whether the string is a valid number within the range.

### Function: `validate_user(username: str, user_password: str, users: list["Account"]) -> int`
```python
def validate_user(username: str, user_password: str, users: list["Account"]) -> int:
    for i, user in enumerate(users):
        if user.name == username and user.password == user_password:
            return i
    return 0
```
- **Purpose**: Validates user credentials against a list of accounts.
- **Parameters**:
  - `username` (`str`): The user's name.
  - `user_password` (`str`): The user's password.
  - `users` (`list["Account"]`): The list of existing accounts.
- **Returns**: `int`: The index of the user in the accounts list if valid, otherwise `0`.

### Function: `get_inner() -> int`
```python
def get_inner() -> int:
    entry: str = ""
    values: set[str] = {"0", "1", "2", "3", "4", "5"}

    while entry not in values:
        print("0: Exit")
        print("1: Deposit")
        print("2: Withdraw")
        print("3: Change password")
        print("4: Change owner")  # change username & age
        print("5: Log out")
        entry = input("Which action would you like to do? ")

    return int(entry)
```
- **Purpose**: Displays a submenu for logged-in users and returns their choice.
- **Returns**: `int`: The user's submenu choice.

## Classes Module

The `classes` module defines the `Account` class, which is the blueprint for creating and managing bank accounts.

### Class: `Account`
```python
class Account:
    ...
```
- **Purpose**: Represents a bank account with attributes like name, age, password, and balance.

### Method: `__init__(self, first: str, last: str, age: str, password: str, balance: str) -> None`
```python
def __init__(self, first: str, last: str, age: str, password: str, balance: str) -> None:
    self._name = f"{first} {last}"
    self._age = age
    self._password = password
    self._balance = balance
```
- **Purpose**: Initializes a new account with the provided details.

### Property: `name`
```python
@property
def name(self) -> str:
    return self._name

@name.setter
def name(self, name: str) -> None:
    from getters import validate
    name.capitalize()
    if validate(name, "n"):
        self._name = name.strip().lower().capitalize()
```
- **Purpose**: Gets or sets the account holder's name.

### Property: `age`
```python
@property
def age(self) -> int:
    return int(self._age)

@age.setter
def age(self, new_age: str) -> None:
    from getters import validate
    if validate(new_age, "a"):
        self._age = int(new_age)
```
- **Purpose**: Gets or sets the account holder's age.

### Property: `password`
```python
@property
def password(self) -> str:
    return self._password

@password.setter
def password(self, value: str) -> None:
    self._password = value.strip()
```
- **Purpose**: Gets or sets the account password.

### Property: `balance`
```python
@property
def password(self) -> str:
    return self._password

@password.setter
def password(self, new_password: str) -> None:
    from getters import validate
    if validate(new_password, "p"):
        self._password = new_password
```
- **Purpose**: Gets or sets the account balance.

### Method: `deposit(self, n: str) -> None`
```python
def deposit(self, n: str) -> None:
    from getters import validate
    if validate(n, "d"):
        self._balance = str(int(self._balance) + int(n))
        return
    print("Entered deposit was not a number or smaller 0 or greater 10000.")
```
- **Purpose**: Deposits a specified amount into the account.

### Method: `withdraw(self, n: str) -> None`
```python
def withdraw(self, n: str) -> None:
    from getters import validate
    if validate(n, "w"):
        self._balance = str(int(self._balance) - int(n))
        return
    print("Entered withdraw was not a number or smaller 0 or greater 10000.")
```
- **Purpose**: Withdraws a specified amount from the account.

### Static Method: `get_accounts(filename: str) -> list["Account"]`
```python
@staticmethod
def get_accounts(filename: str) -> list["Account"]:
    with open(filename) as file:
        reader = DictReader(file)
        users: list["Account"] = []

        for row in reader:
            users.append(Account(row["first"], row["last"], row["age"], row["password"], row["balance"]))
    return users
```
- **Purpose**: Reads account data from a CSV file and returns a list of `Account` objects.

### Static Method: `set_accounts(filename: str, users: list["Account"]) -> None`
```python
@staticmethod
def set_accounts(filename: str, users: list["Account"]) -> None:
    with open(filename, "w", newline="") as file:
        writer = DictWriter(file, fieldnames=["first", "last", "age", "password", "balance"])

        writer.writeheader()
        for user in users:
            writer.writerow({"first": user.name.split(" ")[0],
                             "last": user.name.split(" ")[-1],
                             "age": user.age,
                             "password": user.password,
                             "balance": user.balance})
```
- **Purpose**: Saves account data to a CSV file.

### Static Method: `print_accounts(accounts: list["Account"]) -> None`
```python
@staticmethod
def print_accounts(users: list["Account"]) -> None:
    for user in users:
        print(f"Name: {user.name:<20} Age: {user.age}")
```
- **Purpose**: Prints the details of all accounts.

### Method: `__str__(self) -> str`
```python
def __str__(self) -> str:
    return f"Name: {self.name}, Age: {self.age}, Password: {self.password}, Balance: {self.balance}."
```
- **Purpose**: Returns a string representation of the account.

## Summary

This Bank Account Management System provides a user-friendly interface for managing bank accounts, including features for logging in, creating new accounts, depositing and withdrawing funds, changing account details, and viewing account information. The system is built with modular components to ensure clarity, ease of use, and maintainability.

--- 
