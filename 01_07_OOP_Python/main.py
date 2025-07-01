if __name__ == "__main__":
    from student import Student
    from student_manager import StudentManager

    manager = StudentManager()

    while True:
        print("\n--Student Manager--")
        print("1.Add student")
        print("2.Display list of student")
        print("3.Find student by ID")
        print("4.Delete student")
        print("5.Exit")

        choice = input("Select option from 1 to 5: ")
        if choice == "1":
            while True:
                student_id_add = input("Enter ID of student: ")
                if manager.find_student_by_id(student_id_add):
                    print("Existed ID ! Enter again")
                else:
                    break
            name = input("Enter name of student: ")
            major = input("Enter major of student: ")
            student_add = Student(student_id_add, name, major)
            manager.add_student(student_add)
        elif choice == "2":
            manager.list_student()
        elif choice == "3":
             student_id_find = input("Enter student ID to find")
             student_find = manager.find_student_by_id(student_id_find)
             if student_find:
                    student_find.display_info()
             else:
                    print(f"Not found student with ID {student_id_find}")
        elif choice == "4":
             student_id_remove = input("Enter student ID to remove:")
             student_remove = manager.find_student_by_id(student_id_remove)
             manager.remove_student(student_id_remove)
        elif choice == "5":
             break
        else:
             print("Choose option from 1 to 5. Please choose again")



