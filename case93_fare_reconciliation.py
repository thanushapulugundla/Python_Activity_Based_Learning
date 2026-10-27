fares = {
    "A": {"adult": 20, "student": 10},
    "B": {"adult": 30, "student": 15}
}
n = int(input("Enter number of route records: "))
expected_total = collected_total = 0
discrepancies = 0
if n <= 0:
    print("Invalid number of records")
else:
    for i in range(n):
        print("Record", i + 1)
        route = input("Enter route A or B: ").upper()
        category = input("Enter adult or student: ").lower()
        passengers = int(input("Enter passenger count: "))
        collected = float(input("Enter collected fare: "))
        if route not in fares:
            print("Invalid route")
        elif category not in fares[route]:
            print("Invalid passenger category")
        elif passengers <= 0 or collected < 0:
            print("Invalid passenger count or fare")
        else:
            expected = fares[route][category] * passengers
            difference = collected - expected
            expected_total += expected
            collected_total += collected
            print("Expected fare: Rs.", expected)
            print("Collected fare: Rs.", round(collected, 2))
            if difference == 0:
                print("Fare reconciled")
            else:
                print("Discrepancy: Rs.", round(difference, 2))
                discrepancies += 1
    print("Total expected fare: Rs.", expected_total)
    print("Total collected fare: Rs.", round(collected_total, 2))
    print("Records with discrepancies:", discrepancies)