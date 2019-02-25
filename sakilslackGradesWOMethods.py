# Keymoni Sakil-Slack
# 01/24/2019
# sakilslackGradesWOMethods
# This program will calculate a student's grade


import sakilslackGradesMethods as grade

def main():
    num = grade.get_input()
    average = grade.get_average(num)
    letter_grade = grade.get_letter_grade(average)
    display_grade = grade.display_grade(average,letter_grade)

if __name__ == "__main__":
    main()
