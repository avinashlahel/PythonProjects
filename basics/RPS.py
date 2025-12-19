import sys

from random import choice


class RPS:
    def __init__(self):
        print('Welcome to Rock, paper, scissors')
        self.moves = {'rock': '🪨', 'paper': '📑', 'scissors': '✂️'}
        self.validMoves = list(self.moves.keys())

    def play(self):
        user_move = input('Enter you move (or exit): ').lower()

        if user_move == 'exit':
            print('Thanks for playing')
            sys.exit()

        if user_move not in self.validMoves:
            print('Invalid move, try again')
            return self.play()

        ai_move = choice(self.validMoves)

        self.display(user_move, ai_move)
        self.check(user_move, ai_move)

    def display(self, user_move: str, ai_move: str):
        print(f'You : {self.moves[user_move]}')
        print(f'AI : {self.moves[ai_move]}')

    def check(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print('Its a tie')
        elif (
                (user_move == 'rock' and ai_move == 'scissors')
                or (user_move == 'paper' and ai_move == 'rock')
                or (user_move == 'scissors' and ai_move == 'paper')
        ):
            print('You win')
        else:
            print('AI wins')

        print('---------')


if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play()
