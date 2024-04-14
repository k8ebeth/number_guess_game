import random

true_number = random.randint(1,100)

guess_number = int(input('Enter your guess between 1 and 100: '))



while True: 
    if guess_number == true_number: 
        print('You are correct! Good Job!')
        break 

    elif guess_number < true_number: 
        print('You guessed too low. Try again.')
        guess_number = int(input('Enter your guess between 1 and 100: '))

    elif guess_number > true_number: 
        print('You guessed too high. Try again.')
        guess_number = int(input('Enter your guess between 1 and 100: '))
    

