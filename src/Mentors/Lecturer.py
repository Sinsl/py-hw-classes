from Mentors.Mentor import Mentor

class Lecturer(Mentor): 
    def __init__(self, name, surname) -> None:
        super().__init__(name, surname)
        self.courses_grades = {}

    def __str__(self) -> str:
        st = ("Имя: " + self.name + "\n"
        "Фамилия: " + self.surname + "\n"
        "Средняя оценка за лекции: " + str(self.__get_avg_grades()) + "\n")
        return st

    def __get_avg_grades(self):
        if self.courses_grades:
            sum_ = 0
            count = 0
            for key in self.courses_grades.keys():
                for num in self.courses_grades[key]:
                    sum_ += num
                    count += 1
            return sum_ / count
        else:
            return 'У лектора нет оценок'

    def check_type(self, other):
        return isinstance(other, Lecturer)

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

