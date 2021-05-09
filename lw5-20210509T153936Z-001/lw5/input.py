import math
from domains.Student import *
from domains.Course import *
from domains.Mark import *

from lw4.main import listSt


class input():
    def NoS(self):
        global nos

    nos = int(input("Number of Students: "))

    def In_St(self):
        print("Enter Student Information: ")

    for i in range(0, nos):
        print("Student " + str(i + 1))
        id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        DoB = input("Enter Student DoB: ")
        inst(id, name, DoB)
        listSt[i] = Student(id, name, DoB)

    def NoC(self):
        global noc

    noc = int(input("number of Course: "))

    def In_C(self):
        print("Enter Course Information: ")

    for i in range(0, noc):
        print("Course " + str(i + 1))
        id = input("ID: ")
        name = input("Name : ")
        cd = input("credits :")
        inCo(id, name, cd)
        listC[i] = Course(id, name, cd)

    def input_Mark(self):
        id_s = input("Enter Student'ID to input Mark: ")

    if id_s in studentL:
        id_c = input("Enter Course'ID to input Mark: ")
        if id_c in courseL:
            mark = math.floor(float(input("mark: ")))
            listMark = Mark(id_s, id_c, mark)

    def input_student_file(self):
        fst = open("students.txt", "r+")
        for Student in listSt:
            fst.write(Student.id)
            fst.write(Student.name)
            fst.write(Student.DoB)
        fst.close()

        fc = open("courses.txt", "r+")
        for course in listC:
            fc.write(Course.id)
            fc.write(Course.name)
        fc.close()

        fm = open("marks.txt", "r+")
        fm.write(mark.id_s)
        fm.write(mark.id_c)
        fm.write(str(mark.mark))
        fm.close()