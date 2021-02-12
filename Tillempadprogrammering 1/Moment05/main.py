from meee import *

import os
import json
import itertools
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)

counter = 0

transactions = []
saldo = []
file = 'transactions.txt'

while True:
    userinput = input(Fore.GREEN + '''
    CAYMAN ISLANDS NATIONAL BANK™
    
    A) Open account
    B) Make deposit
    C) Make withdrawal
    D) Check transactions
    E) Check available balance
    F) TERMINATE ACCOUNT
    ''').upper()
    if userinput == 'A':
        while True:
            userans = input('Would you like to open a new bank account? (Y/N)').upper()

            if userans == 'Y' or userans == 'YES':
                name = input('What is your name?')

                user1 = bankAccount(name, 1000)
                transactions.append(+1000)
                saldo.append(user1.balance)

                print(f'Account set up, thank you {name} for choosing CAYMAN ISLANDS NATIONAL BANK™')
                print(f'Current balance: ${user1.balance}')
                break

            else:
                print(Fore.GREEN + 'ok...')
                break
    elif userinput == 'B':
        ui = int(input('How much would you like to deposit?'))
        user1.deposit(ui)
        print(Fore.GREEN + f'{ui} Deposited')
        transactions.append(+ui)
        saldo.append(user1.balance)

    elif userinput == 'C':
        usi = int(input('How much would you like to withdraw?'))
        if usi > user1.balance:
            print('Incufficient funds')
        user1.withdraw(usi)
        transactions.append(-usi)
        saldo.append(user1.balance)

    elif userinput == 'D':
        with open('transaction.txt', 'w') as f:
            f.write(json.dumps(transactions))
            f.write(json.dumps(saldo))

        print('Transactions: ')
        for (t, s) in zip(transactions, saldo):
            print(f'{t}$   Balance: {s} ')

    elif userinput == 'E':
        print(f'${user1.balance} currently available')

    elif userinput == 'F':
        ter = input('Are you sure you want to terminate your account, all data will be lost forever. Press "C" to continue').upper()
        if ter == 'C':
            os.remove("transaction.txt")
            print("Transactions Removed!")
        else:
            pass


    else:
        print(Fore.RED + 'ERROR')
