class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getDob(self):
        return self.dob

    def input(self):
        self.id = input("Student ID: ")
        self.name = input("Student Name: ")
        self.dob = input("Student Birthday: ")

    def __str__(self):
        return "Student: " + self.name + " has id is " + self.id + " has birthday on " + self.dob

    def description(self):
        print(self.__str__())


class Mark:
    def __init__(self, name, course, mark=0):
        self.name = name
        self.course = course
        self.mark = mark

    def input(self):
        print("Student: {self.name} mark ")
        self.mark = input("in {self.course}: ")

    def getMark(self):
        return self.mark

    def getCourse(self):
        return self.course

    def getName(self):
        return self.name

    def __str__(self):
        return "Student " + self.name.TakeName() + " : Mark of " + str(self.mark) + " in course of " + self.course

    def description(self):
        print(self.__str__())


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def input(self):
        self.id = input("Course Id: ")
        self.name = input("Course Name: ")

    def __str__(self):
        return "Course: " + self.name + " has id:  " + self.id

    def description(self):
        print(self.__str__())


Listst = []
ListCourse = []
Marks = []

totalstd = int(input("Enter number of Students: "))

for i in range(totalstd):
    st = Student()
    st.input()
    Listst += [st]

for student in Listst:
    print(student)

totalcourse = int(input("Enter number of Courses: "))

for i in range(totalcourse):
    course = Course()
    course.input()
    totalcourse += [course]

for c in ListCourse:
    print(c)


def Choosecourse():
    Course = input("Enter the course name: ")
    return Course


def inputMark(Course):
    for i in range(totalcourse):
        if Course == ListCourse[i].getName():
            for j in range(totalstd):
                m = Mark(Listst[j].getName(), ListCourse[i].getName())
                m.input()
                Marks.append(m)


def outputMark(Course):
    for mark in Marks:
        if mark.getCourse() == Course:
            print([mark.getName(), mark.getMark()])

inputMark(Choosecourse())
outputMark(Choosecourse())