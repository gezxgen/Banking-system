from csv import DictReader, DictWriter


# Class blueprint for an account
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
        from getters import validate
        name.capitalize()
        if validate(name, "n"):
            self._name = name.strip().lower().capitalize()

    @property
    def age(self) -> int:
        return int(self._age)
    
    @age.setter
    def age(self, new_age: str) -> None:
        from getters import validate
        if validate(new_age, "a"):
            self._age = int(new_age)

    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, new_password: str) -> None:
        from getters import validate
        if validate(new_password, "p"):
            self._password = new_password

    @property
    def balance(self) -> int:
        return int(self._balance)
    
    @balance.setter
    def balance(self, new_balance: str):
        from getters import validate
        if validate(new_balance, "b"):
            self._balance = int(new_balance)
    
    def deposit(self, n: str) -> None:
        from getters import validate
        if validate(n, "d"):
            self._balance = str(int(self._balance) + int(n))
            return
        print("Entered deposit was not a number or smaller 0 or greater 10000.")

    def withdraw(self, n: str) -> None:
        from getters import validate
        if validate(n, "w"):
            self._balance = str(int(self._balance) - int(n))
            return
        print("Entered withdraw was not a number or smaller 0 or greater 10000.")
    
    @staticmethod
    def get_accounts(filename: str) -> list["Account"]:
        with open(filename) as file:
            reader = DictReader(file)
            users: list["Account"] = []

            for row in reader:
                users.append(Account(row["first"], row["last"], row["age"], row["password"], row["balance"]))
        return users

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

    @staticmethod
    def print_accounts(users: list["Account"]) -> None:
        for user in users:
            print(f"Name: {user.name:<20} Age: {user.age}")

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Password: {self.password}, Balance: {self.balance}."
    