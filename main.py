import csv


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

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Password: {self.password}, Balance: {self.balance}."


def main():
    filename = "Accounts.csv"
    with open(filename) as file:
        users: list[int] = [0 for _ in range(sum(1 for line in file) - 1)]
    
    users.append(Account("Keivn", "Muster", "18", "Kevin123", "1000"))
    print(users[-1])


if __name__ == "__main__":
    main()
