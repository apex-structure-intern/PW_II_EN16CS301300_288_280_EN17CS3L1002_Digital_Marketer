import pandas as pd
from send_mail import MailSender

class MassMail:
    def __init__(self):
        # Replace your emails recipients file with email.csv
        self.df = pd.read_csv('emails.csv')
        print(self.df.columns)
        self.recipients = list(self.df.email_id)
    
    def sender(self, text, mail_id, passwd):
        self.plaintext = text
        self.ourmailsender = MailSender(mail_id, passwd, ('smtp.gmail.com', 587))
        self.ourmailsender.set_message(self.plaintext, "This is a test", "Yuvraj Yadav")
        self.ourmailsender.set_recipients(self.recipients)
        self.ourmailsender.connect()
        self.ourmailsender.send_all()
    
    def broadcast(self):
        return False

#if __name__ == "__main__":
#    mail = MassMail('emails.csv')
#    mail.sender("message",'','')
