n = int(input("Enter number of classes: "))
classes = []
for i in range(n):
    print("Class", i + 1)
    subject = input("Enter subject name: ")
    day = input("Enter day: ").upper()
    start = int(input("Enter start hour (0-23): "))
    end = int(input("Enter end hour (0-23): "))
    if start < 0 or end > 23 or start >= end:
        print("Invalid time; record skipped")
        continue
    classes.append((subject, day, start, end))
conflict_found = False
for i in range(len(classes)):
    for j in range(i + 1, len(classes)):
        s1, d1, a1, b1 = classes[i]
        s2, d2, a2, b2 = classes[j]
        if d1 == d2 and a1 < b2 and a2 < b1:
            print("Conflict:", s1, "and", s2, "on", d1)
            conflict_found = True
if not conflict_found:
    print("No timetable conflicts detected")