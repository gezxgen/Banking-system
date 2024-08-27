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
    
    def deposit(self, n: str) -> None:
        try:
            self._balance += int(n)
        except ValueError:
            print("The entered deposit could not be converted into a number.")

    def withdraw(self, n: int) -> None:
        try:
            self._balance -= int(n)
        except ValueError:
            print("The entered withdraw could not be converted into a number.")
    
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


    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Password: {self.password}, Balance: {self.balance}."
    