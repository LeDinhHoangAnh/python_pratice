class StudentManager():
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def list_student(self):
        if not self.students:
            print("No students in list")
        else:
            for student in self.students:
                student.display_info()
    def find_student_by_id(self, student_id_find):
        for student in self.students:
            if student.get_id() == student_id_find:
                return student
            return None
    def remove_student(self, student_id_remove):
        student_remove = self.find_student_by_id(student_id_remove)
        if student_remove:
            self.students.remove(student_remove)
            print("Has deleted student", student_remove._name)
        else:
            print("Not found student with ID",student_id_remove)