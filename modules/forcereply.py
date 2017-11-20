from telegram import ReplyMarkup


class ForceReply(ReplyMarkup):
    """
    Upon receiving a message with this object, Telegram clients will display a reply interface to
    the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be
    extremely useful if you want to create user-friendly step-by-step interfaces without having
    to sacrifice privacy mode.
    Attributes:
        force_reply (:obj:`True`): Shows reply interface to the user.
        selective (:obj:`bool`): Optional. Force reply from specific users only.
    Args:
        selective (:obj:`bool`, optional): Use this parameter if you want to force reply from
            specific users only. Targets:
            1) users that are @mentioned in the text of the Message object
            2) if the bot's message is a reply (has reply_to_message_id), sender of the
               original message.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.
    """

    def __init__(self, force_reply=True, selective=False, **kwargs):
        # Required
        self.force_reply = bool(force_reply)
        # Optionals
        self.selective = bool(selective)