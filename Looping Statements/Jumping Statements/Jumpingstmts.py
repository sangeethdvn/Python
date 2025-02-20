# while loop =>  CONDITION BASED

# for loop => QUANTITY BASED

#  Used to alter thr flow of loop in both while and for loops

# 3 jumping statements => break, continue, pass

# wap to print form 1 to 10 

for i in range(1, 11):
    print(i)
    if i % 5 == 0:
        break       #break is used to exit a loop when a certaon condition is met!              O/P ==> 1 2 3 4 5



for i in range(1, 11):
    if 1 % 3 == 0:
        continue  # used to skip a  iteration when a condition is met
    else:
        print(i, end=" ")  #    O/P ==> 1 2 4 5 7 8