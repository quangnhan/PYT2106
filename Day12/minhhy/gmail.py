import smtplib, ssl
import os

'''
ERROR: ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)

FIX: https://www.dev2qa.com/how-to-fix-python-error-certificate-verify-failed-unable-to-get-local-issuer-certificate-in-mac-os/
'''
class Gmail:
    __port = 465  # For SSL
    __smtp_server = "smtp.gmail.com"
    __sender_email = "b.tintuk@gmail.com"
    __password = os.environ['GMAIL_TOKEN']

    def send_email(self, receiver_email, message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.__smtp_server, self.__port, context=context) as server:
            server.login(self.__sender_email, self.__password)
            server.sendmail(self.__sender_email, receiver_email, message)


if __name__ == "__main__":
    receiver_email = "b.tintuk@gmail.com"  # Enter receiver address
    message = """\
    Subject: Hi there
    This message is sent from Python."""

    gmail = Gmail()
    gmail.send_email(receiver_email, message)