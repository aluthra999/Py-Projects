import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&'\()*+/<>;:[]?,._-=|"

while 1:
    password_lenght = int(input("Type the number the lenght you want for your password: "))
    # password_count = int(input("How many passwords you want? : "))
    # for x in range(0, password_count):
    password = ""
    for x in range(0, password_lenght):
        password_char = random.choice(chars) 
        password = password + password_char
    print("Here is you password: ", password)
    quit()
#random.choice will choose 1 random character from chars string while password_lenght in for loop from user's 
#input number make that lenght of charachter, like if user say 10 -> random.choice will choose 10 random 
#charachter and will create a random password
   
