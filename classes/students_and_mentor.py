import statistics


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lect(self, lecturer, course, grade):  # Выставляем оценки лекторам
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def aver(self):  # Рассчитываем средний бал по экзмепляру студента
        grad = []
        for curse in self.grades:
            for i in self.grades[curse]:
                grad.append(i)
        avg = statistics.mean(grad)
        return round(avg, 2)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.aver()} ' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)} '
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого студента')
            return
        return self.aver() < other.aver()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def aver(self):  # Рассчитываем средний бал по экзмепляру Лектор
        grad = []
        for curse in self.grades:
            for i in self.grades[curse]:
                grad.append(i)
        avg = statistics.mean(grad)
        return round(avg, 2)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.aver()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого Лектора')
            return
        return self.aver() < other.aver()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):  # Выставляем оценки студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


def avg_all_students(students, course):
    grad = []
    for student in students:
        for i in student.grades[course]:
            grad.append(i)
    avg = statistics.mean(grad)
    return round(avg, 2)


def avg_all_lecturer(lecturers, course):
    grad = []
    for lecturer in lecturers:
        for i in lecturer.grades[course]:
            grad.append(i)
    avg = statistics.mean(grad)
    return round(avg, 2)


best_student = Student('Ruoy Student', 'Eman Student', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']

best_student2 = Student('Student2', 'Student2', 'your_gender1')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Java']

col_reviewer = Reviewer('Some Reviewer', 'Buddy Reviewer')
col_reviewer.courses_attached += ['Python']
col_reviewer.courses_attached += ['Java']

col_reviewer2 = Reviewer('Some Reviewer2', 'Buddy Reviewer2')
col_reviewer2.courses_attached += ['Python']
col_reviewer2.courses_attached += ['Java']

col_lecturer = Lecturer('Some Lecturer', 'Buddy Lecturer')
col_lecturer.courses_attached += ['Python']
col_lecturer.courses_attached += ['Java']

col_lecturer2 = Lecturer('Tue Lecturer2', 'Tue Lecturer2')
col_lecturer2.courses_attached += ['Python']
col_lecturer2.courses_attached += ['Java']

col_reviewer.rate_hw(best_student, 'Python', 10)
col_reviewer.rate_hw(best_student, 'Python', 3)
col_reviewer.rate_hw(best_student, 'Python', 5)
col_reviewer.rate_hw(best_student, 'Java', 1)


best_student.rate_lect(col_lecturer, 'Python', 5)
best_student.rate_lect(col_lecturer, 'Python', 10)
best_student.rate_lect(col_lecturer, 'Java', 2)

col_reviewer.rate_hw(best_student2, 'Python', 10)
col_reviewer.rate_hw(best_student2, 'Python', 10)
col_reviewer.rate_hw(best_student2, 'Python', 10)
col_reviewer.rate_hw(best_student2, 'Java', 5)

best_student.rate_lect(col_lecturer2, 'Python', 1)
best_student.rate_lect(col_lecturer2, 'Python', 1)
best_student.rate_lect(col_lecturer2, 'Java', 1)

# Задание № 3. Полиморфизм и магические методы 1. Перегрузите магический метод __str__ у всех классов.
print(col_reviewer)
print(col_lecturer)
print(best_student)

# Задание № 3. Полиморфизм и магические методы 2. Реализуйте возможность сравнивать (через операторы сравнения) между
# собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.
print(col_lecturer2 < col_lecturer)
print(best_student2 < best_student)

# Задание № 4. Полевые испытания
print(avg_all_students([best_student, best_student2], 'Python'))
print(avg_all_lecturer([col_lecturer2, col_lecturer], 'Java'))