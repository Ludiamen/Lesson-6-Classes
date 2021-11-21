class Student:
    def __init__(self, name, surname):
        """Перегрузка метода _init_ для определения атрибутов класса Student
        Содержит атрибуты:
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float() """

        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        """Реализует определение средней оценки и возвращает характеристики экземпляра класса вида:
        print(some_student)
        Имя: Ruoy
        Фамилия: Eman
        Средняя оценка за домашние задания: 9.9
        Курсы в процессе изучения: Python, Git
        Завершенные курсы: Введение в программирование
        """

        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):
        """Реализует возможность выставления оценки лектору студентом, если это лектор ведет лекции по данному курсу у этого студента
        Принимает на вход переменные rate_hw(self, lecturer, course, grade)"""

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        """Реализует сравнение через операторы '<,>' студентов между собой по средней оценке за домашние задания"""
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        """Перегрузка метода _init_ для определения атрибутов класса Mentor
        Содержит атрибуты:
        self.name = name
        self.surname = surname
        self.courses_attached = []
        """

        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        """Перегрузка метода _init_ для определения атрибутов класса Mentor
        Содержит атрибуты:
        self.average_rating = float()
        self.grades = {}
        в том числе родительского класса:
        self.name = name
        self.surname = surname
        self.courses_attached = []
        """

        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        """Возвращает характеристики экземпляра класса вида:
            print(some_reviewer)
            Имя: Some
            Фамилия: Buddy
        """
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        """Реализует сравнение через операторы '<,>' лекторов между собой по средней оценке за лекции"""
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """Реализует возможность выставления оценки студенту за домашние задания,
        если этот проверяющий закреплен за этим студентом по данному курсу,
        или возвращает ошибку.
        Принимает на вход переменные rate_hw(self, student, course, grade)"""

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Реализует определение средней оценки и возвращает характеристики экземпляра класса вида:
        print(some_lecturer)
        Имя: Some
        Фамилия: Buddy
        Средняя оценка за лекции: 9.9
        """

        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

# Создаем лекторов и закрепляем их за курсом
best_lecturer_1 = Lecturer('Ivan', 'Ivanov')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Petr', 'Petrov')
best_lecturer_2.courses_attached += ['Java']

best_lecturer_3 = Lecturer('Semen', 'Zarev')
best_lecturer_3.courses_attached += ['Python']

# Создаем проверяющих и закрепляем их за курсом
cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('Ostap', 'Bender')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Java']

# Создаем студентов и определяем для них изучаемые и завершенные курсы
student_1 = Student('Denis', 'Sviridov')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Roman', 'Malikov')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Sidor', 'Petrov')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

# Выставляем оценки лекторам за лекции
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Python', 5)
student_1.rate_hw(best_lecturer_2, 'Python', 7)
student_1.rate_hw(best_lecturer_2, 'Python', 8)

student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 9)

student_2.rate_hw(best_lecturer_2, 'Java', 10)
student_2.rate_hw(best_lecturer_2, 'Java', 8)
student_2.rate_hw(best_lecturer_2, 'Java', 9)

student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)

# Выставляем оценки студентам за домашние задания
cool_reviewer_1.rate_hw(student_1, 'Python', 8)
cool_reviewer_1.rate_hw(student_1, 'Python', 9)
cool_reviewer_1.rate_hw(student_1, 'Python', 10)

cool_reviewer_2.rate_hw(student_2, 'Java', 8)
cool_reviewer_2.rate_hw(student_2, 'Java', 7)
cool_reviewer_2.rate_hw(student_2, 'Java', 9)

cool_reviewer_2.rate_hw(student_3, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)
cool_reviewer_2.rate_hw(student_3, 'Python', 9)
cool_reviewer_2.rate_hw(student_3, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)
cool_reviewer_2.rate_hw(student_3, 'Python', 9)

# Выводим характеристики созданных и оцененых студентов в требуемом виде
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

# Выводим характеристики созданных и оцененых лекторов в требуемом виде
print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
print()

# Выводим результат сравнения студентов по средним оценкам за домашние задания
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

# Выводим результат сравнения лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()

# Создаем список студентов
student_list = [student_1, student_2, student_3]

# Создаем список лекторов
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]


# Создаем функцию для подсчета средней оценки за домашние задания
# по всем студентам в рамках конкретного курса
# в качестве аргументов принимает список студентов и название курса

def student_rating(student_list, course_name):
    """Функция для подсчета средней оценки за домашние задания
    по всем студентам в рамках конкретного курса
    в качестве аргументов принимает список студентов и название курса"""

    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Создаем функцию для подсчета средней оценки за лекции всех лекторов в рамках курса
# в качестве аргумента принимает список лекторов и название курса

def lecturer_rating(lecturer_list, course_name):
    """Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
     в качестве аргумента принимает список лекторов и название курса"""

    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Выводим результат подсчета средней оценки по всем студентам для данного курса
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

# Выводим результат подсчета средней оценки по всем лекорам для данного курса
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()