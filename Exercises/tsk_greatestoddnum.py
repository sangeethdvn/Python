num = [98,111,47,99,36,58,73]

num.sort()

larg = num[0]

print(num)

for i in num:
  
   if (i > larg) and (i%2 ==1):
       
       larg= i

print(larg)