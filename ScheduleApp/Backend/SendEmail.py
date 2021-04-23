import smtplib, ssl
import os
import sys

class SendEmail:
    def sendEmail(self, recipient):
    
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "tylerfreed2001@gmail.com"  # Enter your address
        receiver_email = recipient  # Enter receiver address
        password = "mypassword"
        message = """\
        Here is your schedule for the month
        """

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)