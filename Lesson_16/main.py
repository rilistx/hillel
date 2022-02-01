from Lesson_16.aval_bank import RaiffeisenBankAval
from Lesson_16.private_bank import PrivateBank
from Lesson_16.ukrsib_bank import UkrSibBank
from Lesson_16.obmenka_bank import ObmenkaPoint


banks = [
    RaiffeisenBankAval(),
    PrivateBank(),
    UkrSibBank(),
    ObmenkaPoint(),
]

for bank in banks:
    result = bank.get_currency_rate()
    rate = result['rate']
    for line in rate:
        print('Currency:', line['currency'])
        print('Purchase:', line['purchase_rate'])
        print('Sale:', line['sale_rate'])
        print('*' * 25)
    print()
