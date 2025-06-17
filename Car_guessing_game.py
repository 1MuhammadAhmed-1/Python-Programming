i = 0
check = 'nothing'
while i < 100:
    choice = input(">")
    if choice.upper() == 'HELP':
        print('start - to start the car')
        print('stop - to stop the car')
        print('exit - to close the game')
    elif choice.upper() == 'START':
        if check == choice:
            print("Car is already started")
        else:
            print('Car started!')
    elif choice.upper() == 'STOP':
        if check == choice:
            print("Car is already stopped")
        else:
            print('Car stopped!')
    elif choice.upper() == 'EXIT':
        print('Game ended!')
        break
    else:
        print("I don't understand what you said")
    check = choice
    i = i + 1
print("Thank you for playing!")