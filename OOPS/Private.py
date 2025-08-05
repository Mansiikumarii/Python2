class Account:
    __name = "Shrishti"
    def __init__(self,acc_no,acc_pass):
       
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    def reset_pass(self):
        print("Resetting password...", self.__acc_pass)
    def __hello(self):
        print("Hello, this is a private method.")
# method and can access the private attribute
    def welcome(self):
        print("Welcome to the bank account system!")
        self.__hello()  # Calling the private method within a public method

acc1 = Account(678901234567, "DtCtw5gJwHRHM1E")
print(acc1.acc_no)
# The following line will raise an AttributeError because __acc_pass is private
# print(acc1.__acc_pass)  # Uncommenting this line will raise an error
acc1.reset_pass()  # This will work as reset_pass is a public
acc1.welcome()  # This will work as welcome is a public method