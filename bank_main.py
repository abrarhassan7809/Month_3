from json import JSONDecodeError

from bank import *
import json
import sys
int(sys.maxsize)

game_on = True
while game_on:
    if __name__ == '__main__':
        print("***********************************")
        print('You want to create an account press 1')
        print('You have already an account press 2')
        print('You want to close the program type exit')
        input_1 = input('Enter the Choice : ')

        # create an account using condition------------
        if input_1 == '1':
            while game_on:
                print("***********************************")
                name = input('Enter your name : ')
                mobile_num = input('Enter your mobile number : ')
                acc_balance = input('Enter the amount : ')
                create_pin = input('Create your 4 digit pin : ')
                if len(name) >= 1 and int(mobile_num) >= 1 and int(acc_balance) >= 1 and int(create_pin) >= 1:
                    if len(mobile_num) == 11 and len(create_pin) == 4:
                        # create an object and pass the arguments-------------
                        cost_1 = Create_account(name, mobile_num, acc_balance, create_pin)
                        cost_1.create_account()
                        game_on = False
                    else:
                        print("***********************************")
                        print("please enter valid mobile number and pin")
                else:
                    print("***********************************")
                    print("Please Enter the Right information")

        # already created account using condition ---------------
        elif input_1 == '2':
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)

                account_id = input('Enter the user account name : ')
                if account_id in data:
                    cost_1 = Create_account(data[account_id]["name"], data[account_id]["mobile number"],
                                            data[account_id]["account balance"], data[account_id]["user pin"])
                    cost_1.default_account(cost_1)
                    game_on = False
                else:
                    print("***********************************")
                    print("invalid user name try again")
            except JSONDecodeError:
                print("***********************************")
                print("There is no account :")

        elif input_1 == 'exit':
            print("***********************************")
            print("You log out")
            game_on = False

        else:
            print("invalid input please try again")
