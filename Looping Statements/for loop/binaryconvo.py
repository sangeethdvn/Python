n = 5


res =""

while n > 0:

    rem = n % 2

    res = str(rem) + res

    n = n// 2

print(res)