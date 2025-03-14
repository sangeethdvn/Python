"""
Create a class Details

method1 (name, place, course)

method2 >> print name and place
"""

# class Details:

#     def method1(self, name, place, course):             # self is used to pass the value of some parameter value b/w other methods
        
#         self.name = name

#         self.place = place

#         self.course = course

#         print("WELCOME")

    
#     def method2(self):

#         print(self.name,self.place)


# obj1 = Details()

# obj1.method1(name = "Sangeeth", place = "Cheruthurthy", course = "Python Django") #||

# obj1.method2()

# ===================================================================================================================

class Details:

    def user(self , name, place, course):

        self.name = name

        self.place = place

        self.course = course 

        print("Thank you")

    def greeting(self):

        print(self.name,self.course)


obj1 =  Details()

obj2 = Details()

obj3 = Details()

obj1.user(name="Sayoo", place="CTY", course="PY")

obj1.greeting()

obj2.user(name="Sree", place="ty", course="java")  #||"name="Sree", place="ty", course="java""===>> attributes
                                                    #attributes are assigned to the obj2 and they share in between methods to self,which sharebetween other methods

obj2.greeting()

obj3.user(name="saha", place ="hs", course = "django")

obj3.greeting()

"""

Self will keep the value as  attributes for  the respective objects.
whenever called it will fetch the coresponding values. 


"""






