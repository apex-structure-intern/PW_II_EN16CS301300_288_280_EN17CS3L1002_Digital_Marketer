import pytumblr

class Tumblr:
    
    def __init__(self):
        # Enter those details
        self.consumer_key = ''
        self.consumer_secret = ''
        self.token_key = '' 
        self.token_secret = ''

        self.client = pytumblr.TumblrRestClient(
                   self.consumer_key,
                   self.consumer_secret,
                   self.token_key,
                   self.token_secret
                   )
                      
    def upload_post(self,caption, path = "social_media/tumblr.png"):
        # Enter user profile
        user_profile = ""
        self.client.create_photo(user_profile,
                                state="published",
                                tags=caption,
                                data=path
                                )
        return True
    
    def generate_post(self):
        pass
    
    def validate(self):
        pass
        
        
#if __name__ == "__main__":
#    obj = Tumblr()
#    obj.upload_post()    
