class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_course(self, course_name):
        if course_name not in self.courses_attached:
            self.courses_attached.append(course_name)
        else:
            print('Ошибка. Ментор уже ведет данный курс')

