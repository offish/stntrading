from tests.config import STN_PREMIUM_KEY, STN_NON_PREMIUM_KEY
from src.stntrading import STN, NoPremiumAccess, InvalidIntent
from unittest import TestCase


class TestSTN(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        self.stn_premium = STN(STN_PREMIUM_KEY)
        self.stn = STN(STN_NON_PREMIUM_KEY)
        super().__init__(methodName)

    def test_premium_access(self):
        self.assertRaises(
            NoPremiumAccess, self.stn.get_item_details, "The Team Captain"
        )

        details = self.stn_premium.get_item_details("The Team Captain")
        self.assertEqual(details["success"], 1)

    # def test_invalid_intent(self):
    #     self.assertRaises(InvalidIntent, self.stn.request_key_trade, "quick_buy")
    #     self.assertRaises(
    #         InvalidIntent,
    #         self.stn.request_key_trade,
    #         "sell_partially_qualified_item_instances",
    #     )
    #     self.assertRaises(InvalidIntent, self.stn.request_item_trade, "buy", [])
    #     self.assertRaises(InvalidIntent, self.stn.request_item_trade, "sell", [])
