class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades.copy()


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(Student(student.name, student.grades))
