"""
Create a nested dictionary of three employees, each with keys for name, age, and salary. 
Write a function to give each employee a 10% raise and print the updated dictionary.
"""
employees = {"emp1":{"name":"ram","age":25,"salary":15000},
             "emp2":{"name":"hari","age":30,"salary":10000},
             "emp3":{"name":"ak","age":32,"salary":20000}}

def emp(a):

    for i in (a):

      a[i]["salary"] += a[i]["salary"] *(10/100)

    print(a)

(emp(a = employees))