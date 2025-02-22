numbers =  [3,2,6,12,8,10]

ev_sum = 0

od_sum = 0

for i in numbers:

    if i % 2 == 0:

        ev_sum += i

    else:

        od_sum += i

print("Even sum: ", ev_sum)

print("Odd sum: ", od_sum)  