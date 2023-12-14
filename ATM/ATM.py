print("Welcome")
print("Enter Your Account Number")

print("Language Options:")
print("1. Marathi")
print("2. Hindi")
print("3. English")
language_choice = int(input("Enter the number for your language choice: "))

print("\nAccount Type Options:")
print("1. Saving")
print("2. Debit")
print("3. Withdraw")
print("4. Deposit")
account_choice = int(input("Enter the number for your account type choice: "))

C = int(input("Enter the amount: "))
D = int(input("Enter your PIN: "))
E = int(input("Confirm your PIN: "))

if language_choice == 1:
    A = 'Marathi'
elif language_choice == 2:
    A = 'Hindi'
elif language_choice == 3:
    A = 'English'
else:
    A = 'Unknown'

if account_choice == 1:
    B = 'Saving'
elif account_choice == 2:
    B = 'Debit'
elif account_choice == 3:
    B = 'Withdraw'
elif account_choice == 4:
    B = 'Deposit'
else:
    B = 'Unknown'

if D == E:
    print("Your money")
else:
    print("Wrong PIN")

if C <= 15000:
    print("Entered amount:", C)
    print("Current balance:", 15000 - C)
else:
    print("Oops, not enough money")

print("Thank you for visiting us")