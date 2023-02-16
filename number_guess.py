import random

# randrange will not include 11
# randint will include 11
# random.randrange/randint (start, end) for ex(-1, 11) or (end) (this will automatically start from 0) 
# r = random.randrange(11)
# print(r)

top_of_range = input("Type a number: ")

# isdigit will check if input is a digit in a string then it will convert that string to int
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number greater than 0 next time")
        quit()
else:
    print("Please type a valid number next time")
    quit()

random_number = random.randint(0, top_of_range)
#print(random_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a valid number next time")
        continue

    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess > random_number:
        print("try a smaller number")
    else:
        print("try a bigger number")
    
    # else:
    #     print("You got it wrong")
        # print("Right answer is: " , random_number)
        # print("Right answer is: " +  str(random_number))
        # break

        # to give user a hint about the number according to the user input
        # if user_guess > random_number:
        #     print("try a smaller number")
        # else:
        #     print("try a bigger number")

print("You got it in: ", guesses, " guesses") 