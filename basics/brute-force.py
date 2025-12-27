from itertools import product
import string


def common_words(word) -> str | None:
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()

        for i, match in enumerate(words, start=1):
            if match == word:
                return f'Common word found {match} at ({i})'

    return None


def brute_force(word: str, length: int, digits: bool, symbol: bool) -> str | None:
    search_str = string.ascii_lowercase

    if digits:
        search_str += string.digits

    if symbol:
        search_str += string.punctuation

    attempt = 0
    for itr_word in product(search_str, repeat = length):
        fin_word = ''.join(itr_word)
        attempt +=1
        if word == fin_word:
            return f'Found word {fin_word} in {attempt} attempt'

    return 'Word could not be brute forced'


if __name__ == '__main__':
    my_pass = 'main'

    if common := common_words(my_pass):
        print(f'Found common work {my_pass}')
    elif brute := brute_force(my_pass, len(my_pass), True, False):
        print(brute)
