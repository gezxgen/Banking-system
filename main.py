from sys    import exit
from csv    import DictReader, DictWriter


class Account:
    def __init__(self, first: str, last: str, age: str, password: str, balance: str) -> None:
        self._name = f"{first} {last}"
        self._age = age
        self._password = password
        self._balance = balance
    
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if name.strip() != "":
            self._name = name.strip()
        else:
            print("The entered first or last name is empty.")

    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, new_age: str) -> None:
        try:
            self._age = int(new_age)
        except ValueError:
            print("The entered age could not be converted into a number.")

    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, new_password: str) -> None:
        if new_password != "":
            self._password = new_password
        else:
            print("The entered password is empty.")

    @property
    def balance(self) -> int:
        return self._balance
    
    @balance.setter
    def balance(self, new_balance: str):
        try:
            self._balance = int(new_balance)
        except ValueError:
            print("The entered age could not be converted into a number.")
    
    @staticmethod
    def get_accounts(filename: str) -> list["Account"]:
        with open(filename) as file:
            reader = DictReader(file)
            users: list["Account"] = []

            for row in reader:
                users.append(Account(row["first"], row["last"], row["age"], row["password"], row["balance"]))

        users.append(Account("Keivn", "Muster", "18", "Kevin123", "1000"))
        return users

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Password: {self.password}, Balance: {self.balance}."


def get_main() -> str:
    entry: str = ""
    values: set[str] = set(["0", "1", "2"])

    while entry not in values:
        print("0: Exit")
        print("1: Login")
        print("2: Create account")
        entry = input("Which action would you like to do? ")
    
    if entry == "0":
        exit()
    
    return int(entry)


def get_login() -> str:
    pass


def main():
    # init accounts
    entry: str = ""
    new_account: list[int | str] = ["" for _ in range(3)]
    filename: str = "Accounts.csv"
    accounts: list["Account"] = Account.get_accounts(filename)

    while True:
        entry = get_main()
        match(entry):
            case 1:
                print("Not made yet...")
            case 2:
                new_account[0] = get_first()
                new_account[1] = get_last()
                new_account[2] = get_age()
                new_account[3] = get_password()
                print("New account added.")
                accounts.append(Account(new_account[0], new_account[1], new_account[2], new_account[3], "0"))


if __name__ == "__main__":
    main()
