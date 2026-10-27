n = int(input("Enter number of questions: "))
if n <= 0:
    print("Invalid number of questions")
else:
    key = input("Enter answer key: ").upper()
    if len(key) != n:
        print("Answer key length must match number of questions")
    else:
        students = int(input("Enter number of students: "))
        if students <= 0:
            print("Invalid number of students")
        else:
            correct_counts = [0] * n
            valid_submissions = 0
            for i in range(students):
                print("Student", i + 1)
                answers = input("Enter answers: ").upper()
                if len(answers) != n:
                    print("Invalid answer length; submission skipped")
                    continue
                valid_submissions += 1
                score = 0
                for j in range(n):
                    if answers[j] == key[j]:
                        score += 1
                        correct_counts[j] += 1
                print("Correct answers:", score)
                print("Score percentage:", round(score / n * 100, 2), "%")
            if valid_submissions == 0:
                print("No valid student submissions")
            else:
                print("Question-wise success rates:")
                for j in range(n):
                    rate = correct_counts[j] / valid_submissions * 100
                    print("Question", j + 1, ":", round(rate, 2), "%")
                lowest = min(correct_counts)
                print("Most difficult question(s):")
                for j in range(n):
                    if correct_counts[j] == lowest:
                        print("Question", j + 1)