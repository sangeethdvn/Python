# Class Library

class Library():

    def __init__(self):

        self.book=[]

    def add_book(self,b_name,b_author):

        self.b_name=b_name

        self.b_author=b_author

        self.book.append({"name":b_name,"author":b_author})

        print(self.book)

    def rem_book(self,b_name):

        for i in self.book:

            # print(type(i))
            
            if i["name"] == b_name:    #i is <class 'dict'> thats why i ["name"]

                self.book.remove(i)

                print("Book removed successfully")

                print(self.book)

        else:

                print("Book not found")

    def display_book(self,b_author):
         
        # for i in self.book:
            
        #     if i["author"] == b_author: 

        #         print(f"Book details book name is {i["name"]} and author is {i["author"]}")

        #         break

        #     else:
                
        #         print("Book not found")

        result = [i for i in self.book if i["author"] == b_author]     #List comprehension used because if a situation in which there is are more than one book by the same author

        if result:
             
            for i in result:

                print(i)

        else:

            print("Author not found")

obj = Library()

obj.add_book(b_name="Sangee adventure",b_author="Sangee")

obj.add_book(b_name="Onepeice",b_author="Oda")

obj.rem_book(b_name="Sangee ")

obj.display_book(b_author="jn")