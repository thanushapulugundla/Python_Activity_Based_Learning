n = int(input("Enter number of registration records: "))
if n <= 0:
    print("Invalid number of records")
else:
    seen = set()
    valid = invalid = duplicates = 0
    for i in range(n):
        print("Record", i + 1)
        record = input("Enter ID|Name|Email: ")
        parts = record.split("|")
        if len(parts) != 3:
            print("Invalid record format")
            invalid += 1
            continue
        reg_id = parts[0].strip().upper()
        name = parts[1].strip()
        email = parts[2].strip()
        errors = []
        if len(reg_id) != 6 or not reg_id.startswith("REG") or not reg_id[3:].isdigit():
            errors.append("Invalid registration ID")
        if name == "":
            errors.append("Missing name")
        if "@" not in email or "." not in email.split("@")[-1]:
            errors.append("Invalid email")
        if reg_id in seen:
            print("Duplicate registration ID:", reg_id)
            duplicates += 1
            errors.append("Duplicate ID")
        else:
            seen.add(reg_id)
        if errors:
            for error in errors:
                print(error)
            invalid += 1
        else:
            print("Valid record:", reg_id, name, email)
            valid += 1
    print("Valid records:", valid)
    print("Invalid records:", invalid)
    print("Duplicate IDs detected:", duplicates)