# file handlingin pyhton involves operations such as creating , reading,  writing and closing files,
# utilizing the vavrious mode to manage data

"""
read()   ==> "r"   read()

write() ==> "w"      write()

append() ==> "a"       write()

open(filename, "r)

"""

# file = open("new.txt","r")

# print(file.read())

# /============================================================================================9

"""write() ==> """

# file = open("new.txt","w")

# file.write("Gadagdagi <3 gadagadoo") #if there is a existing file this operation will overwrite the existing file
                                  #if there is no existing file , a new file is created and the contents of the this write will be presented


# =================================================================================================


"""<<< append >>>"""

# file =open("new.txt","a")

# file.write(" 78984")

# file.write(str(list(range(1,11))))


# /============================================================================================

# items = [1,True,"Hello",5.6]

# file = open("data.txt","w")

# for i in items:

#     file.write(str(i))


# /============================================================================================

# file = open("data.txt","r")

# result = file.read()

# print(result)

# print(len(result.split()))

# /============================================================================================

# file= open("data.txt","r")

# result = file.read().split(" ")

# n = input("Enter the word")

# print(result.count(n))    #because since we used split here and the result of split is in a list (which is always usal) and ".count" is a method of lists


# if n not in result:

#     print("NOt found")

# /============================================================================================


# ["python" ,"is", "a", "programming","Language","used", "to", "create", "web", "applications"]

# file = open("data.txt")

# print(list(set(file.read().split(" "))))

# /============================================================================================


# file = open("C:/Users/sange/OneDrive/Desktop/luminaPy/Collections/LIst Comprehension/task.txt","w")   #<< ctrl + D befor selcting "\" it should either be "\\" or all should be "/" >>

# file.write("Python version is  greater than")

# /============================================================================================


# file = open("new.txt", "r")
   
# # print(file.readline())   #only to read first in the file

# print(file.readlines())    #each line will be represnted as a elment in a list

# print(file.readable()) #O/p true or  false based on whether the file is readable or not

# /============================================================================================

# with open("new.txt", "r") as file:

#     print(file.read())

    #file .close | with >> it ensures that cloes() works right after processing this "with"

# /============================================================================================


# with open("small.txt","r") as file:

#     result = file.read()

# with open("data.txt","w") as file:

#     file.write(result)

# # /============================================================================================

# with open("small.txt","r+") as file:

#     print(file.read())

#     file.write("hello Python")

# ===============================================================================================

# with open("new.txt","r") as file:

#     dic={}

#     ip = file.read()

#     # print(ip.split(" "))

#     for i in ip.split("\n"):

#        for j in i.split(" "):
           
           

               


           
            















