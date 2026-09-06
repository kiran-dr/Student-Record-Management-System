# ==========================================
# STUDENT RECORD MANAGEMENT SYSTEM
# ==========================================

import os

students = {}


def load_data():
    if os.path.exists("students.txt"):
        file = open("students.txt", "r")

        for line in file:
            data = line.strip().split(",")

            roll = data[0]
            name = data[1]
            branch = data[2]
            cgpa = data[3]

            students[roll] = [name, branch, cgpa]

        file.close()


def save_data():
    file = open("students.txt", "w")

    for roll in students:
        file.write(f"{roll},{students[roll][0]},{students[roll][1]},{students[roll][2]}\n")

    file.close()


def add_student():
    roll = input("Enter Roll Number : ")

    if roll in students:
        print("Student already exists.")
        return

    name = input("Enter Name : ")
    branch = input("Enter Branch : ")
    cgpa = input("Enter CGPA : ")

    students[roll] = [name, branch, cgpa]

    save_data()

    print("Student Added Successfully.")


def display_students():

    if len(students) == 0:
        print("No Records Found.")
        return

    print("\n")
    print("=" * 60)
    print("{:<15}{:<20}{:<15}{:<10}".format(
        "Roll No", "Name", "Branch", "CGPA"))
    print("=" * 60)

    for roll in students:
        print("{:<15}{:<20}{:<15}{:<10}".format(
            roll,
            students[roll][0],
            students[roll][1],
            students[roll][2]
        ))


def search_student():
    roll = input("Enter Roll Number : ")

    if roll in students:
        print("\nStudent Found")
        print("Name   :", students[roll][0])
        print("Branch :", students[roll][1])
        print("CGPA   :", students[roll][2])
    else:
        print("Student Not Found.")


def update_student():
    roll = input("Enter Roll Number : ")

    if roll not in students:
        print("Student Not Found.")
        return

    print("Leave blank to keep old value.\n")

    name = input(f"Name ({students[roll][0]}) : ")
    branch = input(f"Branch ({students[roll][1]}) : ")
    cgpa = input(f"CGPA ({students[roll][2]}) : ")

    if name != "":
        students[roll][0] = name

    if branch != "":
        students[roll][1] = branch

    if cgpa != "":
        students[roll][2] = cgpa

    save_data()

    print("Record Updated Successfully.")


def delete_student():
    roll = input("Enter Roll Number : ")

    if roll in students:
        del students[roll]

        save_data()

        print("Record Deleted Successfully.")
    else:
        print("Student Not Found.")


load_data()

while True:

    print("\n")
    print("=" * 45)
    print("   STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter Your Choice : ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You.")
        break

    else:
        print("Invalid Choice.")
