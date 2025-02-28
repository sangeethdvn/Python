"""
Create a dictionary of five countries and their capitals.User need to input a  countryname if the country name is in the 
dictionary retrun its capital and if it is not in dicitonary retrun "Not found" 

"""

countries = {"Afghanistan":"Kabul","Albania":"Tirana","Algeria":"Algiers","Andorra":"Andorra la Vella","India":"Delhi"}

country_name = input("Enter a country name: ")

country_name = country_name.capitalize()

if country_name in countries:

    print(countries[country_name])

else :

    print("Not found")