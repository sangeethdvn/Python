word = input("Enter a word: ")

w_c ={}

for i  in word: #REGULATE

    w_c[i] = word.count(i)   #{'r': 1, 'e': 2, 'g': 1, 'u': 1, 'l': 1, 'a': 1, 't': 1}

print(w_c)

kangaroo = input("enter a kangaroo word:") #RATE

for j in kangaroo:

    if j in w_c and w_c[j] > 0:

        w_c[j] -= 1

    else:

        print("Not a kangaroo word")
        
        break

else:

    print("kangaroo word")



