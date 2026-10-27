n = int(input("Enter number of students: "))
risk_count = 0
for i in range(n):
    print("Student", i + 1)
    name = input("Enter student name: ")
    marks = float(input("Enter marks percentage: "))
    attendance = float(input("Enter attendance percentage: "))
    lab = float(input("Enter lab score percentage: "))
    risks = []
    if marks < 50:
        risks.append("Low marks")
    if attendance < 75:
        risks.append("Low attendance")
    if lab < 50:
        risks.append("Low lab score")
    if risks:
        print(name, "- At academic risk:", ", ".join(risks))
        risk_count += 1
    else:
        print(name, "- No academic risk")
print("Students at academic risk:", risk_count)