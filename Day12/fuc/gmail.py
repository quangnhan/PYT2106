import smtplib, ssl
from server import Server

class Gmail:
    __port = 465  # For SSL
    __smtp_server = "smtp.gmail.com"
    __sender_email = "icdaltmoody@gmail.com"  # Enter your address
    
    __password = "itrgpbgdqeabnpce"


    def send(self,receiver_email, massage):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.__smtp_server, self.__port, context=context) as server:
            server.login(self.__sender_email, self.__password)
            server.sendmail(self.__sender_email, receiver_email, message)

if __name__ =="__main__":
    gmail = Gmail()
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    server = Server()
    data = {
        "name": "fucdeeptry",
        "email": "lightvhp@gmail.com"
    }
    server.edit_gmail_user(1, data)
    print(server.get_gmail())
    for receiver_user in server.get_gmail():
        message = f"""\
        Hi {receiver_user["name"]}

        This message is sent from Python.
        """
        receiver_email = receiver_user["email"]
        gmail.send(receiver_email, message)