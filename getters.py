# get the users option
def get_main() -> int:
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

def get_name(part: str) -> str:
    while True:
        name: str = input(f"Enter your {part} name: ")
        if validate(name, "n"):
            return name.strip().lower().capitalize()

def get_age() -> int:
    while True:
        age = input("Enter your age: ")
        if validate(age, "a"):
                return int(age)
        print("Entered age was not a number or smaller 0 or greater 120.")

def get_password() -> str:
    while True:
        password: str = input("Enter your password: ")
        if validate(password, "p"):
            return password

def get_balance() -> str:
     pass

def validate(dut: str, mode: str) -> bool:
     mode.lower()
     values = set(["n", "a", "p", "b", "d", "w"])
     
     if mode not in values:
          return "Wrong mode entered"
     
     match(mode):
          case "n":
               pass
          
          case "a":
               pass
          
          case "p":
               pass
          
          case "b":
               pass
          
          case "d":
               pass
          
          case "w":
               pass
          
