import random
my_number = random.randint(1,10)

n = 0
x = 0
guess = int(raw_input('Guess a number between 1-10:'))
while n < 1:
    x+=1
    if guess == my_number:
        n+=1
    elif guess < my_number:
        print('your number is too low')
        guess = int(raw_input('Guess again between 1-10:'))
    else:
        print('your number is too high!')
        guess = int(raw_input('Guess again between 1-10:'))
print('your number is correct')
print('You guessed it in ' + str(x) + " tries")
