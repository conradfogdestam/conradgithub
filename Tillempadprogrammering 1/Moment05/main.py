#kursolle moment05 bankapp
#Conrad Fogdestam te19d

from meee import bankAccount # funktion för .balance .withdraw .deposit
import os # för att kunna wipea alla filer
import sys # stänga programmet vid EXIT
from colorama import init #färgtext
from colorama import Fore #färgtext
init(autoreset=True) #färgtext reset efter varje print

file_trans = 'transactions.txt'
file_users = 'accountfile.txt'
file_bal = 'balance.txt'
usern = ['NOT LOGIN']
baluser = [1000]


def register():
    print(Fore.LIGHTMAGENTA_EX + 'Input credentials to register account')
    username = input(Fore.CYAN + "Username ")
    usern.append(username)
    usern[-1] = bankAccount(username, 1000)
    password = input(Fore.CYAN + "Password ")
    with open(file_users, "a") as f:
        f.write(username)
        f.write(" ")
        f.write(password)
        f.write("\n")
        f.close()
        print(Fore.LIGHTMAGENTA_EX + f'Account set up, thank you for choosing CAYMAN ISLANDS NATIONAL BANK™')
    with open(file_bal, 'w+') as fi:
        fi.write(str(1000))

def login():
    print(Fore.LIGHTMAGENTA_EX + 'To login please input your credentials')
    username = input(Fore.CYAN + "Username ")
    password = input(Fore.CYAN + "Password ")
    usern.append(username)
    for line in open(file_users, "r").readlines():
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]:
            print(Fore.LIGHTMAGENTA_EX + "LOGGED IN AS '{}'".format(username))
            return True
    print(Fore.LIGHTRED_EX + "LOGIN FAIL")
    return False


while True:
    userinput = input(Fore.LIGHTCYAN_EX + '''
        CAYMAN ISLANDS NATIONAL BANK™
            L) Login
            R) Register
            E) EXIT
            ''').upper()

    if userinput == 'R':
        register()


    if userinput == 'E':
        print(Fore.LIGHTMAGENTA_EX + 'GOODBYE')
        break

    if userinput == 'L':
            if login() == True:
                with open(file_bal, 'r') as f:
                    temp = f.read()
                    baluser.append(int(temp))

                print(baluser)
                print(usern)

                user1 = bankAccount(usern[-1], int(baluser[-1]))

                while True:
                    userinput = input(Fore.LIGHTCYAN_EX + 'CAYMAN ISLANDS NATIONAL BANK™\n D) Make deposit\n W) Make withdrawal\n T) Check transactions\n B) Check available balance\n E) EXIT\nEnter "TERMINATE" to delete all data\n').upper()

                    if userinput == 'W':

                        ui = int(input(Fore.LIGHTMAGENTA_EX + 'How much would you like to withdraw?'))
                        if ui < user1.balance:
                            user1.withdraw(ui)
                            print(Fore.LIGHTMAGENTA_EX + '${} withdrawn from account '.format(ui))
                            with open(file_trans, 'a+') as f:
                                f.write(f'- ${ui}, Available balance: $' + str(user1.balance) + '\n')
                            with open(file_bal, 'w+') as fi:
                                fi.write(str(user1.balance))

                        else:
                            print('Insufficient funds')
                            print('Funds currently available to withdraw', user1.balance)

                    elif userinput == 'D':
                        try:
                            uis = int(input(Fore.LIGHTMAGENTA_EX + 'How much would you like to deposit?'))
                            user1.deposit(uis)
                            print(Fore.LIGHTMAGENTA_EX + '${} deposited to account'.format(uis))
                            with open(file_trans, 'a+') as f:
                                f.write(f'+ ${uis}, Available balance: $' + str(user1.balance) + '\n')
                            with open(file_bal, 'w+') as fi:
                                fi.write(str(user1.balance))
                        except:
                            print(Fore.LIGHTRED_EX + 'Deposit needs to be an integer')

                    elif userinput == 'T':
                        try:
                            with open(file_trans, 'r+') as f:
                                for line in file_trans:
                                    print(f.readline().strip('\n'))
                        except:
                            print('No Transactions to display')

                    elif userinput == 'B':
                        print(Fore.LIGHTMAGENTA_EX + "$", user1.balance)

                    elif userinput == 'E':
                        print(Fore.LIGHTMAGENTA_EX + 'GOODBYE')
                        sys.exit()

                    elif userinput == 'TERMINATE':

                        os.remove('accountfile.txt')
                        os.remove('transactions.txt')
                        os.remove('balance.txt')
                        baluser.clear()
                        usern.clear()
                        print(Fore.LIGHTMAGENTA_EX + 'Sucsessfully deleted all files')
                        sys.exit()
