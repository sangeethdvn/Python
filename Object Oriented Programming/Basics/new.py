# creat a class named Student

# method1: Suppose to get mark of subject1 , subject2 and subject3

# method2 : suppose to print average

class Studenr():

    def method1(self, subject1, subject2, subject3):

        self.subject1 = subject1

        self.subject2 = subject2

        self.subject3 = subject3

    
    def method2(self):

        avg = (self.subject1 + self.subject2 + self.subject3)/3

        print(avg)

obj = Studenr()

obj.method1(subject1=75,subject2=99,subject3=45)

obj.method2()