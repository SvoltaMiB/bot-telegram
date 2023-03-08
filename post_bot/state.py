from enum import Enum

class State(Enum):
    """
        Define states
    """
    START = 0
    ASK_TITLE = 1
    TITLE = 2
    DESCRIPTION = 3
    ASK_ATTACHMENT = 4
    ATTACHMENT = 5
    END = 1


class CallbackData(Enum):
    """
        Define CallbackData for buttons
    """
    CREATE = 0
    ATTACHMENT_YES = 1
    ATTACHMENT_NO = 2