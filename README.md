# stntrading
[![License](https://img.shields.io/github/license/offish/stntrading.svg)](https://github.com/offish/stntrading/blob/master/LICENSE)
[![Stars](https://img.shields.io/github/stars/offish/stntrading.svg)](https://github.com/offish/stntrading/stargazers)
[![Issues](https://img.shields.io/github/issues/offish/stntrading.svg)](https://github.com/offish/stntrading/issues)
[![Size](https://img.shields.io/github/repo-size/offish/stntrading.svg)](https://github.com/offish/stntrading)
[![Discord](https://img.shields.io/discord/467040686982692865?color=7289da&label=Discord&logo=discord)](https://discord.gg/t8nHSvA)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Interact with STNTrading.eu's API hosted at https://api.stntrading.eu

For getting inventories and item names, I recommend using [tf2-utils](https://github.com/offish/tf2-utils). 


## Installation
```bash
pip install stntrading
```

### Update
```bash
pip install --upgrade stntrading
```

# Setup
Find or register your API key on https://stntrading.eu/dev/apikey

If you want to access BETA endpoints shown [here](https://github.com/STNTrading/public-api/wiki), you need STN Premium.
For more information read [this](https://api.stntrading.eu/docs/#/beta).


# Usage
```python
>>> from stntrading import STN, EStateCodes

>>> stn = STN("26bf8abb59e86b4301aaff5b88547aaf") # (fake api key)

>>> stn.get_key_prices()
{'success': 1, 'result': {'pricing': {'buyPrice': 570.0, 'sellPrice': 606.0}}}

>>> stn.get_key_stock()
{'success': 1, 'result': {'stock': {'canBuy': 15, 'canSell': 15, 'stockLevel': 702, 'stockLimit': 1770}}}

>>> stn.request_key_trade("buy", 1)
{'success': 0, 'error': "Failed to create trade: 'NotEnoughCurrenciesUser'"}

>>> stn.get_trade_status(20530029)
{'success': 1, 'result': {'trade': {'state': 15, 'tradeOfferId': 6697968536}}}

>>> EStateCodes(15).name
CANCELLED_AFTER_SENDING

>>> stn.request_item_trade("buy", "The Team Captain", 1)
{'success': 1, 'result': {'tradeDetails': {'id': 20530029, 'bot': '76561198309976634'}}}

>>> stn.request_item_trade("sell", [12552033523], 1)
{'success': 0, 'error': "Failed to create trade: 'UserItemOverstocked'"}

# ----------------------
# if STN Premium access:
# ----------------------
>>> stn.get_schema()
{'success': 1, 'result': {'schema': ['A Brush with Death', 'A Color Similar to Slate', 'A Deep Commitment to Purple', ...]}}

>>> stn.get_item_details("The Team Captain")
{'success': 1, 'item': {'full_name': 'The Team Captain', 'pricing': {'buy': {'keys': 0, 'metal': 10.0}, 'sell': {'keys': 0, 'metal': 10.88}}, 'stock': {'level': 48, 'limit': 100}}}
```


# Documentation
Documentation can be found on the [official wiki](https://github.com/STNTrading/public-api/wiki) or using [Swagger](https://api.stntrading.eu/docs/).


# License
Copyright (c) 2020-2024 offish

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

