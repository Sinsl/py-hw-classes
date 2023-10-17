# from Mentors.Lecturer import Lecturer

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_course_progress(self, course_name):
        if course_name in self.courses_in_progress:
            print('Ошибка. Такой курс уже есть')
            return
        
        if course_name in self.finished_courses:
            print('Ошибка. Этот курс уже пройден')
            return

        self.courses_in_progress.append(course_name)


    def set_course_finished(self, course_name):
        if course_name not in self.courses_in_progress:
            print('Ошибка. Нельзя закончить курс, который не был пройден')
            return

        self.courses_in_progress.remove(course_name)
        self.finished_courses.append(course_name)


    def rate_lecture(self, lecturer, course, grade):
        if type(lecturer).__name__ != 'Lecturer':
            print('Ошибка. Ментор не является лектором')
            return

        if course not in lecturer.courses_attached:
            print('Ошибка. Лектор не преподает на данном курсе')
            return

        if course not in self.courses_in_progress:
            print('Ошибка. Студент не проходит данный курс')
            return

        if course in lecturer.courses_grades:
            lecturer.courses_grades[course] += [grade]
        else:
            lecturer.courses_grades[course] = [grade]

    def __str__(self) -> str:
        st = ("Имя: " + self.name + "\n"
        "Фамилия: " + self.surname + "\n"
        "Средняя оценка за домашние задания: " + str(self.__get_avg_grades()) + "\n"
        "Курсы в процессе изучения: " + ', '.join(self.courses_in_progress) + "\n"
        "Завершенные курсы: " + ', '.join(self.finished_courses) + "\n")
        return st

    def __get_avg_grades(self):
        if self.grades:
            sum_ = 0
            count = 0
            for key in self.grades.keys():
                for num in self.grades[key]:
                    sum_ += num
                    count += 1
            return sum_ / count
        else:
            return 0

    def check_type(self, other):
        return isinstance(other, Student)

    # ==
    def __eq__(self, other):
        if self.check_type(other):
            return self.__get_avg_grades() == other.__get_avg_grades()
        else:
            return False

    # !=
    def __ne__(self, other):
        if self.check_type(other):
            return self.__get_avg_grades() != other.__get_avg_grades()
        else:
            return False

    # <
    def __lt__(self, other):
        if self.check_type(other):
            return self.__get_avg_grades() < other.__get_avg_grades()
        else:
            return False

    # >
    def __gt__(self, other):
        if self.check_type(other):
            return self.__get_avg_grades() > other.__get_avg_grades()
        else:
            return False

    # <=
    def __le__(self, other):
        if self.check_type(other):
            return self.__get_avg_grades() <= other.__get_avg_grades()
        else:
            return False

    # >=
    def __ge__(self, other):
        if self.check_type(other):
            return self.__get_avg_grades() >= other.__get_avg_grades()
        else:
            return False