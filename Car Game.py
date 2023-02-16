command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started, Where we going?")
    elif command == "stop":
        if not started:
            print("Turn on the car first to stop it.")
        else:
            started = False
            print("Car stopped...")
    elif command == 'help':
        print("""
start - To start the car
stop - To stop the car
quit - To quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry we don't speak gibberish")



# car_start = "START"
# car_stop = "STOP"
# quit_game = "QUIT"
# user_input = input(">")
# if user_input.upper() == car_start:
#     print("Car started")
# elif user_input.upper() == car_stop:
#     print("Car stopped")
# elif user_input.upper() == quit_game:
#     quit()
# else:
#     print("I don't understand")