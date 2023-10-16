from Students.Student import Student
from Mentors.Reviewer import Reviewer
from Mentors.Lecturer import Lecturer

student = Student('Petr', 'Eman', 'your_gender')
student.add_course_progress('Python')
student.add_course_progress('Python')
student.add_course_progress('JavaScript')
student2 = Student('Ivan', 'Eman', 'your_gender')
student2.add_course_progress('Python')

print(student.courses_in_progress)

student.set_course_finished('JavaScript')
student.set_course_finished('JavaScript')
student.add_course_progress('JavaScript')

print(student.courses_in_progress)
print(student.finished_courses)

reviewer = Reviewer('Ivan', 'Ivanov')
reviewer.add_course('Python')
reviewer.add_course('Python')
reviewer.add_course('JavaScript')

reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 9)
print(student.grades)
reviewer.rate_hw(student2, 'Python', 8)
reviewer.rate_hw(student2, 'Python', 9)
reviewer.rate_hw('student', 'Python', 10)
reviewer.rate_hw(student, 'BI', 10)
reviewer.rate_hw(student, 'JavaScript', 10)

lecturer = Lecturer('Petr', 'Petrov')
lecturer.add_course('Python')
lecturer.add_course('BI')
print(lecturer.courses_attached)
lecturer2 = Lecturer('Ivan', 'Petrov')
lecturer2.add_course('Python')

student.rate_lecture(lecturer, 'Python', 10)
student.rate_lecture(lecturer, 'Python', 10)
print(lecturer.courses_grades)
student.rate_lecture(lecturer2, 'Python', 8)
student.rate_lecture(lecturer2, 'Python', 9)

student.rate_lecture(reviewer, 'Python', 10)
student.rate_lecture(lecturer, 'JavaScript', 10)
student.rate_lecture(lecturer, 'BI', 10)
print(lecturer.courses_grades)

# __str__

print(reviewer)
print(lecturer)
print(student)
print(student2)

# func 

def get_avg_range_students_course(students_list:list, course:str):
    sum_ = 0
    count = 0
    for student in students_list:
        if course in student.grades:
            for rate in student.grades[course]:
                sum_ += rate
                count += 1
    return sum_ / count

def get_avg_range_lecturer_course(lecturer_list:list, course:str):
    sum_ = 0
    count = 0
    for lecturer in lecturer_list:
        if course in lecturer.courses_grades:
            for rate in lecturer.courses_grades[course]:
                sum_ += rate
                count += 1
    return sum_ / count 

print('Средняя оценка по курсу Python: ' + str(get_avg_range_students_course([student, student2], 'Python')))
print('Средняя оценка по курсу Python: ' + str(get_avg_range_lecturer_course([lecturer, lecturer2], 'Python')))

