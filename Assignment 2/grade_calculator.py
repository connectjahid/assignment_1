
# Student Grade Calculator

# 1. Take Student Information
student_name = input("Enter Student Name: ")

# 2. Take Subject Marks
math_marks = int(input("Enter Math Marks: "))
english_marks = int(input("Enter English Marks: "))
python_marks = int(input("Enter Python Marks: "))

# 3. Validate Marks
if (math_marks < 0 or math_marks > 100 or
    english_marks < 0 or english_marks > 100 or
    python_marks < 0 or python_marks > 100):

    print("Invalid Marks! Please enter marks between 0 and 100.")

else:

    # 4. Calculate Total and Average
    total_marks = math_marks + english_marks + python_marks

    average_marks = total_marks / 3

    # 5. Determine Grade
    if average_marks >= 80:
        grade = "A+"
    elif average_marks >= 70:
        grade = "A"
    elif average_marks >= 60:
        grade = "B"
    elif average_marks >= 50:
        grade = "C"
    else:
        grade = "F"

    # 6. Display Student Result

    print(f"Student Name: {student_name}")
    print(f"Math Marks: {math_marks}")
    print(f"English Marks: {english_marks}")
    print(f"Python Marks: {python_marks}")


    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Final Grade: {grade}")

 
