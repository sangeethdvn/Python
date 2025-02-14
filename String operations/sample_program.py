company_name = "luminartechnolab"   #LuminarTechnoLab
                                    #0123456789
t= company_name[0]


t = t.upper()
# print(t)

u = company_name[7]

u = u.upper()


print( t + company_name[1:7] + u + company_name[8::])

# print(company_name.split("a"))  # it is used to split the string

print(company_name[0:7].capitalize() + company_name[7::].capitalize())