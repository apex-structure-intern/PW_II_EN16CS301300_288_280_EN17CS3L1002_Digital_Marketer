from send_mail import MailSender

plaintext = "Hello, \n" \
            "I'm just testing my new email sending system here.\n" \
            "Tester"
            
# Enter details here
email = ''
password = ''
recipients = ['','']

ourmailsender = MailSender(email, password, ('smtp.gmail.com', 587))
ourmailsender.set_message(plaintext, "This is a test", "Yuvraj Yadav")
ourmailsender.set_recipients(recipients)
ourmailsender.connect()
ourmailsender.send_all()
