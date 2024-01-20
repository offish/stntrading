class STNTradingException(Exception):
    """General exception"""


class NoPremiumAccess(STNTradingException):
    """
    Raised if user is trying to access a beta endpoint while not having premium access
    """


class InvalidIntent(STNTradingException):
    """Raised if intent is invalid"""
