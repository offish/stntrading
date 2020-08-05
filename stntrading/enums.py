import enum


class EStatusCodes(enum.IntEnum):
    READY_TO_BE_SENT = 0
    SENT = 1
    COMPLETED = 2
    CONFIRM_PENDING = 3
    CANCELLED_AFTER_SENDING = 15
    SENDING_FAILED = 20