from meee import bankAccount
import os
from colorama import init
from colorama import Fore
init(autoreset=True)

file_trans = 'transactions.txt'
file_users = 'accountfile.txt'
account_balances = 'balance_users.txt'
usernamelist = ['']


def register():
    print('Input credentials to register account')
    username = input(Fore.LIGHTMAGENTA_EX + "Username ")
    password = input(Fore.LIGHTMAGENTA_EX + "Password ")
    with open(file_users, "a") as f:
        f.write(username)
        f.write(" ")
        f.write(password)
        f.write("\n")
        f.close()
        print(f'Account set up, thank you for choosing CAYMAN ISLANDS NATIONAL BANK™')
        print('To login please input your credentials')
        username = input(Fore.LIGHTMAGENTA_EX + "Username ")
        password = input(Fore.LIGHTMAGENTA_EX + "Password ")
        for line in open(file_users, "r").readlines():
            login_info = line.split()
            if username == login_info[0] and password == login_info[1]:
                print(Fore.LIGHTMAGENTA_EX + "LOGGED IN AS '{}'".format(username))
                username = bankAccount(username, 1000)
                return True
        print(Fore.LIGHTRED_EX + "LOGIN FAIL")
        return False

def login():
    print('To login please input your credentials')
    username = input(Fore.LIGHTMAGENTA_EX + "Username ")
    usernamelist.append(username)
    password = input(Fore.LIGHTMAGENTA_EX + "Password ")
    for line in open(file_users, "r").readlines():
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]:
            print(Fore.LIGHTMAGENTA_EX + "LOGGED IN AS '{}'".format(username))
            return True
    print(Fore.LIGHTRED_EX + "LOGIN FAIL")
    return False



while True:

    user1 = usernamelist[-1]
    user1 = bankAccount(user1, 1000) #user1 behöver ändras till 'username' och balance måste sparas (för flera användare)

    while True:
        userinput = input(Fore.GREEN + '''
        CAYMAN ISLANDS NATIONAL BANK™
        R) Register
        L) Login
        D) Make deposit
        W) Make withdrawal
        T) Check transactions
        B) Check available balance
        E) EXIT
        
        Enter 'TERMINATE' to delete all data
        ''').upper()

        if userinput == 'L':
            login()

        if userinput == 'R':
            register()

        elif userinput == 'W':
            ui = int(input(Fore.LIGHTMAGENTA_EX + 'How much would you like to withdraw?'))
            if ui < user1.balance:
                user1.withdraw(ui)
                print(Fore.LIGHTMAGENTA_EX + f'${ui} withdrawn from account: {usernamelist[-1]} ')
                with open(file_trans, 'a+') as f:
                    f.write(f'- ${ui}, Available balance: $' + str(user1.balance) + '\n')
            else:
                print('Insufficient funds')
                print('Funds currently available to withdraw', user1.balance)

        elif userinput == 'D':
            uis = int(input(Fore.LIGHTMAGENTA_EX + 'How much would you like to deposit?'))
            user1.deposit(uis)
            print(Fore.LIGHTMAGENTA_EX + f'${uis} deposited to account: {usernamelist[-1]} ')
            with open(file_trans, 'a+') as f:
                f.write(f'+ ${uis}, Available balance: $' + str(user1.balance) + '\n')

        elif userinput == 'T':
            with open(file_trans, 'r+') as f:
                for row in file_trans:
                    print(f.readline())

        elif userinput == 'TERMINATE':
            inp = input(Fore.LIGHTMAGENTA_EX + 'Enter "C" to confirm').upper()
            if inp == 'C':
                os.remove("accountfile.txt")
                os.remove("transactions.txt")
                print(Fore.LIGHTMAGENTA_EX + 'SUCSESSFUL TERMINATION')
                break

        elif userinput == 'B':
            print(user1.balance)

        elif userinput == 'E':
            break

    break



print(Fore.LIGHTMAGENTA_EX + '\nCAYMAN ISLANDS NATIONAL BANK™ CLOSING')
print(Fore.LIGHTMAGENTA_EX + 'HAVE A GOOD LIFE')
