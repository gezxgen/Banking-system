from getters import *
from classes import *


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
