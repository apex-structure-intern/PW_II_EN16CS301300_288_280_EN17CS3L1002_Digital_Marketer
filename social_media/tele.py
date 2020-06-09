from telegram import *
from chatpermissions import ChatPermissions


class Telegram(TelegramObject):

    PRIVATE = 'private'
    
    GROUP = 'group'
    
    SUPERGROUP = 'supergroup'
    
    CHANNEL = 'channel'

    def __init__(self,
                 id,
                 type,
                 title=None,
                 username=None,
                 first_name=None,
                 last_name=None,
                 bot=None,
                 photo=None,
                 description=None,
                 invite_link=None,
                 pinned_message=None,
                 permissions=None,
                 sticker_set_name=None,
                 can_set_sticker_set=None,
                 slow_mode_delay=None,
                 **kwargs):
        # Required
        self.id = int(id)
        self.type = type
        # Optionals
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        # TODO: Remove (also from tests), when Telegram drops this completely
        self.all_members_are_administrators = kwargs.get('all_members_are_administrators')
        self.photo = photo
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = permissions
        self.slow_mode_delay = slow_mode_delay
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set

        self.bot = bot
        self._id_attrs = (self.id,)

    @property
    def link(self):
        if self.username:
            return "https://t.me/{}".format(self.username)
        return None

    @classmethod
    def de_json(cls, data, bot):
        if not data:
            return None

        data['photo'] = ChatPhoto.de_json(data.get('photo'), bot)
        from telegram import Message
        pinned_message = data.get('pinned_message')
        if pinned_message:
            pinned_message['default_quote'] = data.get('default_quote')
        data['pinned_message'] = Message.de_json(pinned_message, bot)
        data['permissions'] = ChatPermissions.de_json(data.get('permissions'), bot)

        return cls(bot=bot, **data)

    def send_action(self, *args, **kwargs):
        return self.bot.send_chat_action(self.id, *args, **kwargs)

    def leave(self, *args, **kwargs):
        return self.bot.leave_chat(self.id, *args, **kwargs)

    def get_administrators(self, *args, **kwargs):
        return self.bot.get_chat_administrators(self.id, *args, **kwargs)

    def get_members_count(self, *args, **kwargs):
        return self.bot.get_chat_members_count(self.id, *args, **kwargs)

    def get_member(self, *args, **kwargs):
        return self.bot.get_chat_member(self.id, *args, **kwargs)

    def kick_member(self, *args, **kwargs):
        return self.bot.kick_chat_member(self.id, *args, **kwargs)

    def unban_member(self, *args, **kwargs):
        return self.bot.unban_chat_member(self.id, *args, **kwargs)

    def set_permissions(self, *args, **kwargs):
        return self.bot.set_chat_permissions(self.id, *args, **kwargs)

    def set_administrator_custom_title(self, *args, **kwargs):
        return self.bot.set_chat_administrator_custom_title(self.id, *args, **kwargs)

    def send_message(self, *args, **kwargs):
        return self.bot.send_message(self.id, *args, **kwargs)

    def send_photo(self, *args, **kwargs):
        return self.bot.send_photo(self.id, *args, **kwargs)

    def send_audio(self, *args, **kwargs):
        return self.bot.send_audio(self.id, *args, **kwargs)

    def send_video(self, *args, **kwargs):
        return self.bot.send_video(self.id, *args, **kwargs)

    def send_video_note(self, *args, **kwargs):
        return self.bot.send_video_note(self.id, *args, **kwargs)

    def send_poll(self, *args, **kwargs):
        return self.bot.send_poll(self.id, *args, **kwargs)
    
    def broadcast(self, *args, **kwargs):
        self.send_message(self, *args, **kwargs)
        self.send_photo(self, *args, **kwargs)
        return True
