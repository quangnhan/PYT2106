import smtplib, ssl
from server import Server
class Gmail:

    __port = 465  # For SSL
    __smtp_server = "smtp.gmail.com"
    __sender_email = "phamanhquangit@gmail.com"  # Enter your address
    __password = "tlujydppiqnfldbi"
    
    def sendmail(self, receiver_email,message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.__smtp_server, self.__port, context=context) as server:
            server.login(self.__sender_email, self.__password)
            server.sendmail(self.__sender_email, receiver_email, message)
if __name__ =="__main__":
    server = Server()
    users = server.get_user()
    email = []
    for i in users:
        receiver_email = i['email']
        message = """\
        Subject: Hi there

        This message is sent from Python."""
        gmail = Gmail()
        print(gmail.sendmail(receiver_email,message))