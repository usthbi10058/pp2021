from domains.Student import *
from domains.Course import *
from domains.Mark import *
from lw4.main import listSt, listC


class output():
    def print_St(self):
        print("All Students: ")
        for i in range(0, nos):
            print("Student " + str(i + 1))
            listSt[i].print_St()

    def print_C(self):
        print("ALL Courses")

    for i in range(0, noc):
        print("Course " + str(i + 1))
        listC[i].print_C()

    def print_Mark(self):
        print("mark information: ")

    listMark.print_mark()