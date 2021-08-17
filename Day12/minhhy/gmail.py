import smtplib, ssl
import os

'''
ERROR: ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)

FIX: https://www.dev2qa.com/how-to-fix-python-error-certificate-verify-failed-unable-to-get-local-issuer-certificate-in-mac-os/
'''

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "b.tintuk@gmail.com"   # Enter your address
receiver_email = "b.tintuk@gmail.com" # Enter receiver address
password = os.environ['GMAIL_TOKEN']  # https://devanswers.co/create-application-specific-password-gmail/
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)