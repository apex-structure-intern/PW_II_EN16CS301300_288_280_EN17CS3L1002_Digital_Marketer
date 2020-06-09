# -*- coding: utf-8 -*-

import smtplib
import string
import random

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from email.mime.image import MIMEImage

class MailSender:
    
    def __init__(self, in_username, in_password, in_server=("smtp.gmail.com", 587), use_SSL=False):
        self.username = in_username
        self.password = in_password
        self.server_name = in_server[0]
        self.server_port = in_server[1]
        self.use_SSL = use_SSL

        if self.use_SSL:
            self.smtpserver = smtplib.SMTP_SSL(self.server_name, self.server_port)
        else:
            self.smtpserver = smtplib.SMTP(self.server_name, self.server_port)
        self.connected = False
        self.recipients = []

    def __str__(self):
        return "Type: Mail Sender \n" \
               "Connection to server {}, port {} \n" \
               "Connected: {} \n" \
               "Username: {}, Password: {}".format(self.server_name, self.server_port, self.connected, self.username, self.password)
    def template(self):
        pass

    def set_message(self, in_plaintext, in_subject="", in_from=None, in_htmltext=None):

        if in_htmltext is not None:
            self.html_ready = True
        else:
            self.html_ready = False

        if self.html_ready:
            self.msg = MIMEMultipart('alternative')  # 'alternative' allows attaching an html version of the message later
            self.msg.attach(MIMEText(in_plaintext, 'plain'))
            self.msg.attach(MIMEText(in_htmltext, 'html'))
        else:
            self.msg = MIMEText(in_plaintext, 'plain')

        self.msg['Subject'] = in_subject
        if in_from is None:
            self.msg['From'] = self.username
        else:
            self.msg['From'] = in_from
        self.msg["To"] = None
        self.msg["CC"] = None
        self.msg["BCC"] = None

    def clear_message(self):

        self.msg.set_payload("")

    def set_subject(self, in_subject):
        self.msg.replace_header("Subject", in_subject)

    def set_from(self, in_from):
        self.msg.replace_header("From", in_from)

    def set_plaintext(self, in_body_text):

        if not self.html_ready:
            self.msg.set_payload(in_body_text)
        else:
            payload = self.msg.get_payload()
            payload[0] = MIMEText(in_body_text)
            self.msg.set_payload(payload)

    def set_html(self, in_html):
     
        try:
            payload = self.msg.get_payload()
            payload[1] = MIMEText(in_html, 'html')
            self.msg.set_payload(payload)
        except TypeError:
            print("ERROR: "
                  "Payload is not a list. Specify an HTML message with in_htmltext in MailSender.set_message()")
            raise

    def set_recipients(self, in_recipients):
    
        if not isinstance(in_recipients, (list, tuple)):
            raise TypeError("Recipients must be a list or tuple, is {}".format(type(in_recipients)))

        self.recipients = in_recipients

    def add_recipient(self, in_recipient):

        self.recipients.append(in_recipient)

    def connect(self):
       
        if not self.use_SSL:
            self.smtpserver.starttls()
        self.smtpserver.login(self.username, self.password)
        self.connected = True
        print("Connected to {}".format(self.server_name))

    def disconnect(self):
        self.smtpserver.close()
        self.connected = False

    def send_all(self, close_connection=True):
     
        if not self.connected:
            raise ConnectionError("Not connected to any server. Try self.connect() first")

        print("Message: {}".format(self.msg.get_payload()))

        for recipient in self.recipients:
                self.msg.replace_header("To", recipient)
                print("Sending to {}".format(recipient))
                self.smtpserver.send_message(self.msg)

        print("All messages sent")

        if close_connection:
            self.disconnect()
            print("Connection closed")
