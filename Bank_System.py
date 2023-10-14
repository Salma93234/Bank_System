class Bank:
    def __init__(self):
        self.users = []
        self.admins = []
        self.loan_system = True
        self.total_balance = 0
        self.total_loan_amount = 0

    def user_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)
        return user

    def admin_account(self):
        admin = Admin()
        self.admins.append(admin)
        return admin

class User:
    account_number_counter = 100

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = User.account_number_counter
        User.account_number_counter += 1
        self.transaction_history = []
        self.loan_taken = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            return "Withdraw amount exceeded"
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")

    def check_balance(self):
        return f"Available Balance: {self.balance}"

    def check_history(self):
        return self.transaction_history

    # def take_loan(self, amount):
    #     if self.loan_taken < 2:
    #         self.balance += amount
    #         return f"Loan of {amount} taken successfully"
    
    #     else:
    #       return "You can't take more than two loans"

    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.balance += amount
            self.loan_taken += 1
            Bank.total_loan_amount += amount
            return f"Loan of {amount} taken successfully"
        else:
            return "You can't take more than two times"

    def transfer_amount(self, replace, amount):
        if replace in Bank.users:
            if amount <= self.balance:
                self.balance -= amount
                replace.balance += amount
                return f"${amount} transferred to {replace.name} successfully"
            else:
                return "funds for transfer"
        else:
            return "Account does not exist"

class Admin:
    def delete_user_account(self, user):
        Bank.users.remove(user)

    def all_user_accounts(self):
        return Bank.users

    def total_available_balance(self):
        total_balance = sum(user.balance for user in Bank.users)
        return f"Total Available Balance: {total_balance}"

    def total_loan_amount(self):
        return f"Total Loan Amount: {Bank.total_loan_amount}"

    def toggle_loan_feature(self):
        pass

    

# bank = Bank()
# user = bank.user_account("Rhaim", "Rhaim@mail.com", "123 Main St", "Savings")
# admin = bank.admin_account()

# while True:
#     print("\nMain Menu:")
#     print("1. User System")
#     print("2. Admin System")
#     print("3. Exit")

#     main_choice = input("Enter your choice: ")

#     if main_choice == '1':
#         if current_user is None:
#             print("\n--> No user logged in!")
#             ch = input("\n--> Register/Login (R/L) : ")
#             if ch == "R":
#                 name = input("Name:")
#                 email = input("Email:")
#                 address = input("Address:")
#                 account_type = input("Account Type (Savings/Current): ")
#                 current_user = bank.create_user_account(name, email, address, account_type)
#                 print(f"User account created successfully. Account number: {current_user.account_number}")
#             elif ch == "L":
#                 account_number = int(input("Enter account number: "))
#                 current_user = bank.get_user(account_number)
#                 if current_user:
#                     print(f"Logged in as {current_user.name}.")
#                 else:
#                     print("User not found.")
#         else:
#             print("\nUser System:")
#             print("1. Deposit")
#             print("2. Withdraw")
#             print("3. Check Balance")
#             print("4. Transaction History")
#             print("5. Take Loan")
#             print("6. Transfer Amount")
#             print("7. Logout")

#             user_choice = input("Enter your choice: ")

#             if user_choice == '1':
#                 amount = int(input("Enter the deposit amount: "))
#                 current_user.deposit(amount)
#             elif user_choice == '2':
#                 amount = int(input("Enter the withdrawal amount: "))
#                 result = current_user.withdraw(amount)
#                 if result:
#                     print(result)
#             elif user_choice == '3':
#                 print(current_user.check_balance())
#             elif user_choice == '4':
#                 print("Transaction History:")
#                 print(current_user.check_transaction_history())
#             elif user_choice == '5':
#                 amount = int(input("Enter the loan amount: "))
#                 result = current_user.take_loan(amount)
#                 print(result)
#             elif user_choice == '6':
#                 recipient_account_number = int(input("Enter the recipient's account number: "))
#                 recipient = bank.get_user(recipient_account_number)
#                 if recipient:
#                     amount = int(input("Enter the transfer amount: "))
#                     result = current_user.transfer_amount(recipient, amount)
#                     print(result)
#                 else:
#                     print("Recipient account does not exist")
#             elif user_choice == '7':
#                 current_user = None
#             else:
#                 print("Invalid choice. Please enter a number between 1 and 7.")





