total = int(input("Enter total classes: "))
attended = int(input("Enter classes attended: "))
target = float(input("Enter target attendance percentage: "))
if total <= 0 or attended < 0 or attended > total:
    print("Invalid class details")
elif target <= 0 or target > 100:
    print("Invalid target percentage")
else:
    attendance = attended / total * 100
    print("Current attendance:", round(attendance, 2), "%")
    if attendance >= target:
        print("Target attendance already achieved")
    else:
        required = 0
        while ((attended + required) / (total + required)) * 100 < target:
            required += 1
        print("Additional classes required:", required)