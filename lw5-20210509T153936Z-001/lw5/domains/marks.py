class Mark():
    def __init__(self, id_S, id_C, mark):
        self.id_S = id_S
        self.id_C = id_C
        self.mark = mark
    def print_mark(self):
        print("ID student: " +self.id_S)
        print("ID course: " +self.id_C)
        print("mark: " +self.mark)