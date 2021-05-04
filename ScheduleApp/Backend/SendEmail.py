import smtplib, ssl
import os
import sys

class SendEmail:
    def sendEmail(self, recipient, message):
        is_sent = False
    
        try:
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "managerEmailTest@gmail.com"  # Enter your address
            password = "mgr123456"

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient, "\n" + message)

            is_sent = True
            return is_sent
        except Exception as ex:
            is_sent = False
            return is_sent