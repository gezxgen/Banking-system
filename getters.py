from classes import *


# get the users option
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


def get_name(part: str) -> str:
    while True:
        name: str = input(f"Enter your {part} name: ")
        if validate(name, "n"):
            return name.strip().lower().capitalize()


def get_age() -> str:
    while True:
        age = input("Enter your age: ")
        if validate(age, "a"):
            return age
        print("Entered age was not a number or smaller 0 or greater 120.")


def get_password() -> str:
    while True:
        password: str = input("Enter your password: ")
        if validate(password, "p"):
            return password
        print("Entered password did not contain lower, upper, numeric and special characters.")
        print("Entered password was not longer than 8 characters.")


def get_balance() -> str:
    while True:
        balance: str = input("Enter the initial balance: ")
        if validate(balance, "b"):
            return balance
        print("Entered balance was not a number or smaller 0 or greater 10000.")


def get_withdraw_deposit(string: str) -> str:
    while True:
        amount = input(f"Enter the amount to {string}: ")
        if validate(amount, string[0]):
            return amount


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


def validate_num(n: str, number=10000) -> bool:
    try:
        num: int = int(n)
    except ValueError:
        return False
    if 0 <= num <= number:
        return True
    else:
        return False


def validate_user(username: str, user_password: str, users: list["Account"]) -> int:
    for i, user in enumerate(users):
        if user.name == username and user.password == user_password:
            return i
    return 0


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
