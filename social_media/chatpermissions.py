from telegram import TelegramObject


class ChatPermissions(TelegramObject):

    def __init__(self, can_send_messages=None, can_send_media_messages=None, can_send_polls=None,
                 can_send_other_messages=None, can_add_web_page_previews=None,
                 can_change_info=None, can_invite_users=None, can_pin_messages=None, **kwargs):
        # Required
        self.can_send_messages = can_send_messages
        self.can_send_media_messages = can_send_media_messages
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages

    @classmethod
    def de_json(cls, data, bot):
        if not data:
            return None

        return cls(**data)


