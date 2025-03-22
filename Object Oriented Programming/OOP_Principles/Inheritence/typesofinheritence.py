"""     <<<SINGLE INHERITENCE>>>>"""
# ===================================


# class Parent():

#     def vehicle(self):

#         print("Maruti")

# class Child(Parent):

#     def vehicle(self):

#         print("Polo")

#         return super().vehicle()
    
# obj = Child()

# obj.vehicle()

# =====================================================

"""     <<<MULTILEVEL INHERITENCE>>>>"""


# Multilevel inheritence in python allows a classs to inherit properties and methods from a class that is already inheritted from another class


# class A:

#     def m1(self):

#         print("HI")


# class B(A):

#     def m2(self):

#         print("OSU")

# class C(B):

#     def m3(self):

#         print("Oi")

# obj = C()
# obj.m1()


"""     <<<MULTIPLE INHERITENCE>>>>"""

# Derived classes willl be inherited from more than one class


class A:

    def m1(self):

        print("HI")


class B:

    def m2(self):

        print("OSU")

class C(B,A):

    def m1(self):
        print("HI, iam form multople inherited class")
        return super().m1()
    
    def m2(self):
        print("Hello iam")
        return super().m2()
    def m3(self):

        print("Oi, I am from both classes A and B")

        

obj = C()
obj.m2I()
