# facebook graph api
import facebook


class Fb:
    
    def __init__(self):
        # Enter access tokens
        self.page_access_token = ""
        self.graph = facebook.GraphAPI(self.page_access_token)
        # Enter or generate facebook page id
        self.facebook_page_id = ""
    
    def upload_post(self, text, path = None):
        # For plan text:
        if(path == None):
            x = self.graph.put_object(self.facebook_page_id, "feed", message=text)
            return True
        elif(path != None):
            y = self.graph.put_photo(image=open(path, 'rb'), message=text)
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
        
#if __name__ == "__main__":
#    obj = Fb()
#    obj.upload_post("Testing 123") 
    #obj.generate_post()
