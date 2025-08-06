class A:
    var1 = "Welcome to Fighter class"
class B:
    var2 = "Welcome to Paladins class"
class C(A, B):
    Var3 = "Welcome to Rogues class"

C1 = C()
print(C1.Var3)
# print(C1.var2)
# print(C1.var1)