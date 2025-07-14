# takes in user input
# name, password, amount
# if person isn't in textfile, create

from utils.string_manipulation import str_to_float
import time
class Bank:
    def __init__(self, path):
        self.acc_logins = {}
        self.path = path
        with open(path + "accounts.txt", "r") as file:
            for line in file:
                values = line.split(",")
                username = values[0]
                password = values[1]
                amount = str_to_float(values[2])
                self.acc_logins[username] = [password, amount]
    def change_balance(self, username, password, amount):
        if not self._check_password(username, password):
            return
        self.acc_logins[username][1] += str_to_float(amount)
        self._save()
    def transfer(self, username, password, other_username, amount):
        other_password = self.acc_logins[other_username][0]
        self.change_balance(username, password, "-" + str(amount))
        self.change_balance(other_username, other_password, str(amount))
        with open(self.path + "transactions.txt", "a") as file:
            current_time = time.strftime("%a %b %d %H:%M:%S %Y")
            file.write(str(current_time) + ": " + username + " transferred $" + str(amount) + " to " + other_username + ".\n")
    def get_balance(self, username, password):
        if not self._check_password(username, password):
            return
        print("Balance: " + str(self.acc_logins[username][1]))
    def change_password(self, username, old_password, new_password):
        if not self._check_password(username, old_password):
            return
        self.acc_logins[username][0] = new_password
        self._save()
    def add_user(self, username, password):
        if username in self.acc_logins:
            print("Error! User has already been added. Please try again!")
            return False
        self.acc_logins[username] = [password, 0]
        self._save()
        return True
    def withdraw(self, username, password, amount):
        self.change_balance(username, password, "-" + amount)
        with open(self.path + "transactions.txt", "a") as file:
            current_time = time.strftime("%a %b %d %H:%M:%S %Y")
            file.write(str(current_time) + ": " + username + " withdrew $" + str(amount) + " from their bank account.\n")
    def deposit(self, username, password, amount):
        self.change_balance(username, password, amount)
        with open(self.path + "transactions.txt", "a") as file:
            current_time = time.strftime("%a %b %d %H:%M:%S %Y")
            file.write(str(current_time) + ": " + username + " deposited $" + str(amount) + " to their bank account.\n")
    def _check_user_exists(self, username):
        if username not in self.acc_logins:
            return False
        return True
    def _check_password(self, username, password):
        if username not in self.acc_logins:
            print("User is not in database. Please try again!")
            return False
        if self.acc_logins[username][0] != password:
            print("Password is invalid. Please try again!")
            return False
        return True
    def _save(self):
        newFile = ""
        for key in self.acc_logins:
            newFile += key + "," + self.acc_logins[key][0] + "," + str(self.acc_logins[key][1]) + "\n"
        with open(self.path + "accounts.txt", "w") as file:
            file.write(newFile)
if __name__ == "__main__":
    import os
    print(os.listdir("."))
    b = Bank("./projects/bank/")
    user_help = input("Hello! How can I help you today? Type '1' to change balance, '2' to transfer money to another account, '3' to get balance, '4' to change password, or '5' to add user: ")
    while True:
        if user_help == "5":
            print("Please enter what username and password you would like to use for your new user.")
            while True:
                user_username = input("Username: ")
                user_password = input("Password: ")
                if b.add_user(user_username, user_password):
                    break
            break
        print("Please enter your account details to login.")
        while True:
            user_username = input("Username: ")
            user_password = input("Password: ")
            if b._check_password(user_username, user_password):
                if user_help == "1":
                    user_deposit_or_withdraw = input("Would you like to deposit or withdraw money? ")
                    while True:
                        if user_deposit_or_withdraw.lower() == "deposit":
                            user_amount = input("How much would you like to deposit? ")
                            b.deposit(user_username, user_password, user_amount)
                            break
                        if user_deposit_or_withdraw.lower() == "withdraw":
                            user_amount = input("How much would you like to withdraw? ")
                            b.withdraw(user_username, user_password, user_amount)
                            break
                        else:
                            user_deposit_or_withdraw = input("Error! Please only type 'deposit' or 'withdraw': ")
                    break
                if user_help == "2":
                    while True:
                        other_user = input("Who would you like to transfer money to? ")
                        if b._check_user_exists(other_user):
                            user_amount = input("How much money would you like to transfer? ")
                            b.transfer(user_username, user_password, other_user, user_amount)
                            break
                        else:
                            print("User does not exist. Please try again!")
                    break
                if user_help == "3":
                    b.get_balance(user_username, user_password)
                    break
                if user_help == "4":
                    user_new_password = input("What would you like to change your password to? ")
                    b.change_password(user_username, user_password, user_new_password)
                    break
        if user_help == "1" or user_help == "2" or user_help == "3" or user_help == "4":
            break
        else:
            user_help = input("Error! Please only type '1' to change balance, '3' to get balance, '4' to change password, or '5' to add user.")