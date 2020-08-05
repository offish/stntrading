py-stntrading
=============
|license| |stars| |issues| |repo_size| |chat|

Easily interact with `STNTrading`_'s public API.

.. _`STNTrading`: https://stntrading.eu

.. contents:: Table of Contents
    :depth: 2

Installation
------------

.. code-block:: text

    pip install stntrading

Setup
-----
Registering an API Key
^^^^^^^^^^^^^^^^^^^^^^
Visit `this`_ page and register an API Key. Make sure to sign in with the account you will use the API with. 

.. _this: https://stntrading.eu/dev/apikey

Example
-------

.. code-block:: python

    >>> from stntrading import STN, EStatusCodes

    >>> stn = STN('your-api-key')

    >>> stn.get_key_prices()
    {'success': 1, 'result': {'pricing': {'buyPrice': 477, 'sellPrice': 486}}}

    >>> stn.get_trade_status(trade-id-as-number)
    {'success': 1, 'result': {'trade': {'state': 2, 'tradeOfferId': 1407310362}}}

    >>> stn.request_key_trade('buy', 1)
    {'success': 1, 'result': {'tradeDetails': {'id': 7563021, 'bot': '76561198311345646'}}}

    >>> EStatusCodes(1)
    EStatusCodes.SENT


Documentation
-------------
Every endpoint to STN's API is documented by STN themselves, and is available `here`_.

.. _here: https://github.com/STNTrading/public-api/wiki

License
-------
Copyright (c) 2020 `offish`_

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

.. _offish: https://offi.sh


.. |license| image:: https://img.shields.io/github/license/offish/py-stntrading.svg
    :target: https://github.com/offish/py-stntrading/blob/master/LICENSE
    :alt: License

.. |stars| image:: https://img.shields.io/github/stars/offish/py-stntrading.svg
    :target: https://github.com/offish/py-stntrading/stargazers
    :alt: Stars

.. |issues| image:: https://img.shields.io/github/issues/offish/py-stntrading.svg
    :target: https://github.com/offish/py-stntrading/issues
    :alt: Issues

.. |repo_size| image:: https://img.shields.io/github/repo-size/offish/py-stntrading.svg
    :target: https://github.com/offish/py-stntrading
    :alt: Repo Size

.. |chat| image:: https://img.shields.io/discord/467040686982692865.svg
    :target: https://discord.gg/t8nHSvA
    :alt: Discord
