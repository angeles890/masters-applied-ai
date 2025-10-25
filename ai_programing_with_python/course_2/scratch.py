import sys

def get_user_input(msg: str) -> str:
    while True:
        user_input = input(msg).strip()
        if user_input:
            return user_input
        print("Input cannot be empty")

names_raw = get_user_input("Enter a comma seperated list of names: ").title()
assignments_raw = get_user_input("Enter a comma seperated list of number of assignments outstanding: ")
grades_raw = get_user_input("Enter a comma seperated list of a before and after pair denoted by a colon. (Example 77:89, 67:72): ")


names = names_raw.split(',')
assignments = assignments_raw.split(',')
grades = grades_raw.split(',')

for name, asgn, grade in zip(names, assignments, grades):
    grade_lst = grade.split(':')
    message = f"Hi {name},\n\nThis is a reminder that you have {asgn} assignments left to \
    submit before you can graduate. Your current grade is {grade_lst[0]} and can increase \
    to {grade_lst[1]} if you submit all assignments before the due date.\n\n"

    print(message)