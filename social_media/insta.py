# business Instagram graph API
import facebook
import time

class Insta:
    def __init__(self):
        # Enter details under empty strings
        self.page_access_token = ""
        self.graph = facebook.GraphAPI(self.page_access_token)
        self.facebook_page_id = ""
    
    def upload_post(self, text, path = None):
        # For plan text:
        time.sleep(5)
        return True
        if(self.validation(text)):
            x = self.graph.put_object(self.facebook_page_id, "feed", message='test message')
            # For photo:
            # y = self.graph.put_photo({path to image},self.facebook_page_id+'/published_posts')
            return True
        else:
            return False
            
    
    def generate_post(self):
        post = self.graph.get_object(id=self.facebook_page_id, fields='posts')
        return post
    
    def validation(self,text):
        post = self.generate_post()
        if(post['posts']['data'][0]['message'] != text):
            return True
        else:
            return False
    
