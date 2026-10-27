menu = {"idli": 20, "dosa": 50, "juice": 40}
stock = {"idli": 20, "dosa": 10, "juice": 8}
total_sales = 0
n = int(input("Enter number of orders: "))
for i in range(n):
    print("Order", i + 1)
    item = input("Enter item (idli/dosa/juice): ").lower()
    quantity = int(input("Enter quantity: "))
    if item not in menu:
        print("Item not available")
    elif quantity <= 0:
        print("Invalid quantity")
    elif quantity > stock[item]:
        print("Insufficient stock")
    else:
        cost = menu[item] * quantity
        total_sales += cost
        stock[item] -= quantity
        print("Order accepted. Cost: Rs.", cost)
        print("Remaining stock:", stock[item])
print("Total sales: Rs.", total_sales)
print("Final stock:", stock)