import time
import itchat
from itchat.content import *

class Wechat:
    def __init__(self):
        itchat.auto_login(True)
        itchat.run(True)
        
    @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
    def text_reply(msg):
        msg.user.send('%s: %s' % (msg.type, msg.text))

    @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
    def download_files(msg):
        msg.download(msg.fileName)
        typeSymbol = {
            PICTURE: 'img',
            VIDEO: 'vid', }.get(msg.type, 'fil')
        return '@%s@%s' % (typeSymbol, msg.fileName)

    @itchat.msg_register(FRIENDS)
    def add_friend(msg):
        msg.user.verify()
        msg.user.send('Nice to meet you!')

    @itchat.msg_register(TEXT, isGroupChat=True)
    def text_reply(msg):
        if msg.isAt:
            msg.user.send(u'@%s\u2005I received: %s' % (
                msg.actualNickName, msg.text))
