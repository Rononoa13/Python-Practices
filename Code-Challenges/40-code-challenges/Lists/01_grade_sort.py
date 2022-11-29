first_grade = int(input("What is your first grade (0-100): "))
second_grade = int(input("What is your second grade (0-100): "))
third_grade = int(input("What is your third grade (0-100): "))
fourth_grade = int(input("What is your fourth grade (0-100): "))

grade_list = [first_grade, second_grade, third_grade, fourth_grade]
# 

print(f"Your grades are: {grade_list}")

grade_list.sort()
grade_list.reverse()

print(f"Your grades from highest to lowest are: {grade_list}")
print(f"The lowest grades will now be dropped.")

low_grade = grade_list.pop()
low_grade1 = grade_list.pop()
print(f"Removed grade: {low_grade}")
print(f"Removed grade: {low_grade1}")

print(f"Your remaining grades are: {grade_list}")