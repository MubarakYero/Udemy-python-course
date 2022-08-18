# import random
# highest = 10
# answer = random.randint(1, highest)

# print("Please guess a number between 1 and {}".format(highest))
# guess = int(input())
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher.")
#     else:
#         print("Please guess lower.")
#     guess = int(input())
#     if guess == answer:
#         print("Great Job!")
#     else:
#         print("Sorry you have not guessed correctly.")
# else:
#     print("You've got it first time.")

import random
highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = ''
guess_attempts = 0
while guess != answer:
    guess = int(input())
    guess_attempts += 1

    if guess_attempts == 5:
        print("Game over")
        break
    elif guess == '':
        print("Please input a number")
    elif guess < answer:
        print("Please guess higher.")
    elif guess > answer:
        print("Please guess lower.")
    elif guess == answer:
        print("Great Job!")
    elif guess == answer:
        print("You've got it first time.")
    else:
        print("Sorry you have not guessed correctly.")


