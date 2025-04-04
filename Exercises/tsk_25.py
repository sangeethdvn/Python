name = input("enter name: ")

length = len(name)


if length <=5:

    sur = input("Enter your sur name: ")

    name = (name.replace(" ", "") + sur.replace(" ", ""))

    print(name.upper())

else:

    print(f"Your name is {name.lower()}")