MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

import random

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def get_slot_machine_spin(rows, cols, symbols):

def deposit():
    while True:
        amount = input("Enter amount to be deposited: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter amount greater than 0.")
        else:
            print("Please enter a valid amount")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to be bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a valid number of lines.")
    return lines

def get_bet():
    while True:
        amount = input("Enter amount to bet on each line: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid amount.")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")


main()
