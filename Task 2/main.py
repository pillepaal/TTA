print('Welcome to the joke generator!')
number = input('Please choose a number between 1 and 100: ')
number = int(number)
if number <= 20:
    print('Here is your joke: I used to have a handle on life, but then it broke.')
elif number <= 40:
    print('Here is your joke: I know they say that money talks, but all\n mine says is "Goodbye."')
elif number <= 60:
    print('Here is your joke: My wife just found out I replaced our bed with\n a trampoline. She hit the ceiling!')
elif number <= 80:
    print('Here is your joke: Russian dolls are so full of themselves.')
else:
    print('Here is your joke: Just burned 2,000 calories. That’s the last time\n '
          'I leave brownies in the oven while I nap.')
