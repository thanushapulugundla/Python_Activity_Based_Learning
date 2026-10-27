balance = float(input("Enter opening balance: "))
n = int(input("Enter number of transactions: "))
successful = rejected = 0
for i in range(n):
    print("Transaction", i + 1)
    action = input("Enter deposit or withdraw: ").lower()
    amount = float(input("Enter amount: "))
    if amount <= 0:
        print("Invalid amount")
        rejected += 1
    elif action == "deposit":
        balance += amount
        print("Deposit accepted")
        successful += 1
    elif action == "withdraw":
        if amount <= balance:
            balance -= amount
            print("Withdrawal accepted")
            successful += 1
        else:
            print("Insufficient balance")
            rejected += 1
    else:
        print("Invalid transaction type")
        rejected += 1
print("Final balance:", round(balance, 2))
print("Successful transactions:", successful)
print("Rejected transactions:", rejected)