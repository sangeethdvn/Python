# wap to show the grades

name = input("Enter your name: ")

mark = int(input("Enter your mark: "))

if mark > 100:

    print("Invalid mark")

else:
   
    if (mark >= 90):

        print(f"{name} score A grade")

    elif (mark >= 80) and (mark < 90):

        print(f"{name} score B grade")

    elif (mark >= 70) and (mark < 80):

        print(f"{name} score C grade")

    elif (mark >= 60) and (mark < 70):

        print(f"{name} score D grade")

    elif (mark >= 50) and (mark < 60):

        print(f"{name} score E grade")
    
    else:
        print(f"{name} score Failed")