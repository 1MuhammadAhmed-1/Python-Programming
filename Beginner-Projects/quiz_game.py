print("Welcome to my computer game")

playing = input('Do you want to play? ' )
if playing.lower() != 'yes':
    quit()

print("Sweet! Let's play.")
number_of_questions = 0
correct_score = 0
wrong_score = 0

play = input("What does CPU stand for? ")
number_of_questions += 1
if(play.lower() == 'central processing unit'):
    print("Correct!")
    correct_score += 1
else:
    print("Wrong!")
    wrong_score += 1

play = input("What does GPU stand for? ")
number_of_questions += 1
if(play.lower() == 'graphics processing unit'):
    print("Correct!")
    correct_score += 1
else:
    print("Wrong!")
    wrong_score += 1

play = input("What does RAM stand for? ")
number_of_questions += 1
if(play.lower() == 'random access memory'):
    print("Correct!")
    correct_score += 1
else:
    print("Wrong!")
    wrong_score += 1

play = input("What does PSU stand for? ")
number_of_questions += 1
if(play.lower() == 'power supply'):
    print("Correct!")
    correct_score += 1
else:
    print("Wrong!")
    wrong_score += 1

print("Result!")
print("Correct answers!")
print(f"{correct_score} out of {number_of_questions}")
print("Wrong answers!")
print(f"{wrong_score} out of {number_of_questions}")
