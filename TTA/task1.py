import random

random_generated_number = random.randint(1, 10)

 #next line code was done to check the code, if it works if i do guess the number.
 #print(int(random_generated_number))

name = input('What is your name? ')
number = input('Pick a number between 1 and 10 ')
number = int(number)

if random_generated_number == number:
    print('You guessed it!!! Well done!!!')
else:
    print('Sorry, wrong answer. Try again.')




