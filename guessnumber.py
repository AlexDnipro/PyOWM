from random import randint

def play():
    number = randint(1,100)
    #print("computer number is", number)
    while True:
        user_number = int(input("Please say a number from 1 to 100:"))

        if user_number < number:
            user_number = int(input("Your number is smaller then should be, please try again:"))
        elif user_number > number:
            user_number = int(input("Your number is bigger then should be, please try again:"))
        elif number == user_number:
            print("Your guess was right!!!")
    

play()
