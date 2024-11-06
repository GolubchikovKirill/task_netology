class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_count

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка: студент или курс не совпадают'

    def __str__(self):
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade():.2f}\n'
                f'Курсы в процессе изучения: {courses_in_progress_str}\n'
                f'Завершенные курсы: {finished_courses_str}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

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
        if not self.grades:
            return 0
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_count

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade():.2f}')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Функции для подсчета средней оценки
def average_student_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)
    return 0

def average_lecturer_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)
    return 0

# Пример использования
student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Git']
student1.grades = {'Python': [10, 8, 9]}

student2 = Student('John', 'Smith', 'male')
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Math']
student2.grades = {'Python': [7, 9, 8], 'Git': [10, 10]}

lecturer1 = Lecturer('Jane', 'Doe')
lecturer1.courses_attached += ['Python']
lecturer1.grades = {'Python': [10, 9, 8]}

lecturer2 = Lecturer('Mike', 'Johnson')
lecturer2.courses_attached += ['Git']
lecturer2.grades = {'Git': [9, 7, 8]}

reviewer1 = Reviewer('Alice', 'Brown')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Bob', 'White')
reviewer2.courses_attached += ['Git']

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

# Сравнение объектов
print(student1 > student2)  # False
print(lecturer1 < lecturer2)  # Depends on their average grades

# Подсчет средней оценки
print(f"Средняя оценка за домашние задания по курсу Python: {average_student_grade([student1, student2], 'Python'):.2f}")
print(f"Средняя оценка за лекции по курсу Git: {average_lecturer_grade([lecturer1, lecturer2], 'Git'):.2f}")
