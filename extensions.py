import requests
import json
from rt import keys




class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://api.fastforex.io/fetch-one?from={quote_ticker}&to={base_ticker}&api_key=a8c5d78b71-4bb800ad36-r3wgyn')

        total_base = round(float(amount)) * float(json.loads(r.content)['result'][keys[base]])


        return total_base

