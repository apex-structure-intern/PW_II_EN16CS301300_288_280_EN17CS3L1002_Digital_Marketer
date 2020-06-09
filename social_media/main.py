# Main file for creating all the objects and passing it to controller.
import fb, tumblr, twitter, insta, myspace, tele
#import wechat

class Obj:
    def __init__(self):
        self.fb = fb.Fb()
        self.tumblr = tumblr.Tumblr()
        self.twitter = twitter.Twitter()
        self.insta = insta.Insta()
        #self.wechat = wechat.Wechat()
        #self.tel = tele.Telegram()
        self.myspace = myspace.Myspace()
        print("cool!")
        

