# def hello():
#     print('Hi!')
#     print('Hi!!!')
#     print('Hi guys!')
# hello()
# hello()
# hello()

# def hello(name):
#     print('Hello, ' + name + '!')
# hello('Kacper')
# hello('Peter')
# hello(input())

# import random
# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'Of course'
#     elif answerNumber == 2:
#         return 'Sure'
#     elif answerNumber == 3:
#         return 'Yes'
#     elif answerNumber == 4:
#         return 'Not sure'
#     elif answerNumber == 5:
#         return 'Ask me later'
#     elif answerNumber == 6:
#         return 'Think about it again and answer'
#     elif answerNumber == 7:
#         return 'My answer is no'
#     elif answerNumber == 8:
#         return 'It looks not good'
#     elif answerNumber == 9:
#         return 'Very bad'
# print(getAnswer(random.randint(1, 9)))

# spam = print('Hello!')
# print(None == spam)

# print('Hello, ', end = '')
# print('world!')
#
# print('cats', 'dogs', 'mouses')
# print('cats', 'dogs', 'mouses', sep = ', ')
# print('cats', 'dogs', 'mouses', sep = ',')

# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)
# def bacon():
#     ham = 101
#     eggs = 0
# spam()

# def spam():
#     print(eggs)
# eggs = 42
# spam()
# print(eggs)

# def spam():
#     eggs = 'Local scope spam()'
#     print(eggs)
# def bacon():
#     eggs = 'Local scope bacon()'
#     print(eggs)
#     spam()
#     print(eggs)
# eggs = 'Global scope'
# bacon()
# print(eggs)

# def spam():
#     global eggs
#     eggs = 'spam'
# eggs = 'Global scope'
# spam()
# print(eggs)

# def spam():
#     global eggs
#     eggs = 'spam'
# def bacon():
#     eggs = 'bacon'
# def ham():
#     print(eggs)
# eggs = 42
# spam()
# print(eggs)

# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error, failure argument')
# print(spam(2))
# print(spam(0))
# print(spam(21))
# print(spam(42))

# import random
# secretNumber = random.randint(1, 20)
# print('Guess the number between 1 and 20')
# for guessesTaken in range(1, 7):
#     userGuess = int(input())
#     if userGuess > secretNumber:
#         print('Too high')
#     elif userGuess < secretNumber:
#         print('Too low')
#     else:
#         break
# if userGuess == secretNumber:
#     print('Awesome! You guessed my number which was ' + str(secretNumber))
# else:
#     print('Unlucky, maybe next time!')

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number//2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result
number = input("Give me a number: ")
while number != 1:
    number = collatz(int(number))