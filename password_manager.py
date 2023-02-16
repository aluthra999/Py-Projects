pwd = input("Master Password: ")

def view():
    with open('password.txt', "r") as f:
        for line in f.readlines():
            # data = line.rstrip()
            # user, passw = data.split("|")
            # print("User:", user, ", Password:", passw)
            print(line.rstrip())

def add():
    name = input("Name: ")
    pswd = input("Password: ")

    with open('password.txt', "a") as f:
        f.write('Account name: ' + name + " " + "|" + ' Password: ' + pswd + '\n')

while True:
    mode = input("Add or View (add/view): ").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid option")
        continue