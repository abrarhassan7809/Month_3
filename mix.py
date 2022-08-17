import json
from pathlib import Path

class Create_account:
    # num_costumer = 0
    # account_num = 4310

    def __init__(self, name, mobile_number, account_balance, pin):
        self.new_data = None
        self.game_on = True
        self.name = name
        self.mobile_number = int(mobile_number)
        # self.account_num = Create_account.account_num
        self.account_balance = int(account_balance)
        self.pin = pin

        # Create_account.account_num = Create_account.account_num + 1
        # Create_account.num_costumer = Create_account.num_costumer + 1

    # how to create account-----------
    def create_account(self):
        self.new_data = {
            self.name: {
                'name': self.name,
                'mobile number': self.mobile_number,
                # 'account number': self.account_num,
                'account balance': self.account_balance,
                'user pin': self.pin
            }
        }
        my_file = Path("data.json")
        if my_file.is_file():
            with open("data.json", "r+") as file:
                try:
                    data = json.load(file)
                except:
                    data = {}
                if self.name in data:
                    print("Username already exist please try again")
                    self.create_account()
                else:
                    file.seek(0)
                    file.truncate()
                    data[self.name] = self.new_data[self.name]
                    update_date = json.dumps(data, indent=4)
                    file.write(update_date)
        else:
            with open('data.json', 'w') as file:
                data_update = json.dumps(self.new_data, indent=4)
                file.write(data_update)

        print("***********************************")
        # print("No. of costumer is ", Create_account.num_costumer)
        self.show_detail()
        self.show_menu()
        input_2 = input('Enter the value : ')
        if input_2 == '1':
            print("***********************************")
            user_name = input('Please enter user name : ')
            user_pin = input('Please enter user pin : ')
            if self.name == user_name and self.pin == user_pin:
                self.add_money()
                self.show_detail()
            else:
                print("***********************************")
                print("invalid input please try again")

        elif input_2 == '2':
            print("***********************************")
            user_name = input('Please enter user name : ')
            user_pin = input('Please enter user pin : ')
            if self.name == user_name and self.pin == user_pin:
                self.withdraw_money()
                self.show_detail()
            else:
                print("***********************************")
                print("invalid input please try again")

        elif input_2 == '3':
            print("***********************************")
            user_name = input('Please enter user name : ')
            user_pin = input('Please enter user pin : ')
            if self.name == user_name and self.pin == user_pin:
                self.show_detail()
            else:
                print("***********************************")
                print("invalid input please try again")

        elif input_2 == 'exit':
            print("***********************************")
            print("You log out")
            self.game_on = False

    # default created account----------
    def default_account(self, cost_1):
        user_pin = input('Please enter user pin : ')

        with open("data.json", "r") as file:
            data = json.load(file)

        if user_pin == data[self.name]["user pin"]:
            # print("No. of costumer is ", Create_account.num_costumer)
            cost_1.show_detail()
            cost_1.show_menu()
            input_2 = input('Enter the value : ')
            if input_2 == '1':
                print("***********************************")
                if self.pin == user_pin:
                    cost_1.add_money()
                    cost_1.show_detail()
                    self.default_account(cost_1)
                else:
                    print("***********************************")
                    print("invalid input please try again")

            elif input_2 == '2':
                print("***********************************")
                if self.pin == user_pin:
                    cost_1.withdraw_money()
                    cost_1.show_detail()
                else:
                    print("***********************************")
                    print("invalid input please try again")

            elif input_2 == '3':
                print("***********************************")
                if self.pin == user_pin:
                    cost_1.show_detail()
                else:
                    print("***********************************")
                    print("invalid input please try again")

            elif input_2 == '4':
                print("***********************************")
                if self.pin == user_pin:
                    self.transfer_amount()
                else:
                    print("***********************************")
                    print("invalid user name please try again")

            elif input_2 == 'exit':
                print("***********************************")
                print("You log out")
                exit()
        else:
            print("***********************************")
            print("invalid input please try again")

    def show_menu(self):
        print("***********************************")
        print("Add money in your account press 1 :")
        print("Withdraw money from your account press 2 :")
        print("Show account details press 3 :")
        print("Transfer data press 4")
        print("close the program type exit :")

    # how to add money in your account----------
    def add_money(self):
        add_amount = int(input("Enter the amount : "))
        if add_amount > 0:
            self.account_balance = self.account_balance + add_amount
            with open('data.json') as file:
                data = json.load(file)
            data[self.name]["account balance"] = self.account_balance
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Successfully add Rs.{add_amount} in your account")
            exit()
        else:
            print("***********************************")
            print("invalid amount you entered please try again")

    # how to withdraw money-----------
    def withdraw_money(self):
        withdraw_amount = int(input("Enter the amount : "))
        if 0 <= withdraw_amount <= self.account_balance:

            self.account_balance = self.account_balance - withdraw_amount
            with open('data.json') as file:
                data = json.load(file)
            data[self.name]["account balance"] = self.account_balance
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Successfully withdraw Rs.{withdraw_amount} in your account")
            exit()

        else:
            print("***********************************")
            print("invalid amount you entered please try again")

    # how to show costumer details---------
    def show_detail(self):
        print(f"Name is {self.name} \nBalance is {self.account_balance} "
              f"\nMobile number is {self.mobile_number} \nAccount number is {self.pin}")

    # how to transfer money ----------
    def transfer_amount(self):
        default_user = input("Enter the user account name : ")
        transfer_money = int(input('Enter the amount : '))

        if 0 < transfer_money <= self.account_balance:
            self.account_balance = self.account_balance - transfer_money
            with open('data.json') as file:
                data = json.load(file)
            data[self.name]["account balance"] = self.account_balance
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
            # ------------------------------------

            with open('data.json') as file:
                data = json.load(file)

            data["account balance"][self.account_balance] = self.account_balance + transfer_money

            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
                data[default_user]["account balance"] = data["account balance"][self.account_balance]

            print(f"Transaction completed : your account balance is : {transfer_money}")
            exit()
        else:
            print("***********************************")
            print('invalid amount please try again')
