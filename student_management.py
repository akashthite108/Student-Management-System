students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")

    student = {
        "roll": roll,
        "name": name,
        "age": age
    }

    students.append(student)
    print("Student Added Successfully!")

def view_students():
    if not students:
        print("No Records Found!")
        return

    print("\nStudent Records")
    print("-" * 30)

    for student in students:
        print(f"Roll No: {student['roll']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print("-" * 30)

def search_student():
    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found")
            print(student)
            return

    print("Student Not Found!")

def update_student():
    roll = input("Enter Roll Number to Update: ")

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            print("Record Updated Successfully!")
            return

    print("Student Not Found!")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Record Deleted Successfully!")
            return

    print("Student Not Found!")

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")