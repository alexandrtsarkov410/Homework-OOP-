def calc_avg_student_grade(students, course):
    total = 0
    grades = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            grades += len(student.grades[course])
    if grades:
        return total / grades

def calc_avg_lecturer_grade(lecturers, course):
    total = 0
    grades = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            grades += len(lecturer.grades[course])
    if grades:
        return total / grades


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade_st(self):
        grades = []
        for course in self.grades.values():
            for grade in course:
                grades.append(grade)
        if grades:
            return sum(grades) / len(grades)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade_st():.1f}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {''.join(self.finished_courses)}"

    def __eq__(self, other):
        return self.avg_grade_st() == other.avg_grade_st()

    def __lt__(self, other):
        return self.avg_grade_st() < other.avg_grade_st()

    def __gt__(self, other):
        return self.avg_grade_st() > other.avg_grade_st()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade_lec(self):
        grades = []
        for course in self.grades.values():
            for grade in course:
                grades.append(grade)
        if grades:
            return sum(grades) / len(grades)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade_lec():.1f}'

    def __eq__(self, other):
        return self.avg_grade_lec() == other.avg_grade_lec()

    def __lt__(self, other):
        return self.avg_grade_lec() < other.avg_grade_lec()

    def __gt__(self, other):
        return self.avg_grade_lec() > other.avg_grade_lec()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_1 = Student('Александр', 'Царьков', 'м')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']

student_2 = Student('Юлия', 'Пашкина', 'ж')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Git']

lecturer_1 = Lecturer('Тимур', 'Анвартдинов')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Олег', 'Булыгин')
lecturer_2.courses_attached += ['Python']

reviewer_1 = Reviewer('Александр', 'Бардин')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Валерия', 'Болтунова')
reviewer_2.courses_attached += ['Python']


reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 8)

student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_2, 'Python', 9)
student_2.rate_lecture(lecturer_1, 'Python', 9)
student_2.rate_lecture(lecturer_2, 'Python', 8)

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

print(f"Сравнение студентов: {student_1 > student_2}")
print(f"Сравнение лекторов: {lecturer_1 > lecturer_2}")

print(f"Средняя оценка студентов по курсу 'Python': {calc_avg_student_grade([student_1, student_2], 'Python'):.2f}")
print(f"Средняя оценка лекторов по курсу 'Python': {calc_avg_lecturer_grade([lecturer_1, lecturer_2], 'Python'):.2f}")