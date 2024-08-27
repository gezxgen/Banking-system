from sys import exit

# get the users option
def get_main() -> str:
    entry: str = ""
    values: set[str] = set(["0", "1", "2"])

    while entry not in values:
        print("0: Exit")
        print("1: Login")
        print("2: Create account")
        entry = input("Which action would you like to do? ")

    return int(entry)


def get_login() -> str:
    pass

def get_first() -> str:
    pass

def get_last() -> str:
    pass

def get_age() -> str:
    pass

def get_password() -> str:
    pass
