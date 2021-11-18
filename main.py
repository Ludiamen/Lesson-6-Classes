class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
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
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                print(lecturer.grades)
            else:
                lecturer.grades[course] = [grade]
        # else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):


    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.average_rating = float()
        self.grades = {}


    def __str__(self):

        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        # print( grades_count)
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating

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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

#
best_lecturer_1 = Lecturer('Ivan', 'Ivanov')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Petr', 'Petrov')
best_lecturer_2.courses_attached += ['Java']

best_lecturer_3 = Lecturer('Semen', 'Zarev')
best_lecturer_3.courses_attached += ['Python']

cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']
#
cool_reviewer_2 = Reviewer('Ostap', 'Bender')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Java']

student_1 = Student('Denis', 'Sviridov')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Roman', 'Malikov')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Sidor', 'Petrov')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

# student_1.rate_hw(best_lecturer_2, 'Python', 5)
# student_1.rate_hw(best_lecturer_2, 'Python', 7)
# student_1.rate_hw(best_lecturer_2, 'Python', 8)

# student_1.rate_hw(best_lecturer_1, 'Python', 7)
# student_1.rate_hw(best_lecturer_1, 'Python', 8)
# student_1.rate_hw(best_lecturer_1, 'Python', 9)

student_2.rate_hw(best_lecturer_2, 'Java', 10)
student_2.rate_hw(best_lecturer_2, 'Java', 8)
student_2.rate_hw(best_lecturer_2, 'Java', 9)

student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)
#
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


# print(student_1)
# print()
# print(student_3)
# print(student_1.name, student_1.surname, student_1.grades, student_1.finished_courses, student_1.courses_in_progress)
# print()
# print(best_lecturer_1.name, best_lecturer_1.surname, best_lecturer_1.courses_attached, best_lecturer_1.grades)
# print()
# print(cool_reviewer_1.name, cool_reviewer_1.surname, cool_reviewer_1.courses_attached)
# print()
# print(best_lecturer_2)
# print()
# print(cool_reviewer_2)
# print()
# print(student_1)
# print()
# print(student_2)
# print()
# print(student_1 > student_2)
# print()
# print(best_lecturer_1 > best_lecturer_2)

student_list_1 = [student_1, student_2, student_3]
lecturer_list_1 = [best_lecturer_1, best_lecturer_2, best_lecturer_3]


def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        # print(lect)
        if lect.courses_attached == [course_name]:
            # print(lect.courses_attached)
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

# print(student_rating(student_list_1, 'Python'))
print()
print(lecturer_rating(lecturer_list_1, 'Python'))
print()
print(best_lecturer_1.average_rating)
print()
print(best_lecturer_1.grades)
print()
print(best_lecturer_2.average_rating)
print()
print(best_lecturer_2.grades)
print()
print(best_lecturer_3.average_rating)
print()
print(best_lecturer_3.grades)
print()


