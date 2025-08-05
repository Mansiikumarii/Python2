class student:
    #constructor
    def __init__(self,fullname,marks):
        self.fullname = fullname
        self.marks = marks
    def hello(self):
        print("Hello", self.fullname)
    def welcome(self):
        print("Welcome to the class", self.fullname)
    def get_marks(self):
        return self.marks
    def get_avg(self):
        sum =0
        for i in self.marks:
            sum += i
        print("Hi",self.fullname,"your average marks are",sum/len(self.marks))
    #methods
s1 = student("Kinjal",[60,99,98,97])
s1.hello()
s1.welcome()
print(s1.get_marks())
s1.get_avg()