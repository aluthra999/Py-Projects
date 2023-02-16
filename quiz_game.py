print("Welcome to my Computer Quiz!!!")

playing = input("Do you want to play? (y/n) ")
# if playing == "y":
#     player = input("Name: ")
#     print(f"{player}, Let's begin the game")
# else:
#     print("You choose not to play! But new games are on the way. Stay tuned.")
#     quit()
if playing != "y":
    quit()
else:
    player = input("Name: ")
    print(f"Welcome {player.upper()}, Let's begin the game")
    # print("type all your answers in small cases")
    print("Let the fun begin")

score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    score += 1
    print("Awsome! you got the answer.")
    print("point +1. Total points: " + str(score))
    print("Here the next one")
else:
    print("Incorrect! Better luck next time. Your points are: " + str(score) + " and you got: " + str(score / 5 * 100) + "%")
    quit()


answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    score += 1
    print("Awsome! you got the answer.")
    print("point +1. Total points: " + str(score))
    print("Here the next one")
else:
    print("Incorrect! Better luck next time.")
    print("You got 1 right answer. Your points are: " + str(score) + " and you got: " + str(score / 5 * 100) + "%")
    quit()

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    score += 1
    print("Awsome! you got the answer.")
    print("point +1. Total points: " + str(score))
    print("Here the next one")
else:
    print("Incorrect! Better luck next time.")
    print("You got 2 right answer. Your points are: " + str(score) + " and you got: " + str(score / 5 * 100) + "%")
    quit()

answer = input("What does GUI stands for? ")
if answer.lower() == "graphical user interface":
    score += 1
    print("Awsome! you got the answer.")
    print("point +1. Total points: " + str(score))
    print("Here the next one")
else:
    print("Incorrect! Better luck next time.")
    print("You got 3 right answer. Your points are: " + str(score) + " and you got: " + str(score / 5 * 100) + "%")
    quit()

answer = input("What does AI stands for? ")
if answer.lower() == "artificial intelligence":
    score += 1
    print("Awsome! you got the answer.")
    print("Congralutions, you got all the answers right.")
    print("Total points: " + str(score) + " You got: " + str(score / 5 * 100) + "%")
else:
    print("Incorrect! Better luck next time.")
    print("You got 4 right answer. Your points are " + str(score) + " and you got " + str(score / 5 * 100) + "%")
    quit()
    