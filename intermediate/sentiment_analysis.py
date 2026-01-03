from dataclasses import dataclass
from textblob import TextBlob

@dataclass
class Mood:
    text: str
    polarity: float

def get_mood(input_txt: str, *, sentiment):
    polarity = TextBlob(input_txt).sentiment.polarity

    if polarity >= sentiment:
        return Mood('😀', polarity)
    elif polarity <= -sentiment:
        return Mood('☹️', polarity)
    else:
        return Mood('😐', polarity)


def run():
    while True:
        txt = input('You: ')
        print(get_mood(txt, sentiment=0.3))

if __name__ == '__main__':
    run()
