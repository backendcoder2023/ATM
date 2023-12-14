class BankAccount:
    def __init__(self):
        self.language_choice = None
        self.account_choice = None
        self.amount = 0
        self.pin = 0

    def welcome_message(self):
        print("Welcome")

    def get_language_choice(self):
        print("Enter Your Account Number")
        print("Language Options:")
        print("1. Marathi")
        print("2. Hindi")
        print("3. English")
        self.language_choice = int(input("Enter the number for your language choice: "))

    def get_account_choice(self):
        print("\nAccount Type Options:")
        print("1. Saving")
        print("2. Debit")
        print("3. Withdraw")
        print("4. Deposit")
        self.account_choice = int(input("Enter the number for your account type choice: "))

    def get_input(self):
        self.amount = int(input("Enter the amount: "))
        self.pin = int(input("Enter your PIN: "))
        confirm_pin = int(input("Confirm your PIN: "))

        if self.pin != confirm_pin:
            print("Wrong PIN")
        else:
            self.process_transaction()

    def process_transaction(self):
        language_options = {1: 'Marathi', 2: 'Hindi', 3: 'English'}
        account_options = {1: 'Saving', 2: 'Debit', 3: 'Withdraw', 4: 'Deposit'}

        selected_language = language_options.get(self.language_choice, 'Unknown')
        selected_account = account_options.get(self.account_choice, 'Unknown')

        if self.amount <= 15000:
            print("Entered amount:", self.amount)
            print("Current balance:", 15000 - self.amount)
        else:
            print("Oops, not enough money")

        print(f"Your money in {selected_language} account of type {selected_account}")
        print("Thank you for visiting us")

if __name__ == "__main__":
    account = BankAccount()
    account.welcome_message()
    account.get_language_choice()
    account.get_account_choice()
    account.get_input()
