#list for grades
grades = []
#grades total, passing
passed_student = 0
total_grade = 0


#checking for input of grades 
while True:
    grades_input = input("Please enter the grade for student between 40 to 100 (type 'done' to finish): ")
    if grades_input.isdigit():
        grades_input = int(grades_input)
        if grades_input < 40 or grades_input > 100:
            print("Error! Please enter grades between 40 to 100 only!")
        else:
            grades.append(grades_input)
            
    elif grades_input.lower() == 'done':
        print("Grades List:", grades)
        break
    else:
        print("Error!")
        
for grade in grades:
    total_grade =+ grade
    average_grade = total_grade / len(grades)
else:
    print(f'\n\nAverage Grade: {average_grade:.2f}')
for grade in grades:
    if grade >= 75:
        passed_student += 1
else:
    print(f'Number of Passed Students: {passed_student}')
    pass_percent = (passed_student / len(grades)) * 100
    print(f'Pass Percentage: {pass_percent:.2f}%')
