import re
from collections import Counter

from PyPDF2 import PdfReader


def pdf_text(file_name: str) -> list[str]:
    with open(file_name, 'rb') as pdf:
        reader = PdfReader(pdf)
        print(f'Number of pages : {len(reader.pages)}')
        extracted_text = [page.extract_text() for page in reader.pages]
        return extracted_text


def get_word_count(pages: list[str]) -> Counter:
    all_words = []
    for page in pages:
        split_words = re.split(r'\s+|[,;?!.-]\s*', page.lower())
        all_words += [word for word in split_words if word]

    return Counter(all_words)


if __name__ == '__main__':
    pages = pdf_text('sample.pdf')
    counter = get_word_count(pages)
    print('*' * 30)
    print('Words with highest frequencies')
    print('*' * 30)
    for word, mention in counter.most_common(5):
        print(f'{word:10} {mention:2} times')
