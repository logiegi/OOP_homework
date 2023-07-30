class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lect, course, grade):
        if isinstance(lect,
                      Lecturer) and course in lect.courses_attached and course in self.courses_in_progress:
            if course in lect.grades:
                lect.grades[course] += [grade]
            else:
                lect.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        if len(self.grades) > 0:
            res = 0
            res2 = 0
            for k, v in self.grades.items():
                res += sum(v)
                res2 += len(v)
            return res / res2
        return 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        return self.average_grades() < other.average_grades()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ,".join(self.finished_courses)}\n'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        if len(self.grades) > 0:
            res = 0
            res2 = 0
            for k, v in self.grades.items():
                res += sum(v)
                res2 += len(v)
            return res / res2
        return 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        return self.average_grades() < other.average_grades()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades()}\n'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, stu, course, grade):
        if isinstance(stu, Student) and course in self.courses_attached and course in stu.courses_in_progress:
            if course in stu.grades:
                stu.grades[course] += [grade]
            else:
                stu.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


# первый студент
best_student1 = Student('Egor', 'Logunov')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['Pascal']
# второй студент
best_student2 = Student('Karina', 'Martynovskaya')
best_student2.courses_in_progress += ['Veterinarian']
best_student2.courses_in_progress += ['Python']

# первый ревьюер
cool_reviewer1 = Reviewer('Oleg', 'Bulikin')
cool_reviewer1.courses_attached += ['Pascal']
cool_reviewer1.courses_attached += ['Python']
# второй ревьюер
cool_reviewer2 = Reviewer('Who', 'You')
cool_reviewer2.courses_attached += ['Veterinarian']

# первый лектор
cool_lecturer1 = Lecturer('Steve', 'Frost')
cool_lecturer1.courses_attached += ['Python']
cool_lecturer1.courses_attached += ['Veterinarian']
# второй лектор
cool_lecturer2 = Lecturer('Mary', 'Jane')
cool_lecturer2.courses_attached += ['Pascal']

# ПРОВЕРКИ
cool_reviewer1.rate_hw(best_student1, 'Python', 9)
cool_reviewer1.rate_hw(best_student1, 'Pascal', 5)
cool_reviewer1.rate_hw(best_student1, 'Python', 7)
cool_reviewer1.rate_hw(best_student1, 'Pascal', 6)

cool_reviewer1.rate_hw(best_student2, 'Python', 5)
cool_reviewer1.rate_hw(best_student2, 'Python', 10)
cool_reviewer2.rate_hw(best_student2, 'Veterinarian', 9)
cool_reviewer2.rate_hw(best_student2, 'Veterinarian', 8)
cool_reviewer2.rate_hw(best_student2, 'Veterinarian', 7)

best_student2.finished_courses += ['Floristry']

best_student1.rate_hw(cool_lecturer1, 'Python', 9)
best_student2.rate_hw(cool_lecturer1, 'Python', 6)
best_student1.rate_hw(cool_lecturer2, 'Pascal', 7)
best_student2.rate_hw(cool_lecturer2, 'Pascal', 8)
best_student1.rate_hw(cool_lecturer1, 'Veterinarian', 9)
best_student2.rate_hw(cool_lecturer1, 'Veterinarian', 8)
print(cool_lecturer1.grades)

print(cool_reviewer1)
print(cool_reviewer2)
print(cool_lecturer1)
print(cool_lecturer2)
print(best_student1)
print(best_student2)

print(best_student1 > cool_lecturer1)
print(best_student1 < cool_lecturer1)
print(best_student1 > cool_lecturer2)
print(best_student1 < cool_lecturer2)

print(best_student2 > cool_lecturer1)
print(best_student2 < cool_lecturer1)
print(best_student2 > cool_lecturer2)
print(best_student2 < cool_lecturer2)

print(best_student1.grades, best_student1.average_grades())
print(best_student2.grades, best_student2.average_grades())
print()
print()

student = [best_student1.grades, best_student2.grades]


# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def average_student(students, course):
    res = []
    for i in students:
        for k, v in i.items():
            if k == course:
                res += v
    return sum(res) / len(res)


print(average_student(student, 'Pascal'))
print(average_student(student, 'Python'))
print(average_student(student, 'Veterinarian'))

lecturer = [cool_lecturer1.grades, cool_lecturer2.grades]


# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def average_lecturer(lecturers, course):
    res = []
    for i in lecturers:
        for k, v in i.items():
            if k == course:
                res += v
    return sum(res) / len(res)


print(cool_lecturer1.grades, cool_lecturer1.average_grades())
print(cool_lecturer2.grades, cool_lecturer2.average_grades())
print()
print()
print(average_lecturer(lecturer, 'Pascal'))
print(average_lecturer(lecturer, 'Python'))
print(average_lecturer(lecturer, 'Veterinarian'))
