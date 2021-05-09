class Student():
    def __init__(self, id, name, dob):
        self.name = name
        self.id = id
        self.dob = dob

    def print(self):
        print("Name student : " + self.name)
        print("ID student : " + self.id)
        print("Dob student : " + self.dob)
