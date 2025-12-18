from random import randint


def roll_dice(amount: int = 2) -> list[int]:
    """
    Generates a list of random dice rolls
    """
    if amount <= 0:
        raise ValueError('Enter a positive number')
    rolls: list[int] = []

    for i in range(amount):
        rolls.append(randint(1, 6))

    return rolls


def main():
        while True:
            try:
                rolls = (input("Enter the number of dice you want to roll ? "))

                if rolls.lower() == 'exit':
                    print('Thanks for playing')
                    exit()

                rlist = roll_dice(int(rolls))
                print(*rlist, sep=', ')

            except ValueError:
                print(f'Please enter a valid value')


if __name__ == "__main__":
    main()
