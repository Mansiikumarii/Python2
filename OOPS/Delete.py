class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Ujjwal")
print(s1)
print(s1.name)
del s1
del s1.name