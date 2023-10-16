from Mentors.Mentor import Mentor

class Reviewer(Mentor): 
    def __init__(self, name, surname) -> None:
       super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if type(student).__name__ != 'Student':
            print('Ошибка. Выставить оценку можно только студенту')
            return
        
        if course not in self.courses_attached:
            print('Ошибка. Ментор не проверяет работы на этом курсе')
            return

        if course not in student.courses_in_progress:
            print('Ошибка. Студент не проходит или уже прошел данный курс')
            return

        if course in student.grades:
                student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]

    def __str__(self) -> str:
        st = ("Имя: " + self.name + "\nФамилия: " + self.surname)
        return st
