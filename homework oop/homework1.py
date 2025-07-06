class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        if len(all_grades) > 0: return sum(all_grades) / len(all_grades)
        else: return 0

    def __str__(self):
        avg_grade = self.average_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades: lecturer.grades[course].append(grade)
            else: lecturer.grades[course] = [grade]
        else: return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        if len(all_grades) > 0: return sum(all_grades) / len(all_grades)
        else: return 0

    def __str__(self):
        avg_grade = self.average_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}'

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades: student.grades[course].append(grade)
            else: student.grades[course] = [grade]
        else: return 'Ошибка'


def calculate_average_homework_grade(students, course_name):
    total_sum = 0
    count_students = 0
    for student in students:
        if course_name in student.grades:
            grades_for_course = student.grades.get(course_name)
            total_sum += sum(grades_for_course)
            count_students += len(grades_for_course)
    if count_students > 0: return round(total_sum / count_students, 1)
    else: return None


def calculate_average_lecture_grade(lecturers, course_name):
    total_sum = 0
    count_grades = 0
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            grades_for_course = lecturer.grades.get(course_name)
            total_sum += sum(grades_for_course)
            count_grades += len(grades_for_course)
    if count_grades > 0: return round(total_sum / count_grades, 1)
    else: return None


student1 = Student("Иван", "Иванов", "Мужской")
student2 = Student("Анна", "Петрова", "Женский")

student1.courses_in_progress.extend(["Python", "Java"])
student1.finished_courses.append("C++")
student1.grades["Python"] = [8, 7, 9]
student1.grades["Java"] = [7, 8]

student2.courses_in_progress.extend(["Python", "Ruby"])
student2.finished_courses.append("PHP")
student2.grades["Python"] = [9, 8, 9]
student2.grades["Ruby"] = [8, 7]

lecturer1 = Lecturer("Сергей", "Сергеев")
lecturer2 = Lecturer("Ольга", "Васильева")

lecturer1.courses_attached.extend(["Python", "Java"])
lecturer2.courses_attached.extend(["Python", "Ruby"])

student1.rate_lecture(lecturer1, "Python", 9)
student2.rate_lecture(lecturer1, "Python", 8)
student1.rate_lecture(lecturer2, "Python", 7)
student2.rate_lecture(lecturer2, "Python", 8)

reviewer1 = Reviewer("Михаил", "Смирнов")
reviewer2 = Reviewer("Елена", "Кузнецова")

reviewer1.courses_attached.extend(["Python", "Java"])
reviewer2.courses_attached.extend(["Python", "Ruby"])

reviewer1.rate_hw(student1, "Python", 8)
reviewer1.rate_hw(student2, "Python", 9)
reviewer2.rate_hw(student1, "Ruby", 7)
reviewer2.rate_hw(student2, "Ruby", 8)
