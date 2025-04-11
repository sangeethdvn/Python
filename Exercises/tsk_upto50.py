elements = []

sum = 0


while sum <= 50:

    n = int(input("enter element:"))

    sum += n

    if sum > 50:

        break

    else:

        elements.append(n)

print(elements)