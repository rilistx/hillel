# Задача №36 (Студенты и группы)

"""
Создать класс, описывающий группу студентов - `Group`.
Данный класс хранит студентов в виде списка объектов
`Student` также реализованного в виде соответствующего класса.
В классах реализовать необходимай набор атрибутов (Например класс
`Student` должен иметь атрибуты `name`, `age`, `grades`), а так
же необходимый набор методов экземпляра для работы с этими экземплярами.

Наследование здесь не понадобится.
"""


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades.copy()

    def info(self):
        for i in range(len(self.grades)):
            self.grades[i] = str(self.grades[i])

        print('|{name:<15}|{age:^5}|{grades:^35}|'.format(
            name=self.name,
            age=str(self.age),
            grades='  '.join(self.grades)
        ))


class Group:
    def __init__(self, name):
        self.name = name
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(Student(student.name, student.age, student.grades))

    def show_student_list(self):
        print('|{name:^15}|{age:^5}|{grades:^35}|'.format(name='NAME', age='AGE', grades='GRADES'))
        print(' ' + '-' * 57 + ' ')
        for student in self.student_list:
            student.info()


first_group = Group('Первая Группа:')

student1 = Student('Андрей', 21, [6, 6, 1, 4, 9, 6, 9, 4, 8, 2, 3, 8])
first_group.add_student(student1)
student2 = Student('Василий', 18, [2, 9, 4, 7, 6, 6, 3, 6, 5, 5, 2, 4])
first_group.add_student(student2)
student3 = Student('Гавриил', 24, [3, 1, 4, 7, 7, 9, 4, 6, 8, 1, 1, 1])
first_group.add_student(student3)

second_group = Group('Вторая группа:')

student1 = Student('Иван', 22, [5, 3, 9, 8, 4, 6, 8, 2, 4, 3, 3, 1])
second_group.add_student(student1)
student2 = Student('Фёдор', 19, [5, 2, 8, 7, 6, 5, 3, 4, 4, 9, 7, 3])
second_group.add_student(student2)
student3 = Student('Герман', 20, [9, 8, 4, 6, 7, 5, 4, 6, 7, 1, 3, 2])
second_group.add_student(student3)

# ПЕРВАЯ ГРУППА
first_group.show_student_list()
print()

# ВТОРАЯ ГРУППА
second_group.show_student_list()
