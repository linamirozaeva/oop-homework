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























# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
#
#     # Метод для подсчета среднего балла студента по оценкам за домашнюю работу
#     def average_grade(self):
#         all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
#         if len(all_grades) > 0:
#             return sum(all_grades) / len(all_grades)
#         else:
#             return 0
#
#     # Перегрузка метода str для вывода информации о студенте
#     def __str__(self):
#         avg_grade = self.average_grade()
#         courses_in_progress_str = ', '.join(self.courses_in_progress)
#         finished_courses_str = ', '.join(self.finished_courses)
#
#         return f'Имя: {self.name}\\nФамилия: {self.surname}\\nСредняя оценка за домашние задания: {avg_grade:.1f}\\nКурсы в процессе изучения: {courses_in_progress_str}\\nЗавершенные курсы: {finished_courses_str}'
#
#     # Реализация оператора сравнения для студентов по среднему баллу
#     def __lt__(self, other):
#         return self.average_grade() < other.average_grade()
#
#     def rate_lecture(self, lecturer, course, grade):
#         if isinstance(lecturer,
#                       Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
#             if course in lecturer.grades:
#                 lecturer.grades[course].append(grade)
#             else:
#                 lecturer.grades[course] = [grade]
#         else:
#             return 'Ошибка'
#
#
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
#
#
# class Lecturer(Mentor):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#         self.grades = {}  # Словарь оценок лектора по каждому курсу
#
#     # Метод для вычисления среднего рейтинга лекций
#     def average_grade(self):
#         all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
#         if len(all_grades) > 0:
#             return sum(all_grades) / len(all_grades)
#         else:
#             return 0
#
#     # Перегрузка метода str для вывода информации о лекторе
#     def __str__(self):
#         avg_grade = self.average_grade()
#         return f'Имя: {self.name}\\nФамилия: {self.surname}\\nСредняя оценка за лекции: {avg_grade:.1f}'
#
#     # Реализация оператора сравнения для лекторов по среднему рейтингу
#     def __lt__(self, other):
#         return self.average_grade() < other.average_grade()
#
#
# class Reviewer(Mentor):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#
#     # Перегрузка метода str для вывода информации о рецензенте
#     def __str__(self):
#         return f'Имя: {self.name}\\nФамилия: {self.surname}'
#
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course].append(grade)
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
#
#
# print('123')