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

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
                course in self.courses_in_progress and grade <= 10:
            lecturer.grades += [grade]
        else:
            return print("Ошибка")

    def get_avg_grade(self):
        sum_hw = 0
        count = 0
        if self.grades:
            for grades in self.grades.values():
                sum_hw += sum(grades)
                count += len(grades)
            return round(sum_hw / count, 2)
        else:
            return print('Нет оценок')

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за ДЗ: {self.get_avg_grade()} \n' \
              f'Курсы в процессе изучения: {self.courses_in_progress} \n' \
              f'Завершенные курсы: {self.finished_courses} \n'
        return res

    def __lt__(self, second_student):
        if not isinstance(second_student, Student):
            print('Такого студента нет')
            return
        else:
            compare = self.get_avg_grade() < second_student.get_avg_grade()
            if compare:
                print(f'{self.name} {self.surname} учится хуже, чем {second_student.name} {second_student.surname}')
            else:
                print(f'{second_student.name} {second_student.surname} учится хуже чем {self.name} {self.surname}')
        return compare


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за лекции: {sum(self.grades) / len(self.grades) :.2f} \n'
        return res

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n'
        return res

    def __lt__(self, second_lecturer):
        if not isinstance(second_lecturer, Lecturer):
            print('Такого лектора нет')
            return
        else:
            compare_lect = sum(self.grades) / len(self.grades) < sum(second_lecturer.grades) / len(
                second_lecturer.grades)
            if compare_lect:
                print(f'{self.name} {self.surname} хуже {second_lecturer.name} {second_lecturer.surname}')
            else:
                print(f'{second_lecturer.name} {second_lecturer.surname} хуже {self.name} {self.surname}')
        return compare_lect


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
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n'
        return res


def get_avg_hw_grade(student_list, course):
    total_sum = 0

    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                total_sum += sum(grades) / len(grades)
    return round(total_sum / len(student_list), 2)


def get_avg_lec_grade(lecturer_list):
    total_sum = 0
    for lecturer in lecturer_list:
        total_sum += sum(lecturer.grades) / len(lecturer.grades)
    return round(total_sum / len(lecturer_list), 2)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']

next_student = Student('Vlad', 'Cepes', 'M')
next_student.courses_in_progress += ['Python']
next_student.courses_in_progress += ['Git']
next_student.grades['Python'] = [5, 5, 9]
next_student.grades['Git'] = [5]

first_reviewer = Reviewer('Abraham', 'Helsing')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Git']

first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(next_student, 'Python', 8)
first_reviewer.rate_hw(best_student, 'Git', 10)
first_reviewer.rate_hw(next_student, 'Git', 7)

first_lecturer = Lecturer('Lucy', 'Westerna')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']

next_lecturer = Lecturer('Jonatan', 'Harker')
next_lecturer.courses_attached += ['Python']
next_lecturer.courses_attached += ['Git']

best_student.rate_lecturer(first_lecturer, 'Python', 10)
best_student.rate_lecturer(next_lecturer, 'Git', 8)
next_student.rate_lecturer(first_lecturer, 'Python', 6)
next_student.rate_lecturer(next_lecturer, 'Git', 9)

print(best_student.grades)
print(next_student.grades)
print(first_lecturer.grades)
print(next_lecturer.grades)
print(next_student < best_student)
print(first_lecturer < next_lecturer)
print(next_student)
print(first_reviewer)
print(next_lecturer)
print(get_avg_hw_grade([best_student, next_student], 'Python'))
print(get_avg_hw_grade([best_student, next_student], 'Git'))
print(get_avg_lec_grade([first_lecturer, next_lecturer]))
