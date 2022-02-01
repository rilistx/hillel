from bs4 import BeautifulSoup
import requests

from Lesson_16.bank import Bank
from Lesson_16.currency import currency


class RaiffeisenBankAval(Bank):
    __URL = 'https://www.aval.ua/'

    def __get_html(self):
        response = requests.get(self.__URL)
        return response.text

    def get_currency_rate(self):
        currency_rate = {
            'rate': []
        }

        html = self.__get_html()
        soup = BeautifulSoup(html, 'lxml')

        contents = soup.find('div', class_='rates-block__wrapper').find_all('div', class_='rate-numbers')
        for line in contents:
            currency_name = None
            for key, value in currency.items():
                if key.lower() in line['class'][1].lower():
                    currency_name = value
                    break

            rates = line.find_all('span')
            currency_rate['rate'].append(
                {
                    'currency': currency_name,
                    'purchase_rate': str(round(float(rates[0].text.strip().strip('\n')), 2)),
                    'sale_rate': str(round(float(rates[1].text.strip().strip('\n')), 2)),
                }
            )

        return currency_rate


if __name__ == '__main__':
    from pprint import pprint
    bank = RaiffeisenBankAval()
    pprint(bank.get_currency_rate())
