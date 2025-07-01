from person import Person

class Student(Person):
    def __init__(self, student_id: int, name: str, major: str):
        super().__init__(name)
        self.__student_id = student_id
        self.major = major
    def display_info(self):
        print(f"ID: {self.__student_id}, Name: {self._name}, Major:{self.major}")
    
    def get_id(self):
        return self.__student_id