import random

random_number = input("Enter a number: ")
if(random_number.isdigit()):
    random_number = int(random_number)

    if(random_number < 0):
        print("Sorry, you can't enter a negative number.")
        quit()

else:
    print("Please enter a numeric value next time.")
    quit()

r = random.randint(0, random_number)
print(r)

print("You have 3 tries to guess the number generated between zero and " + str(random_number))
for i in range(3):
    guess = int(input("Guess: "))
    if(guess == random_number):
        print("Congratulations! you guessed it.")
        quit()
else:
    print("Better luck next time")