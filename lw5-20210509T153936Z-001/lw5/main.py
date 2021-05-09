import input
import output
from domains.Student import *
from domains.Course import *
from domains.Mark import *

studentL = {}
listSt = []
NoS()


def CreateList_St():
    for i in range(0, nos):
        listSt.append("s" + str(i))


CreateList_St()
In_St()
print_St()
courseL = {}
listC = []
NoC()


def CreateList_C():
    for i in range(0, noc):
        listC.append("s" + str(i))


CreateList_C()
In_C()
print_C()
input_Mark()
print_Mark()
input_student_flies()