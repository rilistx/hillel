import requests

from Lesson_16.bank import Bank
from Lesson_16.currency import currency


class PrivateBank(Bank):
    __URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

    def __get_json(self):
        resp = requests.get(self.__URL)
        return resp.json()

    def get_currency_rate(self):
        currency_rate = {
            'rate': []
        }

        result = self.__get_json()

        for line in result:
            if line['ccy'].strip().lower() in currency.keys():
                currency_rate['rate'].append(
                    {
                        'currency': currency.get(line['ccy'].lower()),
                        'purchase_rate': str(round(float(line['buy']), 2)),
                        'sale_rate': str(round(float(line['sale']), 2)),
                    }
                )

        return currency_rate


if __name__ == '__main__':
    from pprint import pprint
    pb = PrivateBank()
    pprint(pb.get_currency_rate())
