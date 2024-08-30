from getters import *
from classes import Account


def main():
    # init accounts
    new_account: list[int | str] = ["" for _ in range(5)]
    filename: str = "Accounts.csv"
    accounts: list["Account"] = Account.get_accounts(filename)
    username: str = ""
    userpassword: str = ""
    userindex: int = 0
    is_logged_in: bool = False
    entry: str = ""
    entry_inner: str = ""

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
                username = get_name("first") + " " + get_name("last")
                userpassword = get_password()
                if userindex := validate_user(username, userpassword, accounts):
                    is_logged_in = True
                    print("Logged in successfully")
                else:
                    print("The entered user was not found in the database.")
                    is_logged_in = False

                if is_logged_in:
                    entry_inner = get_inner()
                    pass


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


if __name__ == "__main__":
    main()
