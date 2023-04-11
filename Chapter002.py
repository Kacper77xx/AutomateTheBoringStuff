name = input('Your name: ')
age = int(input('Your age: '))
if name == 'Alice':
    print('Hi, Alice!')
elif age < 12:
    print('You are not Alice, kiddo!')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire!')
elif age > 100:
    print('You are not Alice, grannie!')
else:
    print('You are neither a kiddo, nor a grannie and nor a vampire!')
