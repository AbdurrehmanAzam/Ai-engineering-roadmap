class BankAccount:
    bank_name = "Mezaan Bank"

    def __init__(self, account_number, account_holder_name, currency, account_balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.currency = currency
        self.account_balance = account_balance

    def show_account_balance(self):
        print("your current bank balance is")
        return self.account_balance


b1 = BankAccount(1101087, "Abdurrehman", "PKR", 100000)
b2 = BankAccount(2332123, "Bruce", "USD", 50000)
print(
    f"The account holder name is '{b1.account_holder_name}' using currency in '{b1.currency}'\nhis/her account id is : '{b1.account_number}' from '{BankAccount.bank_name}'\n"
)
print(
    f"The account holder name is '{b2.account_holder_name}' using currency in '{b2.currency}'\nhis/her account id is : '{b2.account_number}' from '{BankAccount.bank_name}'\n"
)
yes_or_no = input("Enter YES if you want your account balance to be showen = ")
if yes_or_no == "YES":
    print(b1.show_account_balance())
