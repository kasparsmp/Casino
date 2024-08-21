
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