# '''a = 2 + 2
# print(a)
#
# print('a ' + 'b')
#
# print('a' + str(42))
#
# print('a' * 5)
#
# spam = 40
# print(spam)
# eggs = 2
# print(spam + eggs + spam)
# spam = spam + 2
# print(spam)
#
# spam = 'a'
# print(spam)
# spam = 'b'
# print(spam)'''
#
# # print('Hello there!' + ' Whats your name?')
# # myName = input()
# # print('Nice to meet you, ' + myName)
# # print('The length of your name is: ' + str(len(myName)))
# # print('Whats your age?')
# # myAge = input()
# # print('You will be ' + str(int(myAge) + 1) + ' in a year!')
# # while True:
# #     again = input('Again? (y/n): ')
# #     if again.lower() != 'y':
# #         break
# #     else:
# #         print('Hello there!' + ' Whats your name?')
# #         myName = input()
# #         print('Nice to meet you, ' + myName)
# #         print('The lenght of your name is: ' + str(len(myName)))
# #         print('Whats your age?')
# #         myAge = input()
# #         print('You will be ' + str(int(myAge) + 1) + ' in a year!')
#
#
# '''print('Hello tell me something random!')
# x = input()
# print(len(x))
# while True:
#     again = input('Again (y/n): ')
#     if again.lower() != 'y':
#         break
#     else:
#         print('Hello tell me something random!')
#         x = input()
#         print(len(x))
# '''
# '''round(3.55, None)
# round(3.555568, 2)
# etc.'''
#
# # bacon = 20
# # print(bacon + 1)
# # print('spam' + 'spamspam')
# # print('spam' * 5)
# # print('I have eaten ' + str(99) + ' burritos')
#
#

# a = int(input('Number:'))
# print('First number:' + str(a) + ' ' + str(type(a)))
# while True:
#     if a%3 == 0:
#         if a%9 == 0:
#             print('right')
#             break
#         print('ok')
#         break
#     else:
#         print('no')
#         break

# Pd for
# list = list(range(0,100))
# a = int(input('Number:'))
# for a in list:
#     if a%3 == 0 and a%9 == 0:
#         print('ok')
#     else:
#         print('Not ok')
#
def Rest(a, b):
    return a%b
liczba = int(input('Liczba:'))
print(Rest(liczba, 9 and 3))