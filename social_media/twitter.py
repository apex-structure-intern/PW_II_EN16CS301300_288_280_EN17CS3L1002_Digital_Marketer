import tweepy 
  
class Twitter:
    # Enter access Tokens
    consumer_key =""
    consumer_secret =""
    access_token =""
    access_token_secret =""
    
    def __init__(self):  
        # authentication 
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret) 
        self.auth.set_access_token(self.access_token, self.access_token_secret) 
   
        self.api = tweepy.API(self.auth) 
        
    def upload_post(self, caption = "Testing", path = "social_media/tumblr.png"):
        tweet =caption # toDo 
        image_path =path # toDo 
  
        # to attach the media file 
        status = self.api.update_with_media(image_path, tweet)
        #self.api.update_status(status = tweet)
        return True
        
    def generate_post(self):
        status = self.api.home_timeline()
        return status
    
    def validate(self, text):
        if(text == generate_post(self)):
            return True
        else:
            return False
        
        
        
#if __name__ == "__main__":
#    obj = Twitter()
    #obj.upload_post()
    #print(obj.generate_post())
