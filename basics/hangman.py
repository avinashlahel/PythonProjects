from random import choice


def hangman():
    word = choice(['apples', 'banana', 'hangman', 'python'])

    name = input('Please enter your name: ')
    print(f'Welcome to hangman {name}')

    tries = 3
    guessed = ''

    while tries > 0:
        unguessed = 0
        for letter in word:
            if letter in guessed:
                print(letter, end='')
            else:
                unguessed += 1
                print('_', end='')

        if unguessed == 0:
            print('\n Great Job! You guessed the word')
            break

        guess = input('\n Enter your guess: ')

        if guess in guessed:
            print('Already guessed, try another letter')
            continue

        if guess not in word:
            tries -= 1
            print(f'Incorrect Attempt, {tries} tries left !')

        guessed += guess

        if tries == 0:
            print('Total Attempts exhausted. Thanks')
            break



if __name__ == '__main__':
    hangman()
