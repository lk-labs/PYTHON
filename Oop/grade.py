def get_student_details():
    registration_number = input("Enter registration number: ")
    name = input("Enter student name: ")
    gender = input("Enter student gender: ")
    unit_name = input("Enter unit name: ")
    unit_code = input("Enter unit code: ")

    while True:
        try:
            marks = float(input("Enter marks for {} (0-100): ".format(unit_name)))
            if 0 <= marks <= 100:
                return registration_number, name, gender, unit_name, unit_code, marks
            else:
                print("Error: Marks should be between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value for marks.")

def calculate_grade_and_comments(marks):
    if 70 <= marks <= 100:
        return 'A', 'Excellent'
    elif 60 <= marks <= 69:
        return 'B', 'Good'
    elif 50 <= marks <= 59:
        return 'C', 'Fair'
    elif 40 <= marks <= 49:
        return 'D', 'Pass'
    elif 0 <= marks <= 39:
        return 'F', 'Fail'

def main():
    registration_number, name, gender, unit_name, unit_code, marks = get_student_details()

    grade, comments = calculate_grade_and_comments(marks)
    print("\nTranscript:")
    print("Registration Number: {}".format(registration_number))
    print("Student Name: {}".format(name))
    print("Gender: {}".format(gender))
    print("Unit Name: {}".format(unit_name))
    print("Unit Code: {}".format(unit_code))
    print("Marks: {:.2f}".format(marks))
    print("Grade: {}".format(grade))
    print("Comments: {}".format(comments))

if __name__ == "__main__":
    main()
