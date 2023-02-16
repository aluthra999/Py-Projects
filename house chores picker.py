import random

persons = input("Add all the names of person: ").upper()

seprate = persons.split(",")

print (f"{seprate} welcome to House Chores task")

atta = random.choice(seprate)
print(f"{atta} is doing Atta")
remove = seprate.remove(atta)
#print(seprate)

sabzi = random.choice(seprate)
print(f"{sabzi} is making Sabzi")
remove = seprate.remove(sabzi)
#print(seprate)

dishes = random.choice(seprate)
print(f"{dishes} will do dishes")
remove = seprate.remove(dishes)
#print(seprate)

cleanup = random.choice(seprate)
print(f"{cleanup} is doing Clean Up after")