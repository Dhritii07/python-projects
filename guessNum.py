import random

def guessNum():
    print('Why are you here?')
    print('Nvm')
    print('Think of a number between 1 and 1000')
    print('Note: Cold is for Too Low and Hot is for Too High')
    num = random.randint(1,1000)

    attempts = 0
    correct = False

    while not correct:
        guess = input('Enter your guess: ')

        if not guess.isdigit():
            print('Please enter a valid number.')
            continue

        guess = int(guess)
        attempts += 1

        if guess < num:
            print('Cold')
        elif guess > num:
            print('Hot')
        else:
            print(f"Congrats! You have guessed the number in {attempts} attempts!")
            correct = True

guessNum()
