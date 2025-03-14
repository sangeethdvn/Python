# class Student():

#     def user_data(self,name, place):

#         self.name = name

#         print("entered successfully")

#     def display(self):

#         print(self.name)


# obj1 = Student()

# print(type(obj1))       #<class '__main__.Student'>  here its a "main" because its a custom made class 

# obj2 = Student()

# obj3 = Student()

# obj4 = Student()

# =================================================================================================

class Student():

    
    def __init__(self,name, place):         #calls auto when a object is created =====>>>>> consturctor
        
        self.name = name

        print("entered successfully")

    def display(self):

        print(self.name)




obj1 = Student(name="san", place="Indonesian")  #calls auto when a object is created
                                                #there us no need for the extra line "obj1.user_dats(----------Parameters-----------)"

                                                