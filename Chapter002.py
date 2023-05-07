# name = input('Your name: ')
# age = int(input('Your age: '))
# if name == 'Alice':
#     print('Hi, Alice!')
# elif age < 12:
#     print('You are not Alice, kiddo!')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire!')
# elif age > 100:
#     print('You are not Alice, grannie!')
# else:
#     print('You are neither a kiddo, nor a grannie and nor a vampire!')
#
# spam = 0
# while spam < 5:
#     print('ok')
#     spam = spam + 1

# name = ''
# while name != 'Kacper':
#     print('Please, type your name!')
#     name = input()
# print('Thank you')

# while True:
#     print('Type your name!')
#     name = input()
#     if name == 'Kacper':
#         break
# print('Goodbye, thanks!')

# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Kacper':
#         continue
#     print('Hello, Kacper! What is the password (It is a fish)')
#     password = input()
#     if password == 'Swordfish':
#         break
# print('Access granted')

# name = ''
# while not name:
#     print('Enter your name!')
#     name = input()
# print('How many guests will you have?')
# numOfGuests = int(input())
# if numOfGuests:
#     print('Be sure to have enough room for all your guests!')
# print('Done')

# print('My name is:')
# for i in range(5):
#     print('Kacper five times ' + str(i) + '')
#     print('Kacper five times (' + str(i) + ')')

# total = 0
# for num in range(101):
#     total = total + num
# print(total)

# print('My name is')
# i = 0
# while i < 5:
#     print('Kacper five times (' + str(i) + ')')
#     i = i + 1

# for i in range(12, 16):
    # print(i)

# for i in range(0, 10, 2):
    # print(i)

# for i in range(5, -1, -1):
    # print(i)

# import random
# for i in range(5):
    # print(random.randint(1, 10))

# import sys
# while True:
#     print('Type exit to exit!')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')

#Guess a number game.
#
# import random
# print('Hello. What is your name?')
# name = input()
# secretNumber = random.randint(1, 20)
# print('Well, ' + name + ', I am thinking of a number between 1 and 20')
#
# for guessesTaken in range(1, 7):
#     print('Take a guess')
#     guess = int(input())
#     if guess < secretNumber:
#         print('Your guess is too low.')
#     elif guess > secretNumber:
#         print('Your guess is too high')
#     else:
#         break
# if guess == secretNumber:
#     print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken))
# else:
#     print('Nope. The number I was thinking of was ' + str(secretNumber) + ' and you have passed the max repeats, which was 6')
#
# print('Thank for your time! If you want to exit the program, press any button, see you soon!')
# input()

# import random
#
# while True:
#     user_action = input("Enter a choice (rock, paper, scissors): ")
#     possible_actions = ["rock", "paper", "scissors"]
#     computer_action = random.choice(possible_actions)
#     print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
#
#     if user_action == computer_action:
#         print(f"Both players selected {user_action}. It's a tie!")
#     elif user_action == "rock":
#         if computer_action == "scissors":
#             print("Rock smashes scissors! You win!")
#         else:
#             print("Paper covers rock! You lose.")
#     elif user_action == "paper":
#         if computer_action == "rock":
#             print("Paper covers rock! You win!")
#         else:
#             print("Scissors cuts paper! You lose.")
#     elif user_action == "scissors":
#         if computer_action == "paper":
#             print("Scissors cuts paper! You win!")
#         else:
#             print("Rock smashes scissors! You lose.")
#
#     play_again = input("Play again? (y/n): ")
#     if play_again.lower() != "y":
#         break

# import random, sys
#
# print('ROCK, PAPER, SCISSORS')
#
# # These variables keep track of the number of wins, losses, and ties.
# wins = 0
# losses = 0
# ties = 0
#
# while True: # The main game loop.
#     print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
#     while True: # The player input loop.
#         print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
#         playerMove = input()
#         if playerMove == 'q':
#             sys.exit() # Quit the program.
#         if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
#             break # Break out of the player input loop.
#         print('Type one of r, p, s, or q.')
#
#     # Display what the player chose:
#     if playerMove == 'r':
#         print('ROCK versus...')
#     elif playerMove == 'p':
#         print('PAPER versus...')
#     elif playerMove == 's':
#         print('SCISSORS versus...')
#
#     # Display what the computer chose:
#     randomNumber = random.randint(1, 3)
#     if randomNumber == 1:
#         computerMove = 'r'
#         print('ROCK')
#     elif randomNumber == 2:
#         computerMove = 'p'
#         print('PAPER')
#     elif randomNumber == 3:
#         computerMove = 's'
#         print('SCISSORS')
#
#     # Display and record the win/loss/tie:
#     if playerMove == computerMove:
#         print('It is a tie!')
#         ties = ties + 1
#     elif playerMove == 'r' and computerMove == 's':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 'p' and computerMove == 'r':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 's' and computerMove == 'p':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 'r' and computerMove == 'p':
#         print('You lose!')
#         losses = losses + 1
#     elif playerMove == 'p' and computerMove == 's':
#         print('You lose!')
#         losses = losses + 1
#     elif playerMove == 's' and computerMove == 'r':
#         print('You lose!')
#         losses = losses + 1

# spam = int(input())
# if spam == 1:
#     print('Hello')
# elif spam == 2:
#     print('How are you doing?')
# else:
#     print('Cheers!')

# for i in range(1, 11):
    # print(i)

# i = 0
# while i < 11:
#     print(i)
#     i = i + 1

print(abs(-3.22))

# import spam
# spam.bacon()