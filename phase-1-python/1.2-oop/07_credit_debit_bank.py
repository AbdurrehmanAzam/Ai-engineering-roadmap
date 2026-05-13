class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self):
        yes_no = input(
            f"Your initial Balance is {self.balance}\nDo you want to withdraw amount? if yes then enter yes\n"
        )
        if yes_no == "yes":
            withdraw = int(input("Please enter the amount you want to withdraw = "))
            self.balance = self.balance - withdraw
            print(f"Your account {self.account_no} have balance of = {self.balance} ")

    def credit(self):
        yes_no = input(
            f"Your initial Balance is {self.balance}\nDo you want to add amount? if yes then enter yes\n"
        )
        if yes_no == "yes":
            Add = int(
                input("Please enter the amount you want to add to your account = ")
            )
            self.balance = self.balance + Add
            print(
                f"Your account no {self.account_no} have balance of = {self.balance} "
            )


a1 = Account(1000, 1928)
choice = int(
    input(
        "If you want to add balance to your account press 1 and if you want to withdraw balance from your account press 2 = "
    )
)
if choice == 1:
    a1.credit()
elif choice == 2:
    a1.debit()
else:
    print("Invalid number select 1 or 2 and try again")
