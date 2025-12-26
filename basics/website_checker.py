import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus


def get_websites(file_name: str) -> list[str]:
    websites: list[str] = []
    with open(file_name, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            if 'https://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])

    return websites


def get_user_agent():
    ua = UserAgent()
    return ua.chrome


def print_status(code: int):
    desc = '{???} Unknow code'
    for value in HTTPStatus:
        if value == code:
            desc = f'({value.value} {value.name}) ({value.description})'

    return desc


def check_website(website: str, user_agent: str):
    try:
        status_code = requests.get(url=website, headers={'User-Agent': user_agent}).status_code
        print(f'{print_status(status_code)} {website}')
    except:
        print(f'Error connecting to website : {website}')


def main():
    for site in get_websites('websites.csv'):
        check_website(site, get_user_agent())


if __name__ == '__main__':
    main()
