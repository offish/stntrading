from .methods import request, post


class STN:
    URI = 'https://api.stntrading.eu/'

    def __init__(self, api_key: str):
        self.payload = {'apikey': api_key}

    def get_key_prices(self) -> dict:
        uri = self.URI + 'GetKeyPrices/v1'
        return request(uri, self.payload)

    def get_trade_status(self, trade_id: int) -> dict:
        if not isinstance(trade_id, int):
            raise TypeError('trade_id must be int')

        uri = self.URI + 'GetTradeStatus/v1'
        payload = {**self.payload, 'id': trade_id}
        return request(uri, payload)

    def request_key_trade(self, action: str, amount: int) -> dict:
        if not isinstance(action, str):
            raise TypeError('action must be str')

        if not isinstance(amount, int):
            raise TypeError('amount must be int')

        if not (action == 'buy' or action == 'sell'):
            raise ValueError('action must be buy or sell')

        if amount < 1 or amount > 10:
            amount = 1

        uri = self.URI + 'RequestKeyTrade/v1'
        payload = {**self.payload,
                   'action': action, 'amount': amount}
        return post(uri, payload)
