# class | object

'''
class DemoClass:
    a=10
    def sumvalue(self):
     print (20+30)

demoobject = DemoClass()
demoobject1 = DemoClass()
print(demoobject.a)
print(demoobject1.a)
demoobject.sumvalue();
'''
# Method | Constructor
# class DemoClass:
#     a=10
#     def __init__(self):             # constructor pre define keyword
#         print("welcome to ktm")
#     def showvalue(self):
#         # print(self.a)
#         self.c=self.a*self.a
#         print(self.c)
#
#     def showvalue1(self,a,b):
#         # print("welcome to ktm")
#         print(a+b)
#
# obj=DemoClass()
# obj.showvalue()
# obj.showvalue1(20,30)


#   Inheritance

# class A:
#     def displayA(self):
#         print("welcome to ktm A")
#
# class B:
#     def displayB(self):
#         print("welcome to ktm B")
#
# class C(A,B):
#     def displayC(self):
#         print("welcome to ktm C")
#
# obj = C()
# obj.displayA()
# obj.displayB()
# obj.displayC()

# Encapsulation (getter and setter)
#   -> An object variables should not always be directly accessible.
#   -> The methods can ensure the correct values are set. if an incorrect value is set, the method can return an error.

# class Student:
#     def __init__(self):
#         self.__name = ""
#     def getname(self):
#         return self.__name
#     def setname(self,name):
#         self.__name=name
#
# obj = Student()
# obj.setname("Testing")
# name = obj.getname()
# print(name)

# private

# class Student:
#     __name="sandesh"
#     def __init__(self):
#         print(self.__name)
#         self.__displayinfo()
#     def __displayinfo(self):
#         print("Welcome to ktm")
# obj = Student()

#   polymorphism : means same function name (but different signatures) being uses for different types.
# l=[10,20,30,40]
# print(len(l))
# s="welcome"
# print(len(s))

# overloading concept
# class ktm:
#     def displayinfo(self,name=''):
#         print("welcome to rr" +name)
#
#
# obj=ktm()
# obj.displayinfo()
# obj.displayinfo(' BCA')

class ktm:
    def displayinfo(self):
        print("Welcome to ktm")
class RR(ktm):
    def displayinfo(self):
        super().displayinfo()   #
        print("Welcome to RR")
obj=RR()
obj.displayinfo()

