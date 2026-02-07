# Student Grade Management System
# Structural Programming Approach

students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    students[roll] = {
        "name": name,
        "marks": [],
        "grade": ""
    }
    print("Student added successfully!\n")

def add_marks():
    roll = input("Enter Roll Number: ")
    if roll in students:
        marks = []
        for i in range(3):
            m = int(input(f"Enter marks for subject {i+1}: "))
            marks.append(m)
        students[roll]["marks"] = marks
        students[roll]["grade"] = calculate_grade(marks)
        print("Marks added successfully!\n")
    else:
        print("Student not found!\n")

def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"

def display_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        s = students[roll]
        print("\n--- Student Record ---")
        print("Name:", s["name"])
        print("Marks:", s["marks"])
        print("Grade:", s["grade"])
        print()
    else:
        print("Student not found!\n")

def menu():
    while True:
        print("1. Add Student")
        print("2. Add Marks")
        print("3. Display Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_marks()
        elif choice == "3":
            display_student()
        elif choice == "4":
            print("Program terminated.")
            break
        else:
            print("Invalid choice!\n")

# Program Start
menu()
