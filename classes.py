class Course:
    def __init__(self, name: str, num: str, instructor: str = 'TBA', schedule: str, credit: int = 0):
        self.name = name
        self.num = num
        self.credit = credit
        self.instructor = instructor
        department = ''
        for i in self.num: 
            if i not in '1234567890': department += i
        self.department = department
    def __gt__(self, other):
        return self.credit > other.credit
    def __ge__(self, other):
        return self.credit >= other.credit
    def __eq__(self, other):
        return self.num == other.num and self.credit == other.credit
    def __le__(self, other):
        return self.credit <= other.credit
    def __lt__(self, other):
        return self.credit < other.credit
    
    def finish(self, grade):
        self.grade = grade

class Schedule:
    def __init__(self, term: str = '', courses: list = []):
        self.courses = courses
        self.term = term
        self.credit = 0
    def __str__(self):
        return 'Course scheudle for {}\nTaking {} credit hours\nCourses: {}'.format(self.term, self.credit, self.courses)
    def addCourses(self, courses: list):
        for i in courses: 
            self.courses.append(course)
            self.credit += i.credit

class Student:
    def __init__(self, name, grade='freshman'):
        self.name = name
        self.schedules = {}
        self.grade = grade
        self.gpa = 0
    def __str__(self):
        return '{} is a {} student with a {} GPA.'.format(self.name, self.grade, self.gpa)
    def register(schedule: Schedule):
        self.schedules[schedule.term] = schedule
    def calcGPA(self):
        pass

# Fall 2019
fall2019 = Schedule('Fall 2019')

num1011 = Course('Industrial Design Fundamentals 1', 'num1011', 'Sam Harris', 'tr', 2)
num1101 = Course('Intro to Industrial Design 1', 'num1101', 'Steve Chininis', 'm', 1)
num1401 = Course('Intro to Graphic Communication 1', 'num1401', 'Lisa Babb', 't', 1)
num1418 = Course('Intro to Sketching & Modelling 1', 'num1418', 'Dave Lynn', 'r', 1)
num2202 = Course('History of Modern Industrial Design', 'num2202', 'Joyce Medina', 'tr', 3)
apph1040 = Course('Scientific Foundations of Health', 'APPH1040', 'Michele Rosebruck', 'mw')
cee4803 = Course('Origami Engineering', 'CEE4803', 'Glaucio Paulino', 'tr', 3)

fall2019.addCourses([num1011, num1101, num1401, num1418, num2202, apph1040, cee4803])
tynan = Student('Tynan Purdy')


# Spring 2020
cs1301 = Course('Intro to Computing', 'CS1301', 3, 'Dr. Melinda McDaniel', 'mwf')

cs1301.finish(93.63)
