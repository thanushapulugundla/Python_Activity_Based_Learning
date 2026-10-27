n = int(input("Enter number of transactions: "))
threshold = float(input("Enter high-value threshold: "))
seen = set()
duplicates = high_value = 0
for i in range(n):
    print("Transaction", i + 1)
    transaction_id = input("Enter transaction ID: ").strip().upper()
    amount = float(input("Enter transaction amount: "))
    if transaction_id in seen:
        print("Repeated transaction ID:", transaction_id)
        duplicates += 1
    else:
        seen.add(transaction_id)
    if amount > threshold:
        print("High-value transaction:", amount)
        high_value += 1
print("Repeated transactions:", duplicates)
print("High-value transactions:", high_value)