class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = []

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in student.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' + f'Фамилия: {self.surname}\n' + f'Средняя оценка за домашние задания: {self.grades[0]}\n' + f'Курсы в процессе изучения: {"".join(self.courses_in_progress)}\n' + f'Завершенные курсы: {"".join(self.finished_courses)}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(self, name)
        self.grades = []

    def __str__(self):
        return f'Имя: {self.name}\n' + f'Фамилия: {self.surname}\n' + f'Средняя оценка за лекции: {self.grades[0]}\n'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(self, name)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' + f'Фамилия: {self.surname}\n'


some_student = Student('Ruoy', 'Eman', 'M')
some_student.grades.append(9.9)
some_student.courses_in_progress += ['Python', ', ', 'Git']
some_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy')
# some_lecturer.grades.append(9.9)

# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# student = Student('Алёхина', 'Ольга', 'Ж')
# student.courses_in_progress += ['Python', 'Java']
# lecturer.courses_attached += ['Python', 'C++']
# reviewer.courses_attached += ['Python', 'C++']
# print(student.rate_lecture(lecturer, 'Python', 7))  # None
# print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
# print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
# print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
# print(lecturer.grades)  # {'Python': [7]}
print(some_student)
print(' ')
print(some_lecturer)
print(' ')
print(some_reviewer)