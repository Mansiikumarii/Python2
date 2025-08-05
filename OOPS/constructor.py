class Student:
    collage_name = "JECRC University"
    name = "anonymous"
    #default constructor
    def __init__(self):
        pass
    name = "Anshul"
    def __init__(self, name, marks):
        self.name = name # obj attribute> class attribute
        # self.name = "Anshul Jain" # this will override the name attribute
        self.marks = marks
        print("adding names in Database")
s1 = Student("Anshul Jain",97)
print(s1)
print(s1.name, s1.marks)
s2 = Student("Shrishti Kumari",99)
print(s2.name, s2.marks)
print(Student.collage_name)