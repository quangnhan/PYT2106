import smtplib, ssl
from server import Server

class Gmail:

    __port = 465  # For SSL
    __smtp_server = "smtp.gmail.com"
    __sender_email = "phuongnv510@gmail.com"  # Enter your address
    # receiver_email = "phuongnv510@gmail.com"  # Enter receiver address,nhan.vo@menlosecurity.com
    __password = "fgndpdsinvwjykat"

    def send_mail(self, receiver_email, message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.__smtp_server, self.__port, context=context) as server:
            server.login(self.__sender_email, self.__password)
            server.sendmail(self.__sender_email, receiver_email, message)

    def congratz(self, receiver_email, receiver_name):
        message = f"""\
        Subject: Hi {receiver_name}

        Congratulation email from Python."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.__smtp_server, self.__port, context=context) as server:
            server.login(self.__sender_email, self.__password)
            server.sendmail(self.__sender_email, receiver_email, message)


if __name__ == "__main__":
    server = Server
    users = server.get_user()

    email = Gmail()
    for user in users:
        email.Congratz(user["name"], user["email"])


    # receiver_mail = "luckyteddy96@gmail.com"
    # message = """\
    # Subject: Hi there

    # This message is sent from Python."""
    # email.send_mail(receiver_mail, message)