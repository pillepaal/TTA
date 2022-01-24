import random

random_generated_number = random.randint(1, 10)

# I used the following line to check the number in advance and make sure code works
# print (int(random_generated_number))

name = input('Hello! What is your name? ')
number = input('Please pick a number between 1 and 10: ')
number = int(number)

if random_generated_number == number:
    print('You guessed it! Well done!!!')
else:
    print('Wrong number. Please try again.')

