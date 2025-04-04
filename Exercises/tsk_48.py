name = input("Enter your name: ")

count = 1


i=input(f"{name} has  been invited to join the party, do you wish to invite someone else with your name [y/n]; ")

while i == "y":
    
    j = input("Enter the name of your invite: , type 'none' if there is no one: ")
    
    count += 1

    if j=="none":
       
        break

print(f" Total number of guests: {count }")