import random

attempts = 0
name = input('Hey! What is your name?: ')
number = random.randint(1, 30)
print ('Okay {0}. I made a number, you can guess'.format(name))

while attempts < 10:
    guess = int(input('Enter a number: '))
    attempts += 1
    if guess < number:
        print ('This number is less')
    if guess > number:
        print ('This number is more')
    if guess == number:
        break
if guess == number:
    print ('Wow, {0}! you guessed the number in {1} attempts'.format(name, attempts))
else:
    print ('I\'m sorry you didn\'t guess it was the number {0}'.format(number))