bank = Bank()
user = bank.user_account("Rhaim", "Rhaim@mail.com", "123 Main St", "Savings")
admin = bank.admin_account()

current_user = None

while True:
    print("1. User System")
    print("2. Admin System")
    print("3. Exit")

    op = input("Enter your choice: ")

    if op == '1':
        while True:
            print("\nUser System:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Take Loan")
            print("6. Transfer Amount")
            print("7. Exit")

            user_choice = input("Enter your choice: ")

            if user_choice == '1':
                amount = int(input("Enter the deposit amount: "))
                user.deposit(amount)

            elif user_choice == '2':
                amount = int(input("Enter the withdrawal amount: "))
                result = user.withdraw(amount)
                if result:
                    print(result)

            elif user_choice == '3':
                print(f"Available Balance: {user.check_balance()}")

            elif user_choice == '4':
                print("Transaction History:")
                for transaction in user.check_history():
                    print(transaction)

            # elif user_choice == '5':
#                 amount = int(input("Enter the loan amount: "))
#                 result = current_user.take_loan(amount)
#                 print(result)    
            elif user_choice == '5':
                amount = int(input("Enter the loan amount: "))
                result = user.take_loan(amount)
                print(result)
            
            elif user_choice == '6':
                replace_account_number = int(input("Enter the replace's account number: "))
                replace = bank.get_user(replace_account_number)
                if replace:
                    amount = int(input("Enter the transfer amount: "))
                    result = user.transfer_amount(replace, amount)
                    print(result)
                else:
                    print("replace account does not exist")
            elif user_choice == '7':
                break
            else:
                print("Invalid choice.")

    elif op == '2':
        while True:
            print("\nAdmin System Menu:")
            print("1. Create User Account")
            print("2. Delete User Account")
            print("3. See All User Accounts")
            print("4. Check Total Available Balance")
            print("5. Check Total Loan Amount")
            print("6. Toggle Loan Feature")
            print("7. Exit")

            admin_choice = input("Enter your choice: ")

            if admin_choice == '1':
                name = input("Enter user's name: ")
                email = input("Enter user's email: ")
                address = input("Enter user's address: ")
                account_type = input("Enter account type (Savings/Current): ")
                new_user = bank.user_account(name, email, address, account_type)
                print(f"User account created successfully. Account number: {new_user.account_number}")
            elif admin_choice == '2':
                account_number = int(input("Enter the account number to delete: "))
                user_to_delete = bank.get_user(account_number)
                if user_to_delete:
                    admin.delete_user_account(user_to_delete)
                    print("User account deleted successfully.")
                else:
                    print("User account not found.")
            elif admin_choice == '3':
                print("\nAll User Accounts:")
                for user_acc in admin.all_user_accounts():
                    print(f"Account Number: {user_acc.account_number}, Name: {user_acc.name}")

            elif admin_choice == '4':

                print(f"Total Available Balance: {admin.total_available_balance()}")
            elif admin_choice == '5':
                print(f"Total Loan Amount: {admin.total_loan_amount()}")

            # elif user_choice == '5':
#                amount = int(input("Enter the loan amount: "))
#                result = current_user.take_loan(amount)
#                print(result)

            elif admin_choice == '6':
                print(f"Loan Feature: ")
            elif admin_choice == '7':
                break
            else:
                print("Invalid choice")

    elif op == '3':
        break

    else:
        print("Invalid choice.")
 