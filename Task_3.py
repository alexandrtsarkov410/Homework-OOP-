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


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']


some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 9.8)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9.8)

print(some_reviewer)
print(some_lecturer)
print(some_student)

print(some_student == some_student)
print(some_student > some_student)
print(some_student < some_student)
print(some_lecturer == some_lecturer)
print(some_lecturer > some_lecturer)
print(some_lecturer < some_lecturer)
# some_reviewer = Reviewer('Some', 'Buddy')
# print(some_reviewer)
# some_lecturer = Lecturer('Some', 'Buddy')
# some_student.rate_lecture(some_lecturer, 'Python', 7)
# print(some_reviewer)
# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# student = Student('Алёхина', 'Ольга', 'Ж')
#
# student.courses_in_progress += ['Python', 'Java']
# lecturer.courses_attached += ['Python', 'C++']
# reviewer.courses_attached += ['Python', 'C++']
#
# print(student.rate_lecture(lecturer, 'Python', 7))   # None
# print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
# print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
# print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка
#
# print(lecturer.grades)