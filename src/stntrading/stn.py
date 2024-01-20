from .exceptions import *
import requests
import json


class STN:
    def __init__(self, api_key: str):
        self.URL = "https://api.stntrading.eu"
        self.api_key = api_key

    @staticmethod
    def __check_premium_access(response: dict) -> None:
        error = response.get("error", "")

        if "stn premium" in error.lower():
            raise NoPremiumAccess("You need STN Premium in order to use this endpoint")

    @staticmethod
    def __is_valid_intent(intent: str, beta: bool = False) -> bool:
        if not beta:
            return intent in [
                "buy",
                "sell",
            ]

        return intent in [
            "quick_buy",
            "sell_partially_qualified_item_instances",
        ]

    def __get_request(self, endpoint: str, params: dict = {}) -> dict:
        params["apikey"] = self.api_key
        request = requests.get(self.URL + endpoint, params)
        response = request.json()
        self.__check_premium_access(response)
        return response

    def __post_request(self, endpoint: str, data: dict = {}) -> dict:
        data["apikey"] = self.api_key

        request = requests.post(
            self.URL + endpoint,
            data=data,
        )
        response = request.json()
        self.__check_premium_access(response)
        return response

    def get_schema(self) -> dict:
        return self.__get_request("/GetSchema/v1")

    def get_user_details(self, steam_id: str) -> dict:
        return self.__get_request("/GetUserDetails/v1", {"steamid": steam_id})

    def get_key_prices(self) -> dict:
        return self.__get_request("/GetKeyPrices/v1")

    def get_item_details(self, item_name: str) -> dict:
        return self.__get_request("/GetItemDetails/v1", {"full_name": item_name})

    def get_key_stock(self) -> dict:
        return self.__get_request("/GetKeyStock/v1")

    def get_trade_status(self, trade_id: int | str) -> dict:
        return self.__get_request("/GetTradeStatus/v1", {"id": int(trade_id)})

    def request_key_trade(self, intent: str, amount: int = 1) -> dict:
        if not self.__is_valid_intent(intent):
            raise InvalidIntent(f"{intent} is an invalid intent")

        if amount not in range(1, 10 + 1):
            raise ValueError("amount must be in range [1, 10]")

        return self.__post_request(
            "/RequestKeyTrade/v1", {"action": intent, "amount": amount}
        )

    def request_item_trade(
        self, intent: str, items: str | list[int], amount: int = 1
    ) -> dict:
        """item name if buy, assetids if sell"""
        if intent == "buy":
            intent = "quick_buy"

        if intent == "sell":
            intent = "sell_partially_qualified_item_instances"

        if not self.__is_valid_intent(intent, True):
            raise InvalidIntent(f"{intent} is an invalid intent")

        payload = {
            "request_type": intent,
            intent: {
                "app_ctx_id": "440_2",
            },
        }

        if intent == "quick_buy":
            payload[intent]["full_name"] = items
            payload[intent]["amount"] = amount
        else:
            payload[intent]["assets"] = items

        return self.__post_request(
            "/RequestItemTrade/v1", {"fullRequest": json.dumps(payload)}
        )
