import random

#bill = float(input("What's the total bill? "))
#tip_percent = float(input("How much tip you want to give: 2.5%, 5%, 10%, 15%? "))
#people = int(input("How many people bill is splitting? "))
name_of_people = input("Type all the names of person giving card: ")

seprate = name_of_people.split(",")

#print(seprate)
pick = random.choice(seprate)
print(f"{pick} will be paying today!!!")

for names in seprate:
    print(f"Thank you {names} for playing")
