# itemsofdi = {"name" :"SAngeeth", "sex":"male", "age":"99"}

# for i in itemsofdi:

#     print(f"{i}:{itemsofdi[i]}")

# print(itemsofdi.pop("name"))

# print(itemsofdi["sex"])


# =================================================================================================

student_details = {"name" :"vinay", "age" :22 , "course" : "python", "cgpa" : 8.2}

print(student_details.get("age"))

student_details["course"] = "FullStack" #can be updated and added from here itself

print(student_details)

student_details["place"] = "Switzerland" #new key and value is added

print(student_details)

print(student_details["name"])