# checkbook.py is a command line checkbook application that allows users to track their finances
import csv
import os

# variables
play_game = True


def get_checkbook_status():
    """
    Determine if the customer has an account; if not, create an account for the customer.
    :return: status of account as accessed or created
    """
    if os.path.exists('checkbook.csv'):
        get_status = 'Accessing your checkbook!'
    else:
        with open('checkbook.csv', 'w') as f_gcs:
            cols = ['transaction', 'balance']
            transaction = {'transaction': "new account", 'balance': 0}
            writer = csv.DictWriter(f_gcs, fieldnames=cols)
            writer.writeheader()
            writer.writerow(transaction)
        get_status = 'Creating your new checkbook account!'
    return get_status


def get_checkbook_balance():
    """
    Get customer checkbook balance.
    :return: current balance
    """
    with open('checkbook.csv', 'r') as f_gcb:
        cols = ['transaction', 'balance']
        content = csv.DictReader(f_gcb, fieldnames=cols)  # output is a list [balance, 0]
        lines = []
        for line in content:
            lines.append(line)
        current_transaction = lines[-1]["balance"]
        if lines[-2]["balance"] == "balance":
            previous_transaction = 0
        else:
            previous_transaction = lines[-2]["balance"]
        print(previous_transaction)
        print(type(previous_transaction))
        get_current_balance = int(current_transaction) + int(previous_transaction)
    return get_current_balance


def get_valid_input_debit_or_credit(get_choice):
    """
    Prevent invalid input for debits and credits.
    :param get_choice:
    :return: valid input
    """
    if get_choice == 2:
       choice_value = 'debit'
    else:
        choice_value = 'credit'
    while True:
        debit_or_credit_str = input(f'How much is the {choice_value}: ').lower()
        if debit_or_credit_str.isdigit() and int(debit_or_credit_str) > 0:
            valid_input_debit_or_credit = int(debit_or_credit_str)
            break
    return valid_input_debit_or_credit

while play_game:
    print("~~~ Welcome to the terminal checkbook! ~~~\n")
    print("What would you like to do?\n")
    print("1 - view current balance")
    print("2 - record a debit (withdraw)")
    print("3 - record a credit (deposit)")
    print("4 - exit\n")

    while True:
        choice_str = input('Enter your choice: ').lower()
        if choice_str.isdigit() and (0 < int(choice_str) < 5):
            choice = int(choice_str)
            break

    if choice == 4:
        print('Thanks, have a great day!')
        play_game = False

    elif choice == 1:
        checkbook_status = get_checkbook_status()
        print(checkbook_status)
        current_balance = get_checkbook_balance()
        print(f'Your current balance is ${current_balance}\n')

    elif choice == 2:
        debit = get_valid_input_debit_or_credit(choice)
        debit = debit * -1

        checkbook_status = get_checkbook_status()
        print(checkbook_status)

        with open('checkbook.csv', 'a') as f:
            cols_debit = ['transaction', 'balance']
            transaction_debit = {'transaction': "debit", 'balance': debit}
            writer_debit = csv.DictWriter(f, fieldnames=cols_debit)
            writer_debit.writerow(transaction_debit)

    elif choice == 3:
        credit = get_valid_input_debit_or_credit(choice)

        checkbook_status = get_checkbook_status()
        print(checkbook_status)

        with open('checkbook.csv', 'a') as f:
            cols_credit = ['transaction', 'balance']
            transaction_credit = {'transaction': "debit", 'balance': credit}
            writer_credit = csv.DictWriter(f, fieldnames=cols_credit)
            writer_credit.writerow(transaction_credit)

    else:
        print("Something seriously is fishy - Yo money is gaw-gaw-gone!!!")
