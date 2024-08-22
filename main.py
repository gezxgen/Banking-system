from getters    import *
from classes    import Account


def main():
    # init accounts
    entry: str = ""
    new_account: list[int | str] = ["" for _ in range(3)]
    filename: str = "Accounts.csv"
    accounts: list["Account"] = Account.get_accounts(filename)

    # endless loop
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
                accounts.append(Account(new_account[0], new_account[1], new_account[2], new_account[3], "0"))
                print("New account added.")
                

if __name__ == "__main__":
    main()
