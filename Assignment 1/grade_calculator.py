
student_name = input("Enter student name: ")
subject_first = int(input("Enter Math marks: "))
subject_second = int(input("Enter English marks: "))
subject_third = int(input("Enter Python marks: "))


if (subject_first <= 0 or subject_first > 100 or
    subject_second <= 0 or subject_second > 100 or
    subject_third <= 0 or subject_third > 100):

    print("Invalid Marks! Please enter marks between 1 and 100.")

else:
    
    average_marks = (subject_first + subject_second + subject_third) / 3

   
    if average_marks >= 80:
        grade = "A+"
    elif average_marks >= 70:
        grade = "A"
    elif average_marks >= 60:
        grade = "A-"
    elif average_marks >= 50:
        grade = "B"
    elif average_marks >= 40:
        grade = "C"
    else:
        grade = "F"


    print("\nStudent Name:", student_name)
    print("Average Marks:", round(average_marks, 2))
    print("Final Grade:", grade)
