import random

numbers = "0123456789"


area_code = int(input("Your area code: "))
    # while True:
    #     if area_code.isdigit():
    #         area_code = int(area_code)
    #     else:
    #         print("Invalid")
    #         continue

    # if area_code < 3 or area_code > 3:
    #     print(f"{area_code} is not a valid area code, Enter 3 digits only.")
    #     continue
    # else:

while 1:
    numbers_length = 7
    number = ""
    for x in range(0, numbers_length):
        pnumber = random.choice(numbers)
        number = number + pnumber
    print("Your Phone Number is:", area_code,number)
    quit()