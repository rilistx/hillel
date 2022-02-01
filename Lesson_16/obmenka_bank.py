from bs4 import BeautifulSoup
import requests

from Lesson_16.bank import Bank
from Lesson_16.currency import currency


class ObmenkaPoint(Bank):
    __URL = 'https://obmenka.od.ua/'

    def __get_html(self):
        resp = requests.get(self.__URL)
        return resp.text

    def get_currency_rate(self):
        currency_rate = {
            'rate': []
        }

        html = self.__get_html()
        soup = BeautifulSoup(html, 'lxml')

        contents = soup.find_all('li', class_='currencies__block')
        for line in contents:
            name = line.find('div', class_='currencies__block-name').find('a').text.split()[1]
            if not name.upper().endswith('/UAH') or name[:3].lower() not in currency:
                continue

            name = name[:3]
            purchase = (
                line.
                find('div', class_='currencies__block-buy').
                find('div', class_='currencies__block-num').
                text.strip())

            sale = (
                line.
                find('div', class_='currencies__block-sale').
                find('div', class_='currencies__block-num').
                text.strip()
            )

            currency_rate['rate'].append(
                {
                    'currency': name,
                    'purchase_rate': str(round(float(purchase), 2)),
                    'sale_rate': str(round(float(sale), 2))
                }
            )

        return currency_rate


if __name__ == '__main__':
    from pprint import pprint
    bank = ObmenkaPoint()
    pprint(bank.get_currency_rate())
