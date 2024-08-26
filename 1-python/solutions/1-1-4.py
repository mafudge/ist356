number_grade = int(input("Enter your numerical grade: 0 - 120"))
letter_grade = "unknown"

if number_grade >= 0 and number_grade <= 120:

    if number_grade > 95:
        letter_grade = "A"
    elif number_grade > 75:
        letter_grade = "B"
    elif number_grade > 50:
        letter_grade = "C"
    else:
        letter_grade = "F"

    print(f"For {number_grade} points the letter grade is {letter_grade}")

else:
    print(f"Number grade of {number_grade} is out of range!")